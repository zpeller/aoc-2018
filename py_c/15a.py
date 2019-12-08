#!/usr/bin/python

import copy
import sys
import time

if len(sys.argv)>1:
	input_file=sys.argv[1]
else:
	input_file='15x.txt'

debug = True

num_elves = 0
num_goblins = 0

fighters = []
fighter_id_list = []
hitpoints = {}
fighter_pos_list = {}
cave_map = []
id_map = []
cave_width = 0
cave_height = 0

attack_power_goblin = 3
attack_power_elf = 23
init_hit_points = 200

def dprint(*arg):
	if not debug:
		return
	print(arg)

def get_fighter_hp_at(x, y):
	global id_map
	fighter_id = id_map[y][x]
	return hitpoints[fighter_id]

def get_fighter_id_at(x, y):
	global id_map
	return id_map[y][x]

def print_cave_map(l_cave_map):
	if not debug:
		return

	y=0
	for cave_line in l_cave_map:
		out = '  '
		x=0
		for c in cave_line:
			if c in ('E', 'G'):
				out += c + ':'+ str(get_fighter_hp_at(x,y)) +' '
			x += 1
		print("".join(map(str, cave_line)) + out)
		y += 1

fighter_id = 0
with open(input_file) as f:
	y = 0
	for cave_line in f:
		cave_line = list(cave_line.strip('\n'))
		id_line = list(cave_line)
		x = 0
		for c in cave_line:
			if c in ('E', 'G'):
				fighters.append((x, y))
				hitpoints[fighter_id] = init_hit_points
				fighter_pos_list[fighter_id] = (x, y)
				if c=='E':
					num_elves += 1
				else:
					num_goblins += 1
				id_line[x] = fighter_id
				fighter_id_list.append(fighter_id)
				fighter_id += 1

			x += 1
		cave_map.append(cave_line)
		id_map.append(id_line)
		y += 1
	cave_height=y
	cave_width=len(cave_map[0])

print_cave_map(cave_map)
print_cave_map(id_map)
dprint(fighters)
dprint(fighter_id_list)
dprint(fighter_pos_list)
dprint(hitpoints)

def sortKey(coord):
	return ((coord[1], coord[0]))

def adjacent_field_coords_list(x, y):
	return ((x, y-1), (x-1, y), (x+1, y), (x, y+1))

def first_adjacent_enemy(l_cave_map, fighter, fighter_type):	# in reading order

	f_x=fighter[0]
	f_y=fighter[1]
	enemy_type = 'G' if fighter_type=='E' else 'E'
	minhp=init_hit_points+1

	for (x, y) in adjacent_field_coords_list(f_x, f_y):
#		print(x,y,l_cave_map[y][x])
		if (l_cave_map[y][x]==enemy_type) and minhp>get_fighter_hp_at(x,y):
			minhp, minx, miny = get_fighter_hp_at(x,y), x, y
	if minhp<init_hit_points+1:
		return (minx, miny)

	return None

def has_adjacent_previous_move(l_cave_map, m_x, m_y, level):	# in reading order
	prev_level = level-1

	for (x, y) in adjacent_field_coords_list(m_x, m_y):
		if (l_cave_map[y][x]==prev_level):
			return True

	return False

def find_reading_order_target(l_cave_map, target_field_list, fighter_type):
	target_field_list = sorted(target_field_list, key=sortKey)
	for (x,y) in target_field_list:
		enemy = first_adjacent_enemy(l_cave_map, (x, y), fighter_type)
		if enemy:
			return (x, y)
	return None

def find_prev_move_coords(l_cave_map, possible_moves, level):

	if level==1:
		possible_moves = sorted(possible_moves, key=sortKey)
		return possible_moves[0]
		
	prev_level = level-1

	next_move_list = []
	for move in possible_moves:
		for (x, y) in adjacent_field_coords_list(move[0], move[1]):
			if (x,y) in next_move_list:
				continue
			if (l_cave_map[y][x]==prev_level):
				next_move_list.append((x,y))

#	print (prev_level, next_move_list)
	return find_prev_move_coords(l_cave_map, next_move_list, level-1)


def find_move_path(l_cave_map, fighter, fighter_type):
	global cave_width
	global cave_height

	search_map = copy.deepcopy(l_cave_map)

	f_x=fighter[0]
	f_y=fighter[1]
	enemy_type = 'G' if fighter_type=='E' else 'E'

	cells_filled = 1
	move_level = 1
	search_map[f_y][f_x] = 0
	while cells_filled>0:
		cells_filled = 0
		moves_list = []
		for x in range(1, cave_width):
			for y in range(1, cave_height):
				if search_map[y][x]=='.' and has_adjacent_previous_move(search_map, x, y, move_level):
					search_map[y][x] = move_level
					moves_list.append((x,y))
					cells_filled += 1
#		print(move_level, cells_filled)

		best_target = find_reading_order_target(search_map, moves_list, fighter_type)
		if (best_target):
#			print_cave_map(search_map)
#			print('Best target:', best_target)
			next_move = find_prev_move_coords(search_map, [best_target], move_level)
#			print('Next move:', next_move)
			return(next_move)

#		print_cave_map(search_map)
		move_level += 1
	return None

def move_fighter(l_cave_map, fighter_id, prev_pos, next_pos):
	global id_map
	global fighter_pos_list
	fighter_pos_list[fighter_id] = next_pos
	prev_x, prev_y = prev_pos[0], prev_pos[1]
	next_x, next_y = next_pos[0], next_pos[1]
	fighter_type = get_fighter_type(prev_pos)
	l_cave_map[prev_y][prev_x] = '.'
	id_map[prev_y][prev_x] = '.'
	l_cave_map[next_y][next_x] = fighter_type
	id_map[next_y][next_x] = fighter_id
	return (next_x, next_y)

def attack(l_cave_map, fighter, enemy_pos):
	global attack_power_elf
	global attack_power_goblin
	enemy_id = get_fighter_id_at(enemy_pos[0], enemy_pos[1])
	fighter_type = get_fighter_type(fighter)
	attack_power = attack_power_elf if fighter_type == 'E' else attack_power_goblin
	enemy_hp = hitpoints[enemy_id] - attack_power

	hitpoints[enemy_id] = enemy_hp
	if enemy_hp<= 0:
		remove_fighter(l_cave_map, enemy_pos)
		hitpoints[enemy_id] = 0
#		print('Fighter eliminated', enemy_pos)
		return True
	return False

def remove_fighter(l_cave_map, fighter_pos):
	global num_elves
	global num_goblins
	global id_map
	global fighter_pos_list
	fighter_id = get_fighter_id_at(fighter_pos[0], fighter_pos[1])
	fighter_id_list.remove(fighter_id)
	del fighter_pos_list[fighter_id]
	f_x, f_y = fighter_pos[0], fighter_pos[1]
	fighter_type = get_fighter_type(fighter_pos)
	l_cave_map[f_y][f_x] = '.'
	id_map[f_y][f_x] = '.'
	if fighter_type == 'E':
		num_elves -= 1
		print("Elf died, aborted!")
		sys.exit(1)
	else:
		num_goblins -= 1

def get_fighter_type(fighter):
	global cave_map
	return cave_map[fighter[1]][fighter[0]]

print("")
iter_no = 1
while iter_no<400 and num_elves>0 and num_goblins>0:
#	fighters = sorted(fighters, key=sortKey)
	fighters = sorted(fighter_pos_list.items(), key=lambda x: (x[1][1],x[1][0]))
#	dprint('Iter:', iter_no, hitpoints, fighters)
	next_fighters = []
	for fighter_id, fighter in fighters:
#		print(fighter)
		if fighter_id not in fighter_id_list:
#			dprint('Fighter already eliminated, skipped', fighter)
			continue

		enemy_pos = first_adjacent_enemy(cave_map, fighter, get_fighter_type(fighter))
		if (enemy_pos):
			if attack(cave_map, fighter, enemy_pos) and enemy_pos in next_fighters:
				next_fighters.remove(enemy_pos)
			next_fighters.append(fighter)
			continue

		next_pos = find_move_path(cave_map, fighter, get_fighter_type(fighter))
		if (next_pos):
			n_fighter = move_fighter(cave_map, fighter_id, (fighter[0], fighter[1]), next_pos)
			enemy_pos = first_adjacent_enemy(cave_map, n_fighter, get_fighter_type(n_fighter))
			if (enemy_pos):
				if attack(cave_map, n_fighter, enemy_pos) and enemy_pos in next_fighters:
					next_fighters.remove(enemy_pos)
			next_fighters.append(n_fighter)
		else:
			next_fighters.append(fighter)
	fighters = next_fighters
	iter_no += 1
	print_cave_map(cave_map)
	time.sleep(0.5)
	print("")


# print(hitpoints)
print('Completed rounds: ', iter_no-2, 'remaining hitpoints:', sum(hitpoints.values()), 'result: ', (iter_no-2)*sum(hitpoints.values()), 'elf_power: ', attack_power_elf )

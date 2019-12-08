#!/usr/bin/python

import sys

input_file='20.txt'
debug = True

room_doors = {}
room_dists = {}
input_list = []
opposite_move_tokens = { 'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N' }
token_id=1


def dprint(*arg):
	if not debug:
		return
	print(arg)

def read_input_file():
	global input_list
	with open(input_file) as f:
		for line in f:
			line = line.strip('\n')
			input_list = list(line)

def draw_room(room_pos):
	if room_pos not in room_doors:
		return '..', '..'
	room = [['#', '#'], ['#', '.']]
	for door in room_doors[room_pos]:
		if door=='N':
			room[0][1] = '-'
		elif door=='W':
			room[1][0] = '|'
	return "".join(room[0]), "".join(room[1])

def print_room_map():
	global room_doors
	line_len = 0
	min_y = min(room_doors, key=lambda x: x[1])[1]
	max_y = max(room_doors, key=lambda x: x[1])[1]
	min_x = min(room_doors, key=lambda x: x[0])[0]
	max_x = max(room_doors, key=lambda x: x[0])[0]
	sorted_rooms = sorted(room_doors, key=lambda x: (x[1], x[0]))
	for y in range (min_y, max_y+1):
		line0, line1 = '', ''
		for x in range (min_x, max_x+1):
			l0, l1 = draw_room((x, y))
			line0 += l0
			line1 += l1
		print line0+'#'
		print line1+'#'
		line_len = len(line0)
	line0 = ''
	for y in range (line_len+1):
		line0 += '#'
	print line0

def add_door(room_coords, movement_token):
	global room_doors
	if room_coords not in room_doors:
		room_doors[room_coords] = [movement_token]
	else:
		if movement_token not in room_doors[room_coords]:
			room_doors[room_coords].append(movement_token)

def add_room_with_door(room_coords, movement_token):
	global room_doors
	if room_coords not in room_doors:
		room_doors[room_coords] = []
	if movement_token:
		add_door(room_coords, opposite_move_tokens[movement_token])

def room_coords_after_move(room_coords, movement_token):
	if movement_token=='E':
		return (room_coords[0]+1, room_coords[1])
	elif movement_token=='W':
		return (room_coords[0]-1, room_coords[1])
	elif movement_token=='S':
		return (room_coords[0], room_coords[1]+1)
	elif movement_token=='N':
		return (room_coords[0], room_coords[1]-1)
	else:
		print("Invalid move token:" , movement_token)
		sys.exit(1)

def find_closing_paren(pos):
	cnt_open_paren = 1
	token_pos = pos
	while cnt_open_paren>0:
		token_pos += 1
		if input_list[token_pos] == '(':
			cnt_open_paren += 1
		elif input_list[token_pos] == ')':
			cnt_open_paren -= 1
	return token_pos

def move(pos, dir_token):
	add_door(pos, dir_token)
	new_pos = room_coords_after_move(pos, dir_token)
	add_room_with_door(new_pos, dir_token)
	return new_pos

def get_start_pos_list(start_pos, token_id, end_token_id):
	act_pos = start_pos
	pos_list = [(start_pos, token_id)]
	act_id = token_id
	while act_id < end_token_id:
		act_token = input_list[act_id]
		if act_token == '|':
			pos_list.append((start_pos, act_id+1))
		elif act_token == '(':
			act_id = find_closing_paren(act_id)
		elif act_token == ')':
			break
		act_id += 1
	return pos_list

def start_branch(start_pos, token_id, end_token_id):
	start_pos_list = get_start_pos_list(start_pos, token_id, end_token_id)

	end_pos_list = []

	while len(start_pos_list) > 0:
#		print start_pos_list
		act_pos, act_token_id = start_pos_list.pop(0)
#		print act_pos, act_token_id
		while act_token_id < end_token_id:
			act_token = input_list[act_token_id]
			if act_token == '(':
				start_pos_list.extend( start_branch(act_pos, act_token_id+1, find_closing_paren(act_token_id)) )
				break
			if act_token in (')', '$'):
				return end_pos_list
			if act_token == '|':
				if (act_pos, end_token_id+1) not in end_pos_list:
					end_pos_list.append( (act_pos, end_token_id+1) )
#				print ('EPL: ', end_pos_list)
				break
			if act_token in ('E', 'W', 'S', 'N'):
				act_pos = move(act_pos, act_token)
				print (act_token_id, act_token, act_pos)
			act_token_id += 1
	return end_pos_list

def add_room_with_dist(room_coords, dist):
	global room_dists
	if room_coords not in room_dists:
		room_dists[room_coords] = dist
		return True
	else:
		return False

def build_dist_map():
	dist = 0
	while True:
		new_rooms_found = False
		coord_list = []
		for coords, room_dist in room_dists.items():
			if room_dist == dist:
				coord_list.append(coords)
#		print dist, coord_list
		for coords in coord_list:
#		 	print coords, room_doors[coords]
			for movement_token in room_doors[coords]:
				next_room = room_coords_after_move(coords, movement_token)
				new_room_added = add_room_with_dist(next_room, dist+1)
				new_rooms_found = new_rooms_found or new_room_added
		if not new_rooms_found:
			break
		dist += 1
	return dist

def count_rooms_min_1000():
	cnt = 0
	for coords, room_dist in room_dists.items():
		if room_dist >= 1000:
			cnt += 1
	return cnt

read_input_file()
print input_list

add_room_with_door((0,0), None)
start_branch((0, 0), 1, len(input_list)-1)

# print room_doors
print_room_map()

add_room_with_dist((0,0), 0)
max_dst = build_dist_map()
# print room_dists
print('max dst:', max_dst)
min_1000_doors = count_rooms_min_1000()
print('min 1000 doors:', min_1000_doors)


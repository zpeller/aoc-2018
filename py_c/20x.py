#!/usr/bin/python

import sys
import exrex

#input_file='20a0.txt'
input_file='20.txt'
debug = True

room_doors = {}
input_list = []
input_line = ''
opposite_move_tokens = { 'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N' }
token_id=1


def dprint(*arg):
	if not debug:
		return
	print(arg)

def read_input_file():
	global input_list
	global input_line
	with open(input_file) as f:
		for line in f:
			line = line.strip('\n')
			input_list = list(line)
			input_line = line

def draw_room(room_pos):
	if room_pos not in room_doors:
		return '...', '...', '...'
	room = [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']]
	for door in room_doors[room_pos]:
		if door=='N':
			room[0][1] = '-'
		elif door=='S':
			room[2][1] = '-'
		elif door=='W':
			room[1][0] = '|'
		else:
			room[1][2] = '|'
	return "".join(room[0]), "".join(room[1]), "".join(room[2])

def print_room_map():
	global room_doors
	sorted_rooms = sorted(room_doors, key=lambda x: (x[1], x[0]))
	for y in range (min(sorted_rooms)[1], max(sorted_rooms)[1]+1):
		line0, line1, line2 = '', '', ''
		for x in range (min(sorted_rooms)[0], max(sorted_rooms)[0]+1):
			l0, l1, l2 = draw_room((x, y))
			line0 += l0
			line1 += l1
			line2 += l2
		print line0
		print line1
		print line2

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

read_input_file()
print input_list

def start_branch(start_pos, token_id):
	act_pos = start_pos
	pos_list = []
	while token_id < len(input_list):
		act_token = input_list[token_id]
		if act_token == '(':		# temp!
			token_id += 1
			branch_pos_list = start_branch(act_pos)
			# ??? break?
		if act_token in (')', '$'):
			token_id += 1
			return pos_list
		if act_token == '|':
		 	if act_pos not in pos_list:
		 		pos_list.append(act_pos)
			act_pos = start_pos
			token_id += 1
			continue
		if act_token in ('E', 'W', 'S', 'N'):
			print (token_id, act_token)
			add_door(act_pos, act_token)
			new_pos = room_coords_after_move(act_pos, act_token)
			add_room_with_door(new_pos, act_token)
			act_pos = new_pos
		token_id += 1


add_room_with_door((0,0), None)
# start_branch((0,0), 1)

# print room_doors
# print_room_map()

paths = list(exrex.generate(input_line))
print len(paths)
for path in paths:
	print len(path)

print len(paths)



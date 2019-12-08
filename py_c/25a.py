#!/usr/bin/pypy

import sys

input_file='25.txt'
debug = False

if len(sys.argv) > 1 and sys.argv[1]=='-d':
	debug = True

def dprint(*arg):
	if not debug:
		return
	print(arg)

def parse_number_from_string(line, pos):
	rv = ''
	act_pos = pos
	while line[act_pos] in list('0123456789'):
		rv += line[act_pos]
		act_pos += 1
	return rv, act_pos

def manhattan_distance(coords1, coords2):
	return abs(coords1[0]-coords2[0]) + abs(coords1[1]-coords2[1]) + abs(coords1[2]-coords2[2]) + abs(coords1[3]-coords2[3])

all_coords = []

def read_coords():
	global all_coords
	with open(input_file) as f:
		for line in f:
			line = line.strip('\n')
			coords = map(int, line.split(','))
			all_coords.append(coords)

def find_constellations(input_coords):
	constell_id = 1000
	constellations = {}
	for new_coords in input_coords:
		print new_coords
#		print constellations
		member_of = []
		for constell in constellations:
			for coords in constellations[constell]:
				if manhattan_distance(coords, new_coords) <= 3:
						member_of.append(constell)
						if len(member_of) == 1:
							constellations[constell].append(new_coords)
						break
		if len(member_of) == 0:
			constellations[constell_id] = [new_coords]
			constell_id += 1
		elif len(member_of) > 1:
			base_constell_id = member_of[0]
			for c_idx in range(1, len(member_of)):
				constellations[base_constell_id] += constellations.pop(member_of[c_idx])

#	print(constellations)
	return len(constellations)

read_coords()
print find_constellations(all_coords)

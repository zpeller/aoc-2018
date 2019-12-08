#!/usr/bin/python

import copy

input_file='18.txt'
debug = True

wood_map = []
next_wood_map = []
map_hashes = {}
map_hash_ids = {}
map_resource_values = {}

def dprint(*arg):
	if not debug:
		return
	print(arg)

def print_wood_map(l_map):
	for line in l_map:
		print("".join(line))

def adjacent_fields(l_map, coord_x, coord_y):
	global map_height
	global map_width

	fields=[]
	for x in range(coord_x-1, coord_x+2):
		if x<0 or x>=map_width:
			continue
		for y in range(coord_y-1, coord_y+2):
			if y<0 or y>=map_height or (x==coord_x and y==coord_y):
				continue
			fields.append((x, y))
	return fields

def cnt_neighbours(l_map, coord_x, coord_y):
	num_open = 0
	num_wooded = 0
	num_lumber = 0
	for field in adjacent_fields(l_map, coord_x, coord_y):
		x=field[0]
		y=field[1]
		if l_map[y][x] == '.':
			num_open += 1
		elif l_map[y][x] == '|':
			num_wooded += 1
		else:
			num_lumber += 1
	return (num_open, num_wooded, num_lumber)

def cnt_all(l_map):
	num_open = 0
	num_wooded = 0
	num_lumber = 0
	for x in range(0, map_width):
		for y in range(0, map_height):
			if l_map[y][x] == '.':
				num_open += 1
			elif l_map[y][x] == '|':
				num_wooded += 1
			else:
				num_lumber += 1
	return (num_open, num_wooded, num_lumber)


with open(input_file) as f:
	for line in f:
		wood_map.append(list(line.strip('\n')))
map_height = len(wood_map)
map_width = len(wood_map[0])

iter_no = 0
print_wood_map(wood_map)
while iter_no < 1001:
	next_wood_map = copy.deepcopy(wood_map)
	for x in range(0, map_width):
		for y in range(0, map_height):
			n_open, n_wooded, n_lumber = cnt_neighbours(wood_map, x, y)
			if wood_map[y][x] == '.' and n_wooded>=3:
				next_wood_map[y][x] = '|'
			elif wood_map[y][x] == '|' and n_lumber>=3:
				next_wood_map[y][x] = '#'
			elif wood_map[y][x] == '#' and not (n_lumber>=1 and n_wooded>=1):
				next_wood_map[y][x] = '.'
	wood_map = next_wood_map
	iter_no += 1
	print(iter_no)
	print_wood_map(wood_map)
	map_hash = hash(str(wood_map))
	if map_hash in map_hashes.values():
		print("Hash found", map_hash_ids[map_hash], iter_no, map_hash)
		for id in range(map_hash_ids[map_hash], iter_no):
			print("res value: ", id, map_resource_values[map_hashes[id]])
		break
	else:
		map_hashes[iter_no] = map_hash
		map_hash_ids[map_hash] = iter_no
		n_open, n_wooded, n_lumber = cnt_all(wood_map)
		map_resource_values[map_hash] = n_wooded*n_lumber
	

n_open, n_wooded, n_lumber = cnt_all(wood_map)
print("Wooded: ", n_wooded, "lumber: ", n_lumber, "resource: ", n_wooded*n_lumber)



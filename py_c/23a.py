#!/usr/bin/pypy

import sys

input_file='23.txt'
debug = False

min_coords = {'X': 100000000, 'Y': 100000000, 'Z': 100000000}
max_coords = {'X': -100000000, 'Y': -100000000, 'Z': -100000000}

origo = (0,0,0)

nanobots = {}

if len(sys.argv) > 1 and sys.argv[1]=='-d':
	debug = True

def dprint(*arg):
	if not debug:
		return
	print(arg)

# instead of "parse" for pypy
def parse_number_from_string(line, pos):
	rv = ''
	act_pos = pos
	while act_pos<len(line):
		if line[act_pos] not in '+-0123456789':
			break
		rv += line[act_pos]
		act_pos += 1
	return int(rv), act_pos

def manhattan_distance(coords1, coords2):
	return abs(coords1[0]-coords2[0]) + abs(coords1[1]-coords2[1]) + abs(coords1[2]-coords2[2])

def add_min_max(ctype, value):
	if (min_coords[ctype] > value):
		min_coords[ctype] = value
	if (max_coords[ctype] < value):
		max_coords[ctype] = value

def read_nanobots():
	max_signal_radius = 0
	strongest_bot = (-1, -1, -1)
	with open(input_file) as f:
		for line in f:
			line = line.strip('\n')
			pos = 5
			x, pos = parse_number_from_string(line, pos)
			add_min_max('X', x)
			pos += 1
			y, pos = parse_number_from_string(line, pos)
			add_min_max('Y', y)
			pos += 1
			z, pos = parse_number_from_string(line, pos)
			add_min_max('Z', z)
			pos += 5
			signal_radius, pos = parse_number_from_string(line, pos)
			if signal_radius > max_signal_radius:
				max_signal_radius = signal_radius
				strongest_bot = (x, y, z)
			nanobots[x,y,z] = signal_radius
	dprint(strongest_bot, max_signal_radius)
	return strongest_bot, max_signal_radius

def find_bots_in_signal_range(center_coords, signal_radius):
	bot_list = []
	for bot in nanobots:
		if manhattan_distance(bot, center_coords) <= signal_radius:
			bot_list.append(bot)
	return len(bot_list)

def find_bots_in_coord_range(center_coords):
	bot_list = []
	for bot in nanobots:
		if manhattan_distance(bot, center_coords) <= nanobots[bot]:
			bot_list.append(bot)
	return len(bot_list)

def scan_bots_in_range(pos1, pos2, steps):
	min_manhattan = 1000000000000000
	min_manhattan_coords = (0,0,0)
#	max_bots = 912
	max_bots = 0
	stepx=max(1, (pos2[0]-pos1[0])/steps)
	for x in range(pos1[0], pos2[0]+stepx+1, stepx):
		stepy=max(1, (pos2[1]-pos1[1])/steps)
		for y in range(pos1[1], pos2[1]+stepy+1, stepy):
			stepz=max(1, (pos2[2]-pos1[2])/steps)
			for z in range(pos1[2], pos2[2]+stepz+1, stepz):
				target_coords = (x,y,z)
				num_inrange_bots = find_bots_in_coord_range(target_coords)
#				print('Number of nanobots in range of target coords: ' +str(target_coords) + ': ' + str(num_inrange_bots))
				if num_inrange_bots>=max_bots:
					if num_inrange_bots>max_bots:
						print(str(target_coords) + ': ' + str(num_inrange_bots))
						max_bots = num_inrange_bots
						min_manhattan = 1000000000000000
					if manhattan_distance(origo, target_coords) < min_manhattan:
						min_manhattan = manhattan_distance(origo, target_coords)
						print(target_coords, min_manhattan)
						min_manhattan_coords = target_coords
					max_coords = (x, y , z)
					add_min_max('X', x)
					add_min_max('Y', y)
					add_min_max('Z', z)
	return min_manhattan_coords

center_bot, strongest_signal = read_nanobots()
dprint(nanobots)
print(min_coords, max_coords, (max_coords['X']-min_coords['X'])/1000/1000, (max_coords['Y']-min_coords['Y'])/1000/1000, (max_coords['Z']-min_coords['Z'])/1000/1000 )

num_inrange_bots = find_bots_in_signal_range(center_bot, strongest_signal)
print('Number of nanobots in range: '+ str(center_bot)+ ': ' + str(num_inrange_bots) +' sig_radius: ' + str(strongest_signal/1000000))

num_inrange_bots = find_bots_in_coord_range((0,0,0))
target_coords = (0,0,0)
print('Number of nanobots in range of target coords: ' +str(target_coords) + ': ' + str(num_inrange_bots))

#c1 = (min_coords['X'], min_coords['Y'], min_coords['Z'])
#c2 = (max_coords['X'], max_coords['Y'], max_coords['Z'])
#scan_bots_in_range( c1, c2, 100)
#print("")
#diff = 4000000
#c1 = (14626668-diff, 46033048-diff, 27514612-diff)
#c2 = (14626668+diff, 46033048+diff, 27514612+diff)
#scan_bots_in_range( c1, c2, 100)

min_coords = {'X': 100000000, 'Y': 100000000, 'Z': 100000000}
max_coords = {'X': -100000000, 'Y': -100000000, 'Z': -100000000}

#print("")
#diff = 1000000
#c1 = (15106668-diff, 45393048-diff, 27914612-diff)
#c2 = (c1[0]+2*diff, c1[1]+2*diff, c1[2]+2*diff)
#scan_bots_in_range( c1, c2, 200)
#
#print(min_coords, max_coords, (max_coords['X']-min_coords['X'])/1000/1000, (max_coords['Y']-min_coords['Y'])/1000/1000, (max_coords['Z']-min_coords['Z'])/1000/1000 )

#print("")
#diff = 50
#c0 = (13972634, 45661224, 28290272)
#c1 = (c0[0]-diff, c0[1]-diff, c0[2]-diff)
#c2 = (c0[0]+diff, c0[1]+diff, c0[2]+diff)
#scan_bots_in_range( c1, c2, 200)
#
#print(min_coords, max_coords, (max_coords['X']-min_coords['X']), (max_coords['Y']-min_coords['Y']), (max_coords['Z']-min_coords['Z']) )

def scan_and_lock(start_pos, start_diff):
	c0 = start_pos
	diff = start_diff
	step = 50
	while diff>10:
		c1 = (c0[0]-diff, c0[1]-diff, c0[2]-diff)
		c2 = (c0[0]+diff, c0[1]+diff, c0[2]+diff)
		new_c0 = scan_bots_in_range( c1, c2, step)
		if new_c0 != c0:
			if abs(new_c0[0]-c0[0])>diff/100 or abs(new_c0[1]-c0[1])>diff/100 or abs(new_c0[1]-c0[1])>diff/100:
				print('Reposition: ', new_c0)
				c0 = new_c0
				continue
		diff = diff/2
		print('New diff:', c0, diff)

def get_cube_vertice_coords(center_coords, cube_size, add_center=False):
	cube_vertices = []
	for x in center_coords[0]-cube_size/2, center_coords[0]+cube_size/2:
		for y in center_coords[1]-cube_size/2, center_coords[1]+cube_size/2:
			for z in center_coords[2]-cube_size/2, center_coords[2]+cube_size/2:
				cube_vertices.append((x,y,z))
	if add_center:
		cube_vertices.append(center_coords)
	return cube_vertices


def find_bots_on_cube_vertices_in_range(center_coords, cube_size):
	bot_list = []
	for bot in nanobots:
		for vertice_coords in get_cube_vertice_coords(center_coords, cube_size, True):
			if manhattan_distance(bot, vertice_coords) <= nanobots[bot]:
				if bot not in bot_list:
					bot_list.append(bot)
		if bot[0]>center_coords[0]-cube_size/2 and bot[0]<center_coords[0]+cube_size/2 and \
			bot[1]>center_coords[1]-cube_size/2 and bot[1]<center_coords[1]+cube_size/2 and \
			bot[2]>center_coords[2]-cube_size/2 and bot[2]<center_coords[2]+cube_size/2:
				if bot not in bot_list:
					bot_list.append(bot)
#		print(vertice_coords, len(bot_list))
	return len(bot_list)

def get_strongest_cube(center_pos, cube_size):
	max_bots = 0
	max_cube = (0, 0, 0)
	for cube_center in get_cube_vertice_coords(center_pos, cube_size):
		num_inrange_bots = find_bots_on_cube_vertices_in_range(cube_center, cube_size)
		print('cpower:', cube_center, num_inrange_bots)
		if num_inrange_bots > max_bots:
			max_bots = num_inrange_bots
			max_cube = cube_center
	return max_cube

def split_and_calc(start_pos, start_cube_size):
	cube_center = start_pos
	cube_size = start_cube_size
	while cube_size>10:
		cube_center = get_strongest_cube(cube_center, cube_size)
		print(cube_center, cube_size)
		print("")
		cube_size = cube_size*3/4

	cube_size = 20
	c1 = (cube_center[0]-cube_size, cube_center[1]-cube_size, cube_center[2]-cube_size)
	c2 = (cube_center[0]+cube_size, cube_center[1]+cube_size, cube_center[2]+cube_size)
	scan_bots_in_range(c1, c2, 50)

print("")
#scan_and_lock(origo, 33000000)
#scan_and_lock((15970000, 44600000, 29300000), 10000)
#scan_and_lock((15971003, 44656553, 29284970), 17000)

split_and_calc(origo, 500000000)
#split_and_calc((50000000, 50000000, 50000000), 200000000)

#print(min_coords, max_coords, (max_coords['X']-min_coords['X']), (max_coords['Y']-min_coords['Y']), (max_coords['Z']-min_coords['Z']) )


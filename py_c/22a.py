#!/usr/bin/pypy

import sys

debug = False

cave_depth = 5355
cave_target = (14, 796)
cave_extension = 1000

#cave_depth = 510
#cave_target = (10, 10)
#cave_extension = 250

cave_modulo = 20183
cave_y0_multiplier = 16807
cave_x0_multiplier = 48271

tool_change_cost = 7
move_cost = 1

cave_erosion_char = ('.', '=', '|')

geo_indexes = {}
erosion_levels = {}
risk_levels = {}
cave_map = []

distance_map = {}
distance_map['N'] = {}		# neither
distance_map['T'] = {}		# torch
distance_map['C'] = {}		# climbing gear
distance_list = { 0: [(0, 0)] }

tool_types = { '.': ('T', 'C'), '=': ('C', 'N'), '|': ('N', 'T') }

if len(sys.argv) > 1 and sys.argv[1]=='-d':
	debug = True

def dprint(*arg):
	if not debug:
		return
	print(arg)

def get_erosion_level_w_type(geo_index):
	erosion_level = (geo_index + cave_depth) % cave_modulo
	erosion_type = erosion_level % 3
	return erosion_level, erosion_type, cave_erosion_char[erosion_type]

def get_geo_index(c_x, c_y):
	if c_x == 0 and c_y == 0:
		return 0
	if c_x == cave_target[0] and c_y == cave_target[1]:
		return 0
	if c_y == 0:
		return c_x * cave_y0_multiplier
	if c_x == 0:
		return c_y * cave_x0_multiplier
	return erosion_levels[c_x-1, c_y] * erosion_levels[c_x, c_y-1]

def fill_cave_info():
	for y in range(0, cave_target[1]+cave_extension):
		cave_line = []
		for x in range(0, cave_target[0]+cave_extension):
			geo_indexes[x, y] = get_geo_index(x, y)
			erosion_levels[x, y], risk_levels[x, y], erosion_char = get_erosion_level_w_type(geo_indexes[x, y])
			cave_line.append(erosion_char)
		cave_map.append(cave_line)
#	cave_map[0][0]='M'
#	cave_map[cave_target[1]][cave_target[0]]='T'

def print_cave_map():
	for lineno in range(0, len(cave_map)):
		print("".join(cave_map[lineno]))

def print_distance_and_torch_map_w_region(is_torch, min_coords, max_coords):
	line = '      '
	for x in range(min_coords[0], max_coords[0]):
		line += '%-4d   '%x
	print line
	for y in range(min_coords[1], max_coords[1]):
		line = '%4d  '%y
		for x in range(min_coords[0], max_coords[0]):
			if not is_torch:
				min_dist, min_type = get_field_min_dist_value_with_type( (x, y) )
			else:
				if (x,y) in distance_map['T']:
					min_dist = distance_map['T'][x, y]
					min_type = 'T'
				else:
					min_dist = None
			if min_dist:
				line += cave_map[y][x] + min_type + '%-4d '%min_dist
			else:
				line += cave_map[y][x] + '     '
		print(line)

def print_distance_and_torch_map(is_torch):
	print_distance_and_torch_map_w_region(is_torch, (0,0), (len(cave_map[0]), len(cave_map)))

def print_distance_map():
	print_distance_and_torch_map(False)

def print_torch_map():
	print_distance_and_torch_map(True)

def get_risk_level(coord1, coord2):
	risk_level = 0
	for x in range(coord1[0], coord2[0]+1):
		for y in range(coord1[1], coord2[1]+1):
			risk_level += risk_levels[x, y]
	return risk_level

def adjacent_field_coords_list( (x, y) ):
	field_coords = [(x+1, y), (x, y+1)]
	if x>0:
		field_coords.append((x-1, y))
	if y>0:
		field_coords.append((x, y-1))
	return field_coords

def get_field_min_dist_value_with_type(coords):
	min_dist = 1000000000
	min_dist_type = ''
	if coords not in distance_map['N']:
		return None, None
	for dist_type in ('N', 'T', 'C'):
		if distance_map[dist_type][coords] >=0 and distance_map[dist_type][coords] < min_dist:
			min_dist = distance_map[dist_type][coords]
			min_dist_type = dist_type
	return min_dist, min_dist_type

def get_field_min_dist_value(coords):
	min_dist, field_type =  get_field_min_dist_value_with_type(coords)
	return min_dist

def get_fields_for_level(level):
	field_list = []
	for coords in distance_map['N']:
		if distance_map['N'][coords] == level or distance_map['T'][coords] == level or distance_map['C'][coords] == level:
			field_list.append(coords)
	return field_list

def add_to_distance_map(coords, values):
	if coords not in distance_map['N']:
		for dist_type in ('N', 'T', 'C'):
			distance_map[dist_type][coords] = values[dist_type]
	else:
		for dist_type in ('N', 'T', 'C'):
			if values[dist_type] == -1:	# XXX dest type validation should happen before call! (no check for dst -1 )
				continue
			if distance_map[dist_type][coords] > values[dist_type]:
				distance_map[dist_type][coords] = values[dist_type]		# XXX adjust other value with toolchange?

def calc_field_distances(src_coords, dst_coords):	# adjacent fields
	distances = {'T':-1, 'C':-1, 'N':-1}

	src_type = cave_map[src_coords[1]][src_coords[0]]
	dst_type = cave_map[dst_coords[1]][dst_coords[0]]

	src_tool_types = tool_types[src_type]
	dst_tool_types = tool_types[dst_type]

	local_tool_change_target = None
	for dist_type in ('N', 'T', 'C'):
		if dist_type not in dst_tool_types:
			continue
		if src_type == dst_type:
			distances[dist_type] = distance_map[dist_type][src_coords] + move_cost
			continue
		if dist_type in src_tool_types:
			distances[dist_type] = distance_map[dist_type][src_coords] + move_cost
		else:
			local_tool_change_target = dist_type

	if local_tool_change_target:
		distances[local_tool_change_target] = max(distances.values()) + tool_change_cost

	return distances


def process_fields_near_level(level):
	for level_field in get_fields_for_level(level):
		for field in adjacent_field_coords_list(level_field):
			new_distances = calc_field_distances(level_field, field)
#			print level_field, field, new_distances
			add_to_distance_map(field, new_distances)

def check_field_value_sanity():
	for field in distance_map['N']:
		mv = sorted((distance_map['N'][field], distance_map['T'][field], distance_map['C'][field]))
		if mv[1]<0:
			print("Double -1!", field)
			sys.exit(1)
		if mv[2]-mv[1]>tool_change_cost:
			print('Dist value anomaly (N, T, C):', field, distance_map['N'][field], distance_map['T'][field], distance_map['C'][field])
			sys.exit(1)
	print("Check field sanity test passed!")

def check_neighbour_value_sanity():
	for field in distance_map['N']:
		field_min_value = get_field_min_dist_value(field)
		for neighb_field in adjacent_field_coords_list(field):
			if neighb_field not in distance_map['N']:
				continue
			neigh_max_value = max((distance_map['N'][neighb_field], distance_map['T'][neighb_field], distance_map['C'][neighb_field]))
			if abs(field_min_value-neigh_max_value) > 2*tool_change_cost + move_cost:
				print('Neighbour value anomaly (N, T, C):', field, neighb_field, distance_map['N'][field], distance_map['T'][field], distance_map['C'][field], distance_map['N'][neighb_field], distance_map['T'][neighb_field], distance_map['C'][neighb_field])
				sys.exit(1)

	print("Check neighbour value sanity test passed!")

fill_cave_info()
# print_cave_map()
print("")
print("risk level: ", get_risk_level((0,0), cave_target))
print("")

add_to_distance_map((0,0), {'T':0, 'C':7, 'N':-1})

proc_level = 0
while True:
	if proc_level % 10 == 0:
		print('proc_level:', proc_level, 'torch map size:', len(distance_map['T']))
	process_fields_near_level(proc_level)
	proc_level += 1
	if cave_target not in distance_map['T']:
		continue
	if distance_map['T'][cave_target]+tool_change_cost+50 < proc_level:
		break

check_field_value_sanity()
check_neighbour_value_sanity()

print("")
#print_torch_map()
print_distance_and_torch_map_w_region(False, (0,780), (30, 820))
print("")
#print_distance_and_torch_map_w_region(True, (0,780), (30, 820))
#print_distance_and_torch_map_w_region(False, (0,0), (25, 25))
#print("")
#print_distance_and_torch_map_w_region(True, (0,0), (25, 25))
print('Max proc level:', proc_level)
print('Dst level:', cave_target, distance_map['T'][cave_target])
# 1110 too high!

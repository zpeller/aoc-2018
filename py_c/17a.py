#!/usr/bin/python

from parse import parse
import sys

input_file='17.txt'
debug = False

#min_x = 480 	# 420
#max_x = 520		# 690
#min_y = 0		
#max_y = 16		# 2000

min_x = 10000 	# 420
max_x = 0		# 690
min_y = 10000		
max_y = 0		# 2000

fountain = (500, 1)

water_source_list = [fountain]

sand_map = {}
water_flow = {}

def dprint(*arg):
	if not debug:
		return
	print(arg)

def print_sand_map():
	global sand_map
	for y in range(min_y, max_y+1):
		line=''
		for x in range(min_x, max_x+1):
			if (x,y) in water_flow:
			 	line += '|'
			elif (x,y) in sand_map:
				line += sand_map[x,y]
			else:
			 	line += '.'
		print(line)
	print("")

def add_wall(line):
	global sand_map
	global max_x
	global max_y
	global min_x
	global min_y
	params = parse('{}={}, {}={}..{}', line)
	var1=params[0]
	if var1 == 'x':
		x_from=int(params[1])
		x_to=int(params[1])
		y_from=int(params[3])
		y_to=int(params[4])
	else:
		y_from=int(params[1])
		y_to=int(params[1])
		x_from=int(params[3])
		x_to=int(params[4])
	for x in range(x_from, x_to+1):
		for y in range(y_from, y_to+1):
			sand_map[x,y] = '#'
	if min_x > x_from-2:
		min_x = x_from-2
	if max_x < x_to+2:
		max_x = x_to+2
	if min_y > y_from:
		min_y = y_from
	if max_y < y_to+1:
		max_y = y_to+1

def add_spring_to_map(spring):
	global sand_map
	sand_map[spring[0],spring[1]] = '+'
	
def add_water_flow(water_y, water_min_x, water_max_x):
	global water_flow
	for x in range(water_min_x, water_max_x+1):
		if (x, water_y) not in water_flow:
			water_flow[x, water_y]='|'

def add_still_water(water_y, water_min_x, water_max_x):
	global sand_map
	global water_flow
	for x in range(water_min_x, water_max_x+1):
		sand_map[x, water_y]='~'
		if (x, water_y) in water_flow:
			del water_flow[x, water_y]

def is_free_space_below(x, y):
	global sand_map
	return not ((x,y+1) in sand_map)

def is_steady_surface_below(x, y):
	global sand_map
	return (x,y+1) in sand_map and (sand_map[x,y+1] == '#' or sand_map[x,y+1] == '~')

def is_wall(x, y):
	global sand_map
	return (x,y) in sand_map and sand_map[x,y] == '#'

def find_flatbed(water_x, water_y):
	global min_x
	global max_x
	if not is_steady_surface_below(water_x, water_y):
		return None
	x = water_x-1
	while x>min_x:
	 	if is_wall(x, water_y):
			left_wall_x = x
			break
		if not is_steady_surface_below(x, water_y):
			return None
		x -= 1
	if x<=min_x:
		return None
	x = water_x+1
	while x<max_x:
	 	if is_wall(x, water_y):
			right_wall_x = x
			break
		if not is_steady_surface_below(x, water_y):
			return None
		x += 1
	if x>=max_x:
		return None
	return (left_wall_x, right_wall_x)

def find_flow_borders(water_x, water_y):
	global min_x
	global max_x

	if not is_steady_surface_below(water_x, water_y):
		return (False, water_x, water_x)

	is_steady = True

	x = water_x-1
	while x>min_x:
	 	if is_wall(x, water_y):
			left_wall_x = x
			break
		if not is_steady_surface_below(x, water_y):
			left_wall_x = x-1
			is_steady = False
			break
		x -= 1

	if x<=min_x:
		print("Water flows out to the left!!!!", water_x, water_y, x)
		sys.exit(1)

	x = water_x+1
	while x<max_x:
	 	if is_wall(x, water_y):
			right_wall_x = x
			break
		if not is_steady_surface_below(x, water_y):
			right_wall_x = x+1
			is_steady = False
			break
		x += 1
	if x>=max_x:
		print("Water flows out to the left!!!!", water_x, water_y, x)
		sys.exit(1)
	return (is_steady, left_wall_x+1, right_wall_x-1)

with open(input_file) as f:
	for line in f:
		line = line.strip('\n')
		add_wall(line)
	add_spring_to_map(water_source_list[0])

def add_water_source(source_coords):
	global water_source_list
	if source_coords not in water_source_list:
		water_source_list.append(source_coords)

def drop_water(water):
	global water_flow
	global water_source_list
	print("Dropping water from:", water)

	w_x=water[0]
	w_y=water[1]+1

	while w_y < max_y:
		if is_free_space_below(w_x,w_y):
			add_water_flow(w_y, w_x, w_x)
			w_y += 1
			continue

		is_steady, surface_left_x, surface_right_x = find_flow_borders(w_x, w_y)
		dprint(w_y, surface_left_x, surface_right_x, is_steady)
		if is_steady:
			add_still_water(w_y, surface_left_x, surface_right_x)
			if debug:
				print_sand_map()
			if w_y == water[1]+1:
				add_water_source(fountain)
				break
			else:
				w_y=water[1]+1
				continue
		else:
			print("--------------------- addwf")
			add_water_flow(w_y, surface_left_x, surface_right_x)
			if debug:
				print_sand_map()
			if is_free_space_below(surface_left_x, w_y):
				add_water_source((surface_left_x, w_y-1))
				print("add source: ", surface_left_x, w_y)
			if is_free_space_below(surface_right_x, w_y):
				add_water_source((surface_right_x, w_y-1))
				print("add source: ", surface_right_x, w_y)
			break
		break

def count_water():
	global sand_map
	global water_flow
	
	steady_water_count = 0
	for y in range(min_y, max_y+1):
		for x in range(min_x, max_x+1):
#			if (x,y) in water_flow:
#			 	water_count += 1
			if (x,y) in sand_map and sand_map[x,y]=='~':
			 	steady_water_count += 1
	return steady_water_count, len(water_flow), steady_water_count+len(water_flow)


print_sand_map()
print("")

while len(water_source_list) > 0:
	print("------------------------------------------------------------------")
	print("Water source list:", water_source_list)
	drop_water(water_source_list[0])
	del water_source_list[0]
#	print_sand_map()

dprint(min_x, max_x, min_y, max_y)

print_sand_map()
water = count_water()
print("Steady: ", water[0], "flowing: ", water[1], "total: ", water[2])


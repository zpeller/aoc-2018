#!/usr/bin/python

import copy

tracks_map = []
carts = []
cart_positions = []

def print_track_map():
	global tracks_map
	global carts
	print_map = copy.deepcopy(tracks_map)
	for cart in carts:
		x = cart[0]
		y = cart[1]
		dx = cart[2]
		dy = cart[3]
		if dx == 0:
			print_map[y][x] = 'v' if dy==1 else '^'
		else:
			print_map[y][x] = '>' if dx==1 else '<'

	for track_line in print_map:
		print("".join(track_line))

def cart_move(cart_coords):
	global tracks_map
	coord_x = cart_coords[0]
	coord_y = cart_coords[1]
	dx = cart_coords[2]
	dy = cart_coords[3]
	plus_dir = cart_coords[4]

	next_x = coord_x + dx
	next_y = coord_y + dy
	if ( tracks_map[next_y][next_x] == '/' or 
			( tracks_map[next_y][next_x] == '+' and 
		  		( (plus_dir == 'right' and dx == 0) or
		  		  (plus_dir == 'left' and dy == 0) ) ) ):
		if dy != 0:
			next_dx = -dy
			next_dy = 0
		else:
			next_dx = 0
			next_dy = -dx
	elif ( tracks_map[next_y][next_x] == '\\' or
			( tracks_map[next_y][next_x] == '+' and 
		  		( (plus_dir == 'left' and dx == 0) or
		  		  (plus_dir == 'right' and dy == 0) ) ) ):
		if dy != 0:
			next_dx = dy
			next_dy = 0
		else:
			next_dx = 0
			next_dy = dx
	else:
		next_dx = dx
		next_dy = dy

	if tracks_map[next_y][next_x] == '+':
		if plus_dir == 'left':
			next_dir = 'straight'
		elif plus_dir == 'straight':
			next_dir = 'right'
		else:
			next_dir = 'left'
	else:
		next_dir = plus_dir

	return (next_x, next_y, next_dx, next_dy, next_dir)


with open('13.txt') as f:
	y = 0
	for track_line in f:
		track_line = list(track_line.strip('\n'))
		x = 0
		for c in track_line:
			if c in ('v', '^'):
				track_line[x] = '|'
				carts.append((x, y, 0, 1 if c=='v' else -1, 'left'))
				cart_positions.append((x, y))
			elif c in ('<', '>'):
				track_line[x] = '-'
				carts.append((x, y, 1 if c=='>' else -1, 0, 'left'))
				cart_positions.append((x, y))
			x += 1
		tracks_map.append(track_line)
		y += 1

print_track_map()
print(carts)
print('CP1:', cart_positions)

def sortKey(coord):
	return ((coord[1], coord[0]))

print("")
iter_no = 1
collided = False
while not collided:
	carts = sorted(carts, key=sortKey)
	for cart_id in range(0, len(carts)):
		cart = carts[cart_id]
		x, y, dx, dy, ndir = cart_move(cart)
		if ((x,y) in cart_positions):
			print("Collision at ", x, y)
			collided = True
			break
		carts[cart_id] = (x, y, dx, dy, ndir)
		cart_positions.remove((cart[0],cart[1]))
		cart_positions.append((x, y))
#		print_track_map()
	print('End iter ', iter_no)
	iter_no += 1



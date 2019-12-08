#!/usr/bin/python

from parse import parse

def nextpos(light):
	x, y, dx, dy = light
	return x+dx, y+dy, dx, dy

def prevpos(light):
	x, y, dx, dy = light
	return x-dx, y-dy, dx, dy

def light_area():
	global lights
	ziplights = zip(*lights)
	return (max(ziplights[0])-min(ziplights[0])) * (max(ziplights[1])-min(ziplights[1]))

def to_coords(light):
	return light[0]-110, light[1]-129

lights = []

with open('10.txt') as f:
	for line in f:
		lights.append(map(int, parse('{} => {}', line.strip())))

maxiter=30000
iter_no = 0
min_area = light_area()

while True:
	lights = map(nextpos, lights)
	l_area = light_area()
	if l_area>min_area:
		break
	min_area = l_area
#	print(iter_no, min_area, l_area)
	iter_no += 1

lights = map(prevpos, lights)
ziplights = zip(*lights)
coords = map(to_coords, lights)
# print(tuple(lights))
print("iters: ", iter_no)

screen = (
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................'),
	list('................................................................................................')
)

for (cx, cy) in coords:
	screen[cy][cx]='#'

for s in screen:
	print("".join(s))


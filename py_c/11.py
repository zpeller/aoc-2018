#!/usr/bin/python

def calc_power(x, y, grid_sn):
	rack_id = x+10
	power = rack_id * y
	power += grid_sn
	power *= rack_id
	power  = (power%1000) /100
	power -= 5
	return power

#print(calc_power(3, 5, 8))
#print(calc_power(122, 79, 57))
#print(calc_power(217, 196, 39))
#print(calc_power(101, 153, 71))

def calc_power_nxn(cells, coord_x, coord_y, grid_size):
	sum_power = 0
	for x in range(coord_x, coord_x+grid_size):
		sum_power += sum(cells[x][coord_y:(coord_y+grid_size)])
	return sum_power

maxx = 300
maxy = 300

grid_serial_no = 5535
# grid_serial_no = 18

cells= [ [ 0 for i in range(0,maxx+1) ] for j in range(0,maxy+1) ]
max_power = -10000
max_coords = (0, 0)

for x in range(1, maxx+1):
	for y in range(1, maxy+1):
		cells[x][y] = calc_power(x, y, grid_serial_no)
#		if ((x>=32) and (x<=38)) and ((y>=44) and (y<=48)):
#			print(cells[x, y])
		if (x>=3) and (y>=3):
			power = calc_power_nxn(cells, x-2, y-2, 3)
			if power>max_power:
				max_power = power
				max_coords = (x-2, y-2)

print(max_coords, max_power)

max_power = -10000
max_coords = (0, 0, 0)
for x in range(1, maxx+1):
	print(x)
	for y in range(1, maxy+1):
		max_grid_size = min( (maxx+1-x), (maxy+1-y) )
		for grid_size in range(1, max_grid_size+1):
			power = calc_power_nxn(cells, x, y, grid_size)
			if power>max_power:
				max_power = power
				max_coords = (x, y, grid_size)

print(max_coords, max_power)


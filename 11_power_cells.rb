#!/usr/local/bin/ruby

require 'pp'

input = (ARGV.empty? ? DATA : ARGF).each_line.map(&:to_i)[0].freeze

def calc_power(x, y, grid_sn)
    rack_id = x+10
    power = rack_id * y
    power += grid_sn
    power *= rack_id
    power  = (power%1000) /100
    power -= 5
    return power
end

def calc_power_nxn(cells, c_x, c_y, cell_grid_size)
	(c_y..c_y+cell_grid_size-1).map { |y| cells[y][c_x, cell_grid_size].sum }.sum
end

def find_max_nxn(cells, cell_grid_size)
	maxpower = [0, 0, 0]
	(1..FUEL_GRID_SIZE-cell_grid_size+1).each { |y|
		(1..FUEL_GRID_SIZE-cell_grid_size+1).each { |x|
			power = calc_power_nxn(cells, x, y, cell_grid_size)
			maxpower = [maxpower, [power, x, y]].max
		}
	}
	return maxpower
end

def find_max_3x3(cells)
	return find_max_nxn(cells, 3)
end

def find_max_gridsize(cells)
	maxnpower = [0, 0, 0, 0]
	(1..FUEL_GRID_SIZE).each { |n|
		maxpower = find_max_nxn(cells, n)
		maxnpower = [maxnpower, maxpower + [n]].max
		pp [n, maxnpower]
	}
	return maxnpower
end

FUEL_GRID_SIZE = 300

cells = Array.new(FUEL_GRID_SIZE+1) { |y| Array.new(FUEL_GRID_SIZE+1) { |x| calc_power(x,y,input)} }

pp find_max_3x3(cells)
pp find_max_gridsize(cells)
	

__END__
5535

#!/usr/local/bin/ruby

require 'pp'

input = (ARGV.empty? ? DATA : ARGF).each_line.map { |l|
	l.scan(/-?\d+/).map(&:to_i)
}.freeze

# pp input

class Light
	attr_reader :x
	attr_reader :y

	def initialize(x, y, vx, vy)
		@x, @y, @vx, @vy = x, y, vx, vy
	end

	def step(n=1)
		@x += n*@vx
		@y += n*@vy
	end

	def inspect
		"<#{self.object_id} #{@x},#{@y}>"
	end
end

def init_lights(lights, lights_list)
	lights_list.each { |x, y, vx, vy|
		lights << Light.new(x, y, vx, vy)
	}
end

def get_area(lights)
	min_x = lights.min_by{|l| l.x}.x
	max_x = lights.max_by{|l| l.x}.x
	min_y = lights.min_by{|l| l.y}.y
	max_y = lights.max_by{|l| l.y}.y
	return (max_x-min_x)*(max_y-min_y), min_x, min_y, max_x-min_x+1, max_y-min_y+1
end

def find_smallest_area(lights)
	area, = get_area(lights)
	prev_area = area + 1

	secs = 0
	while area < prev_area
		prev_area = area
		lights.each { |l| l.step }
		area, = get_area(lights)
		secs += 1
	end
	lights.each { |l| l.step(-1) }
	return secs - 1
end

def print_lights(lights)
	_, min_x, min_y, w, h = get_area(lights)
	light_map = Array.new(h) { ['.'] * (w) }
	lights.each { |l|
		light_map[l.y-min_y][l.x-min_x] = '#'
	}
	light_map.each { |l| print l.join, "\n" }
end

lights = []
init_lights(lights, input)

t = find_smallest_area(lights)
print_lights(lights)
pp t




__END__
position=< 52672,  52690> velocity=<-5, -5>
position=<-20892,  10646> velocity=< 2, -1>
position=<-10378, -52423> velocity=< 1,  5>
position=< 21199, -20892> velocity=<-2,  2>
position=< 21187,  42176> velocity=<-2, -4>
position=<-31392,  10644> velocity=< 3, -1>
position=< 21152,  31665> velocity=<-2, -3>
position=<-20880, -41905> velocity=< 2,  4>
position=< 21200, -10373> velocity=<-2,  1>
position=< 31652,  42178> velocity=<-3, -4>
position=<-20873,  31671> velocity=< 2, -3>
position=< 52717,  42181> velocity=<-5, -4>
position=<-10350,  10650> velocity=< 1, -1>
position=< 31691, -10372> velocity=<-3,  1>
position=<-52390,  21157> velocity=< 5, -2>
position=<-10354,  52690> velocity=< 1, -5>
position=< 52696, -41906> velocity=<-5,  4>
position=<-10354,  42182> velocity=< 1, -4>
position=<-20879, -20883> velocity=< 2,  2>
position=<-52382,  52688> velocity=< 5, -5>
position=<-41906, -20891> velocity=< 4,  2>
position=<-10394, -31401> velocity=< 1,  3>
position=<-20873,  31670> velocity=< 2, -3>
position=< 52700,  31663> velocity=<-5, -3>
position=<-52414, -20888> velocity=< 5,  2>
position=<-52438,  42182> velocity=< 5, -4>
position=< 42205,  10641> velocity=<-4, -1>
position=< 42169,  10646> velocity=<-4, -1>
position=<-52406,  10647> velocity=< 5, -1>
position=< 42178,  52689> velocity=<-4, -5>
position=< 52725, -31399> velocity=<-5,  3>
position=<-31372, -41905> velocity=< 3,  4>
position=< 10657,  31670> velocity=<-1, -3>
position=<-31363, -20890> velocity=< 3,  2>
position=<-10352,  52689> velocity=< 1, -5>
position=<-41884,  42178> velocity=< 4, -4>
position=< 52720, -20883> velocity=<-5,  2>
position=< 21143, -31399> velocity=<-2,  3>
position=<-31381,  52685> velocity=< 3, -5>
position=<-20863, -52425> velocity=< 2,  5>
position=<-20885,  21158> velocity=< 2, -2>
position=<-31376,  52687> velocity=< 3, -5>
position=<-20873, -31399> velocity=< 2,  3>
position=< 21155,  10648> velocity=<-2, -1>
position=< 42214,  52690> velocity=<-4, -5>
position=< 10636, -41906> velocity=<-1,  4>
position=<-10365, -52416> velocity=< 1,  5>
position=< 42161,  21154> velocity=<-4, -2>
position=< 10644, -10380> velocity=<-1,  1>
position=<-41867,  10641> velocity=< 4, -1>
position=<-31390,  10650> velocity=< 3, -1>
position=< 31698, -20884> velocity=<-3,  2>
position=< 52709, -31402> velocity=<-5,  3>
position=< 10630, -52425> velocity=<-1,  5>
position=< 42186,  31663> velocity=<-4, -3>
position=<-41887, -31399> velocity=< 4,  3>
position=< 42217, -52425> velocity=<-4,  5>
position=<-52386, -52421> velocity=< 5,  5>
position=<-20892,  42182> velocity=< 2, -4>
position=< 10657, -10376> velocity=<-1,  1>
position=<-20892, -41908> velocity=< 2,  4>
position=< 21168,  42175> velocity=<-2, -4>
position=<-31403, -20883> velocity=< 3,  2>
position=< 31695,  10649> velocity=<-3, -1>
position=< 31687,  31664> velocity=<-3, -3>
position=<-41914, -10380> velocity=< 4,  1>
position=<-10351, -20883> velocity=< 1,  2>
position=< 10678,  31667> velocity=<-1, -3>
position=< 52701, -31395> velocity=<-5,  3>
position=< 31686, -41914> velocity=<-3,  4>
position=<-52398, -31399> velocity=< 5,  3>
position=<-41887,  10642> velocity=< 4, -1>
position=< 42209, -52419> velocity=<-4,  5>
position=<-52422,  52693> velocity=< 5, -5>
position=<-20881,  52690> velocity=< 2, -5>
position=< 31671, -31400> velocity=<-3,  3>
position=<-41924, -41910> velocity=< 4,  4>
position=<-20852,  52689> velocity=< 2, -5>
position=< 42201, -52422> velocity=<-4,  5>
position=< 31691,  21161> velocity=<-3, -2>
position=<-41870, -31399> velocity=< 4,  3>
position=<-20889, -52423> velocity=< 2,  5>
position=< 42169,  21153> velocity=<-4, -2>
position=< 52672, -52420> velocity=<-5,  5>
position=< 52691, -10381> velocity=<-5,  1>
position=<-41882,  52690> velocity=< 4, -5>
position=<-31403,  10649> velocity=< 3, -1>
position=<-41871, -20885> velocity=< 4,  2>
position=<-52393,  21158> velocity=< 5, -2>
position=<-41867,  31667> velocity=< 4, -3>
position=< 31686, -52421> velocity=<-3,  5>
position=<-52385, -20887> velocity=< 5,  2>
position=<-31412, -52425> velocity=< 3,  5>
position=<-31395,  10643> velocity=< 3, -1>
position=< 52706,  52685> velocity=<-5, -5>
position=< 31670,  10645> velocity=<-3, -1>
position=<-10374, -31397> velocity=< 1,  3>
position=<-41922, -31403> velocity=< 4,  3>
position=<-20862, -41905> velocity=< 2,  4>
position=< 52672,  21160> velocity=<-5, -2>
position=< 31693, -20883> velocity=<-3,  2>
position=<-20889, -10375> velocity=< 2,  1>
position=<-31360,  10642> velocity=< 3, -1>
position=< 10662,  21156> velocity=<-1, -2>
position=< 21158, -10377> velocity=<-2,  1>
position=<-31384,  52691> velocity=< 3, -5>
position=< 10684,  10642> velocity=<-1, -1>
position=<-20846, -31399> velocity=< 2,  3>
position=<-52382, -20885> velocity=< 5,  2>
position=< 31710, -41908> velocity=<-3,  4>
position=<-10349, -20890> velocity=< 1,  2>
position=< 52672,  10647> velocity=<-5, -1>
position=< 10644, -10380> velocity=<-1,  1>
position=<-41882,  52686> velocity=< 4, -5>
position=<-31356,  31670> velocity=< 3, -3>
position=<-10346, -20885> velocity=< 1,  2>
position=<-31384,  42183> velocity=< 3, -4>
position=<-41895, -52416> velocity=< 4,  5>
position=< 52683,  10647> velocity=<-5, -1>
position=<-10375,  21157> velocity=< 1, -2>
position=< 42205,  42174> velocity=<-4, -4>
position=<-20889, -41905> velocity=< 2,  4>
position=< 10636, -52418> velocity=<-1,  5>
position=<-20901, -52421> velocity=< 2,  5>
position=< 10681, -10373> velocity=<-1,  1>
position=<-20889, -20888> velocity=< 2,  2>
position=<-31387, -20891> velocity=< 3,  2>
position=<-31371,  10646> velocity=< 3, -1>
position=<-41879, -10372> velocity=< 4,  1>
position=< 31671,  31665> velocity=<-3, -3>
position=< 10689, -20883> velocity=<-1,  2>
position=< 10641,  52691> velocity=<-1, -5>
position=<-41874,  10643> velocity=< 4, -1>
position=<-52405,  10645> velocity=< 5, -1>
position=<-20852,  10641> velocity=< 2, -1>
position=<-41914, -20891> velocity=< 4,  2>
position=< 52699,  42183> velocity=<-5, -4>
position=< 10630, -10381> velocity=<-1,  1>
position=< 21147, -31400> velocity=<-2,  3>
position=< 42222,  52693> velocity=<-4, -5>
position=< 31695, -41913> velocity=<-3,  4>
position=< 31706,  21161> velocity=<-3, -2>
position=<-31363,  31665> velocity=< 3, -3>
position=< 42193, -41914> velocity=<-4,  4>
position=< 52672,  31670> velocity=<-5, -3>
position=<-10384, -20889> velocity=< 1,  2>
position=< 10684,  21156> velocity=<-1, -2>
position=<-10341, -52421> velocity=< 1,  5>
position=<-41876,  21156> velocity=< 4, -2>
position=< 52728,  42182> velocity=<-5, -4>
position=< 31677, -41909> velocity=<-3,  4>
position=<-31395,  52693> velocity=< 3, -5>
position=< 52689,  10641> velocity=<-5, -1>
position=<-31399,  10641> velocity=< 3, -1>
position=< 52717,  21155> velocity=<-5, -2>
position=<-52398, -10375> velocity=< 5,  1>
position=<-10375,  10641> velocity=< 1, -1>
position=< 42161,  21155> velocity=<-4, -2>
position=< 21139, -31402> velocity=<-2,  3>
position=<-52425, -41905> velocity=< 5,  4>
position=<-52406, -41911> velocity=< 5,  4>
position=<-31389,  21157> velocity=< 3, -2>
position=<-31388,  21157> velocity=< 3, -2>
position=<-52425, -20885> velocity=< 5,  2>
position=<-10394, -10372> velocity=< 1,  1>
position=<-31384, -20891> velocity=< 3,  2>
position=< 42206,  31665> velocity=<-4, -3>
position=<-52385, -31398> velocity=< 5,  3>
position=<-10341, -31400> velocity=< 1,  3>
position=<-10386, -52423> velocity=< 1,  5>
position=<-10346,  52690> velocity=< 1, -5>
position=< 21164, -20883> velocity=<-2,  2>
position=< 42177,  10645> velocity=<-4, -1>
position=< 52725,  10644> velocity=<-5, -1>
position=< 42217,  52685> velocity=<-4, -5>
position=< 31650, -41911> velocity=<-3,  4>
position=<-31379, -41912> velocity=< 3,  4>
position=<-41887,  42181> velocity=< 4, -4>
position=<-52422, -31396> velocity=< 5,  3>
position=<-31376, -20889> velocity=< 3,  2>
position=<-41878,  21156> velocity=< 4, -2>
position=< 10684,  31669> velocity=<-1, -3>
position=< 31677, -41905> velocity=<-3,  4>
position=<-31376, -41905> velocity=< 3,  4>
position=<-52427, -10376> velocity=< 5,  1>
position=< 21142,  42174> velocity=<-2, -4>
position=<-20863, -52421> velocity=< 2,  5>
position=<-52409, -41908> velocity=< 5,  4>
position=< 21192,  21158> velocity=<-2, -2>
position=<-41895, -31400> velocity=< 4,  3>
position=< 52731,  52685> velocity=<-5, -5>
position=<-52398,  10646> velocity=< 5, -1>
position=<-31408, -20883> velocity=< 3,  2>
position=< 21197,  31667> velocity=<-2, -3>
position=<-31389,  52685> velocity=< 3, -5>
position=<-41874,  42177> velocity=< 4, -4>
position=<-52382,  31664> velocity=< 5, -3>
position=<-52385, -31396> velocity=< 5,  3>
position=< 42181, -31399> velocity=<-4,  3>
position=<-20904,  10645> velocity=< 2, -1>
position=<-10370,  42176> velocity=< 1, -4>
position=<-52437, -31403> velocity=< 5,  3>
position=< 31659, -31402> velocity=<-3,  3>
position=< 10656, -41906> velocity=<-1,  4>
position=<-41914,  42179> velocity=< 4, -4>
position=<-20865,  21155> velocity=< 2, -2>
position=<-10374, -31396> velocity=< 1,  3>
position=<-20870,  42178> velocity=< 2, -4>
position=< 21195,  31670> velocity=<-2, -3>
position=< 21139, -31401> velocity=<-2,  3>
position=<-31375, -31399> velocity=< 3,  3>
position=< 42174, -41905> velocity=<-4,  4>
position=< 31687,  31666> velocity=<-3, -3>
position=<-31375, -10372> velocity=< 3,  1>
position=<-10333, -52416> velocity=< 1,  5>
position=< 21167,  52693> velocity=<-2, -5>
position=< 42185,  52686> velocity=<-4, -5>
position=<-10366,  52685> velocity=< 1, -5>
position=< 42185, -10373> velocity=<-4,  1>
position=< 52691, -52425> velocity=<-5,  5>
position=<-41887,  52692> velocity=< 4, -5>
position=< 31663,  31666> velocity=<-3, -3>
position=< 42201,  31665> velocity=<-4, -3>
position=<-41900,  42174> velocity=< 4, -4>
position=< 31710,  42181> velocity=<-3, -4>
position=<-52382, -20890> velocity=< 5,  2>
position=< 42214, -41914> velocity=<-4,  4>
position=< 10647, -10377> velocity=<-1,  1>
position=< 31703, -20883> velocity=<-3,  2>
position=< 31690, -20883> velocity=<-3,  2>
position=< 10644, -20891> velocity=<-1,  2>
position=< 21152,  52691> velocity=<-2, -5>
position=<-20873,  10648> velocity=< 2, -1>
position=<-31408, -52423> velocity=< 3,  5>
position=< 31658, -41910> velocity=<-3,  4>
position=<-10337, -41910> velocity=< 1,  4>
position=< 21196, -10381> velocity=<-2,  1>
position=< 42205, -10381> velocity=<-4,  1>
position=<-10383,  52691> velocity=< 1, -5>
position=<-10362,  52688> velocity=< 1, -5>
position=<-52380, -41914> velocity=< 5,  4>
position=< 52704,  31665> velocity=<-5, -3>
position=< 52700, -31398> velocity=<-5,  3>
position=< 52714,  10650> velocity=<-5, -1>
position=< 42201, -52417> velocity=<-4,  5>
position=<-20849,  21161> velocity=< 2, -2>
position=<-20902,  42174> velocity=< 2, -4>
position=< 31692, -41905> velocity=<-3,  4>
position=< 10631, -20888> velocity=<-1,  2>
position=< 42197,  10641> velocity=<-4, -1>
position=<-10351,  42174> velocity=< 1, -4>
position=< 10677, -20888> velocity=<-1,  2>
position=< 31701,  10645> velocity=<-3, -1>
position=<-31400,  31670> velocity=< 3, -3>
position=< 21181,  21152> velocity=<-2, -2>
position=< 10673,  21154> velocity=<-1, -2>
position=< 52733, -10372> velocity=<-5,  1>
position=< 10644, -41908> velocity=<-1,  4>
position=< 42190,  10650> velocity=<-4, -1>
position=<-20905,  52688> velocity=< 2, -5>
position=<-10362, -10376> velocity=< 1,  1>
position=< 31711,  21155> velocity=<-3, -2>
position=< 10652,  52692> velocity=<-1, -5>
position=<-41891, -31399> velocity=< 4,  3>
position=< 21171, -41908> velocity=<-2,  4>
position=< 31682, -10377> velocity=<-3,  1>
position=< 52705,  42174> velocity=<-5, -4>
position=< 52681, -41913> velocity=<-5,  4>
position=< 42164, -41914> velocity=<-4,  4>
position=<-10346, -31397> velocity=< 1,  3>
position=<-31363,  42175> velocity=< 3, -4>
position=< 42189,  10641> velocity=<-4, -1>
position=<-20892,  42181> velocity=< 2, -4>
position=< 21155, -10381> velocity=<-2,  1>
position=< 10636, -52420> velocity=<-1,  5>
position=<-41871,  52693> velocity=< 4, -5>
position=< 42212,  42178> velocity=<-4, -4>
position=< 31707,  42174> velocity=<-3, -4>
position=< 52728,  31668> velocity=<-5, -3>
position=< 31703, -20886> velocity=<-3,  2>
position=<-52438, -10375> velocity=< 5,  1>
position=<-20892,  21152> velocity=< 2, -2>
position=<-31384, -41913> velocity=< 3,  4>
position=< 52677, -52425> velocity=<-5,  5>
position=<-52438,  31668> velocity=< 5, -3>
position=<-20885,  52685> velocity=< 2, -5>
position=<-31384, -41914> velocity=< 3,  4>
position=< 31698, -10381> velocity=<-3,  1>
position=<-52398, -10373> velocity=< 5,  1>
position=< 31709, -10381> velocity=<-3,  1>
position=< 10685, -31399> velocity=<-1,  3>
position=<-41868, -10381> velocity=< 4,  1>
position=< 52688, -52417> velocity=<-5,  5>
position=< 10669, -31399> velocity=<-1,  3>
position=< 10628, -52424> velocity=<-1,  5>
position=< 31698, -31397> velocity=<-3,  3>
position=<-52379, -10376> velocity=< 5,  1>
position=< 21187,  52687> velocity=<-2, -5>
position=<-41914,  10649> velocity=< 4, -1>
position=< 42201,  10648> velocity=<-4, -1>
position=<-41866, -31402> velocity=< 4,  3>
position=< 31650,  31663> velocity=<-3, -3>
position=<-20901, -52421> velocity=< 2,  5>
position=< 42209,  21160> velocity=<-4, -2>
position=< 21150, -31398> velocity=<-2,  3>
position=< 31671, -20891> velocity=<-3,  2>
position=<-20871, -52421> velocity=< 2,  5>
position=<-10378,  52691> velocity=< 1, -5>
position=<-10338, -20886> velocity=< 1,  2>
position=<-52420, -20888> velocity=< 5,  2>
position=< 10676,  52690> velocity=<-1, -5>
position=<-10394, -41914> velocity=< 1,  4>
position=<-41869, -41910> velocity=< 4,  4>
position=< 52693,  52688> velocity=<-5, -5>
position=< 10629,  10641> velocity=<-1, -1>
position=<-20848, -10381> velocity=< 2,  1>
position=<-31400,  31668> velocity=< 3, -3>
position=<-31375,  42174> velocity=< 3, -4>
position=<-10378, -41909> velocity=< 1,  4>
position=< 21181,  31672> velocity=<-2, -3>
position=<-41882,  21160> velocity=< 4, -2>
position=< 52688,  42179> velocity=<-5, -4>
position=<-41879, -31399> velocity=< 4,  3>
position=<-41914, -41907> velocity=< 4,  4>
position=<-10358,  21156> velocity=< 1, -2>
position=< 21164, -20892> velocity=<-2,  2>
position=<-20849, -31394> velocity=< 2,  3>
position=< 21179, -10381> velocity=<-2,  1>
position=<-20897, -41910> velocity=< 2,  4>
position=< 31711, -31401> velocity=<-3,  3>
position=< 42177, -41911> velocity=<-4,  4>
position=< 42169, -31401> velocity=<-4,  3>
position=<-31368,  31666> velocity=< 3, -3>
position=<-10338,  42178> velocity=< 1, -4>
position=< 10681, -31394> velocity=<-1,  3>
position=<-52401, -10378> velocity=< 5,  1>
position=< 52672,  31667> velocity=<-5, -3>
position=< 10647, -31399> velocity=<-1,  3>
position=< 10672,  42183> velocity=<-1, -4>
position=<-52398, -10375> velocity=< 5,  1>
position=<-31398, -31399> velocity=< 3,  3>
position=< 31675, -52416> velocity=<-3,  5>
position=<-31389, -10381> velocity=< 3,  1>
position=< 42170,  10643> velocity=<-4, -1>
position=<-52389, -10377> velocity=< 5,  1>
position=<-31371, -41911> velocity=< 3,  4>
position=< 52672,  52692> velocity=<-5, -5>
position=< 31677, -41905> velocity=<-3,  4>
position=< 21155, -31395> velocity=<-2,  3>
position=< 10686,  52689> velocity=<-1, -5>
position=< 21165,  31663> velocity=<-2, -3>
position=<-10373,  42176> velocity=< 1, -4>
position=< 31662, -10374> velocity=<-3,  1>
position=< 31671, -31395> velocity=<-3,  3>
position=<-10386, -52418> velocity=< 1,  5>
position=<-41898,  10649> velocity=< 4, -1>
position=<-31357, -52421> velocity=< 3,  5>
position=<-20849,  52688> velocity=< 2, -5>
position=<-52428,  10645> velocity=< 5, -1>
position=<-52396, -41914> velocity=< 5,  4>
position=< 21187,  52686> velocity=<-2, -5>
position=< 10689,  42175> velocity=<-1, -4>
position=< 21147,  21152> velocity=<-2, -2>
position=< 52713, -52421> velocity=<-5,  5>
position=<-41906, -52416> velocity=< 4,  5>
position=< 42188, -31398> velocity=<-4,  3>
position=<-52394, -20888> velocity=< 5,  2>
position=<-41924, -52421> velocity=< 4,  5>
position=< 31703, -31395> velocity=<-3,  3>
position=<-10378, -52421> velocity=< 1,  5>
position=<-20881,  10642> velocity=< 2, -1>
position=< 31682,  21154> velocity=<-3, -2>
position=< 31710,  21158> velocity=<-3, -2>
position=<-41911, -20883> velocity=< 4,  2>
position=< 10652,  31666> velocity=<-1, -3>
position=< 42173, -41906> velocity=<-4,  4>
position=<-10382, -41907> velocity=< 1,  4>
position=<-20888, -52421> velocity=< 2,  5>
position=<-10333, -31400> velocity=< 1,  3>
position=< 21148, -52424> velocity=<-2,  5>
position=<-31398, -10381> velocity=< 3,  1>
position=< 42185,  42180> velocity=<-4, -4>
position=< 21187, -52424> velocity=<-2,  5>
position=<-20864,  10641> velocity=< 2, -1>
position=< 31684, -31403> velocity=<-3,  3>
position=< 21152, -41910> velocity=<-2,  4>
position=< 42174, -20888> velocity=<-4,  2>
position=< 42169,  52691> velocity=<-4, -5>
position=<-10394, -20884> velocity=< 1,  2>
position=<-41919,  31671> velocity=< 4, -3>
position=<-52388,  10645> velocity=< 5, -1>
position=< 21165, -31394> velocity=<-2,  3>
position=<-41898,  10646> velocity=< 4, -1>
position=<-52385,  10647> velocity=< 5, -1>

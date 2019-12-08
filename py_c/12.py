#!/usr/bin/python

from parse import parse

plant_state='##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#...............................................................................................................................................................................................................................................................................'
# plant_state='#..#.#..##......###...###.........................................'

def segment_n(plants, center_pos, pattern_len):
	pos = center_pos-2
	if pos<0 and pos+pattern_len>=0:
		return plants[pos:]+plants[:pos+pattern_len]
	else:
		return plants[pos:pos+pattern_len]
		
rec_nr = 0
plant_patterns = {}

with open('12.txt') as f:
	for line in f:
		rec_nr += 1
		if (rec_nr>2):
			pattern, value = parse('{} => {}', line.strip())
			plant_patterns[pattern] = value

def next_plant_iter(act_state, patterns, pattern_len):
	next_state = list(act_state)
	for pos in range(-len(act_state)/2, len(act_state)/2):
		act_segment = segment_n(act_state, pos, pattern_len)
		next_state[pos] = plant_patterns[segment_n(act_state, pos, pattern_len)]
	return "".join(next_state)

def plant_sum(act_state):
	sum_val=0
	for pos in range(0, len(act_state)):
		if plant_state[pos]=='#':
			sum_val += pos
	return sum_val

iter_no = 0
while iter_no < 20:
	plant_state = next_plant_iter(plant_state, plant_patterns, 5)
	iter_no += 1

print(iter_no, plant_state)
sum_20=plant_sum(plant_state)

while iter_no < 120:
	plant_state = next_plant_iter(plant_state, plant_patterns, 5)
	iter_no += 1
	print(iter_no, plant_sum(plant_state), plant_state)

sum_120=plant_sum(plant_state)

sum_50000000000 = sum_120 + (50000000000-120) * 87

print sum_20, sum_120, sum_50000000000


	

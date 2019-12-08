#!/usr/bin/python

import sys
import os

step_list = {}

with open('7o.txt') as f:
    for line in f:
		line = line.strip()
		step = line[5];
		depends_on = line[36];

		if step not in step_list:
			step_list[step] = []
		step_list[step].append(depends_on)

		if depends_on not in step_list:
			step_list[depends_on] = []
result = ''

while len(step_list)>0:
	nodep_list = []
#	print step_list
	for step in step_list:
		if len(step_list[step]) == 0:
			nodep_list.append(step)
	nodep_list.sort()
	removable_step = nodep_list[0]

#	print nodep_list
	for step in step_list:
		if removable_step in step_list[step]:
			step_list[step].remove(removable_step)
	step_list.pop(removable_step)
	result += removable_step
print result

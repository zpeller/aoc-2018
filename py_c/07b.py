#!/usr/bin/python

import sys
import os
import string

NUM_WORKERS = 5
MIN_SECS = 60

def secs_to_complete(step):
	return MIN_SECS+ord(step)-ord('A')+1

def get_nodeps_no_work(l_step_list, l_work_list):
	l_nodep_list = []
	for step in l_step_list:
		if step not in l_work_list and len(l_step_list[step]) == 0:
			l_nodep_list.append(step)
	l_nodep_list.sort()
	return l_nodep_list

def remove_step(l_step_list, removable_step):
	for step in l_step_list:
		if removable_step in l_step_list[step]:
			l_step_list[step].remove(removable_step)
	l_step_list.pop(removable_step)
	return l_step_list

step_list = {}

with open('7o.txt') as f:
    for line in f:
		line = line.strip()
		step = line[36];
		depends_on = line[5];

		if step not in step_list:
			step_list[step] = []
		step_list[step].append(depends_on)

		if depends_on not in step_list:
			step_list[depends_on] = []

done = ''

work_list = {}
time = 0
while len(step_list)>0 or len(work_list)>0:
	for work in work_list.keys():
		if work_list[work] <= time:
			work_list.pop(work)
			done += work
			step_list = remove_step(step_list, work)

	print(time, work_list, done)
	
	if len(work_list) >= NUM_WORKERS:
		time += 1
		continue
	
	removable_steps = get_nodeps_no_work(step_list, work_list)

	if len(removable_steps) == 0:
		time += 1
		continue

	while len(removable_steps)>0 and len(work_list)<NUM_WORKERS:
		r_step = removable_steps[0]
		work_list[r_step] = time + secs_to_complete(r_step)
		removable_steps.remove(r_step)

	time += 1



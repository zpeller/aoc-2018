#!/usr/bin/python

import sys
import os

def sum_metadata():
	global meta_inf
	num_chnodes = meta_inf.pop(0)
	num_metadata = meta_inf.pop(0)

#	print('1:', num_chnodes, num_metadata, meta_inf)

	if num_chnodes == 0:
		sum_nodes_meta = 0
		while (num_metadata>0):
			sum_nodes_meta += meta_inf.pop(0)
			num_metadata -= 1
#		print('3:', num_chnodes, num_metadata, meta_inf)
		return sum_nodes_meta

	child_list = []
	while (num_chnodes>0):
		child_value = sum_metadata()
		child_list.append(child_value)
		num_chnodes -= 1
	
	sum_nodes_child = 0
	while (num_metadata>0):
		child_index = meta_inf.pop(0)-1
		if child_index>=0 and child_index<len(child_list):
			sum_nodes_child += child_list[child_index]
		num_metadata -= 1
#	print('2:', num_chnodes, num_metadata, meta_inf)

	return sum_nodes_child

meta_inf = []

with open('8.txt') as f:
    for line in f:
		line = int(line.strip())
		meta_inf.append(line)

sum_meta = 0
while len(meta_inf)>0:
	sum_meta += sum_metadata()
	print ('MAIN:', meta_inf, sum_meta)

print(meta_inf, sum_meta)

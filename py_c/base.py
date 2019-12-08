#!/usr/bin/pypy

import sys

input_file='.txt'
debug = False

if len(sys.argv) > 1 and sys.argv[1]=='-d':
	debug = True

def dprint(*arg):
	if not debug:
		return
	print(arg)

def parse_number_from_string(line, pos):
	rv = ''
	act_pos = pos
	while line[act_pos] in list('0123456789'):
		rv += line[act_pos]
		act_pos += 1
	return rv, act_pos

with open(input_file) as f:
	for line in f:
		line = line.strip('\n')


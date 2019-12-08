#!/usr/bin/python

import sys
import os

def count23(line):
	cnt2 = 0
	cnt3 = 0
	char_counts = {}

	for c in line:
		if c not in char_counts:
			char_counts[c]=1
		else:
			char_counts[c] += 1
	if 2 in char_counts.values():
		cnt2 = 1
	if 3 in char_counts.values():
		cnt3 = 1
	print(line, char_counts, cnt2, cnt3)

	return cnt2, cnt3

count_2 = 0
count_3 = 0

with open('2.txt') as f:
    for line in f:
		res2,res3 = count23(line.strip())
		count_2 += res2
		count_3 += res3

print(count_2, count_3, count_2*count_3)

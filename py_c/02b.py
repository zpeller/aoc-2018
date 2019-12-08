#!/usr/bin/python

import sys
import os

def one_diff(s1, s2):
	diff=0
	for i in range(0, len(s1)):
		if (s1[i] != s2[i]):
			diff += 1
			if diff>1:
				return False
	return diff==1

str_list = []

with open('2.txt') as f:
    for line in f:
		line = line.strip()
		str_list.append(line)
for str1 in str_list:
	for str2 in str_list:
		if one_diff(str1, str2):
			print(str1, str2)

#!/usr/bin/python

recipes = [3, 7]

#dst = 9
#dst = 18
#dst = 2018
dst = 74501

round = 1

pos_elf0 = 0
pos_elf1 = 1

while len(recipes) <= dst+10:
	score_elf0 = recipes[pos_elf0]
	score_elf1 = recipes[pos_elf1]
	new_recipe = score_elf0 + score_elf1
	if new_recipe<10:
		recipes.append(new_recipe)
	else:
		recipes.extend( map(int, list(str(new_recipe))) )

	pos_elf0 += score_elf0 + 1
	while pos_elf0 >= len(recipes):
		pos_elf0 -= len(recipes)

	pos_elf1 += score_elf1 + 1
	while pos_elf1 >= len(recipes):
		pos_elf1 -= len(recipes)

#	print(round, pos_elf0, pos_elf1, recipes)
	round += 1

print("".join(map(str, recipes[dst:dst+10])))



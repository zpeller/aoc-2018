#!/usr/bin/python

recipes = [3, 7]

#dst = 9
#dst = 18
#dst = 2018
#dst = 74501

patterns = ['51589', '01245', '92510', '59414', '74501', '074501']

round = 1
match_pos = 0

pos_elf0 = 0
pos_elf1 = 1

pattern = map(int, list(patterns[5]))

while True:
	score_elf0 = recipes[pos_elf0]
	score_elf1 = recipes[pos_elf1]
	new_recipe = score_elf0 + score_elf1
	if new_recipe<10:
		recipes.append(new_recipe)
		no_new_recipes = 1
	else:
		recipes.extend( map(int, list(str(new_recipe))) )
		no_new_recipes = 2
	
#	print(pattern, recipes[match_pos:match_pos+len(pattern)], recipes[match_pos+1:match_pos+len(pattern)+1] if no_new_recipes==2 else "")
	if recipes[match_pos:match_pos+len(pattern)] == pattern:
#		print('1:', len(recipes)-len(pattern))
		print('2:', match_pos)
		break

	if no_new_recipes == 2  and recipes[match_pos+1:match_pos+len(pattern)+1] == pattern:
#		print('3:', len(recipes)-len(pattern))
		print('4:', match_pos+1)
		break
	
	if (len(recipes)>len(pattern)):
		match_pos += no_new_recipes

	pos_elf0 += score_elf0 + 1
	while pos_elf0 >= len(recipes):
		pos_elf0 -= len(recipes)

	pos_elf1 += score_elf1 + 1
	while pos_elf1 >= len(recipes):
		pos_elf1 -= len(recipes)

#	print(round, pos_elf0, pos_elf1, recipes)
	round += 1

# print("".join(map(str, recipes)))
print("".join(map(str, recipes[-20:])))



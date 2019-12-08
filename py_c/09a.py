#!/usr/bin/python

# 462 players; last marble is worth 71938 points

DEBUG = True
# NUM_PLAYERS, MAX_MARBLE = 9, 25
# NUM_PLAYERS, MAX_MARBLE = 10, 1618 
# NUM_PLAYERS, MAX_MARBLE = 13, 7999
NUM_PLAYERS, MAX_MARBLE = 462, 7193800

player_score = {}
marble_circle = [0]

def add_new_marble(act_id, new_id):
	global marble_circle
	insert_point = act_id + 2
	if insert_point>len(marble_circle):
		insert_point -= len(marble_circle)
	marble_circle.insert(insert_point, new_id)
	return insert_point
		
def remove_marble_7(act_id):
	global marble_circle
	remove_point = act_id - 7
	if remove_point<0:
		remove_point += len(marble_circle)
	marble_score = marble_circle.pop(remove_point)
	return remove_point, marble_score
		
act_marble = 0
marble_id = 1
player_id = 1

while marble_id <= MAX_MARBLE:
	if marble_id%10000 == 0:
		print marble_id
	if marble_id%23 == 0:
		act_marble, score = remove_marble_7(act_marble)
		if player_id not in player_score:
			player_score[player_id] = marble_id+score
		else:
			player_score[player_id] += marble_id+score
			
#		print('7:', player_id, player_score[player_id], marble_id, score)
	else:
		act_marble = add_new_marble(act_marble, marble_id) 
#	print(act_marble, marble_circle)
	player_id += 1
	if player_id>NUM_PLAYERS:
		player_id=1
	marble_id += 1

# print player_score
print max(player_score.values())

#!/usr/bin/python

import sys
import copy
from parse import parse

input_file='24.txt'
debug = False

group_id = 0

class Group:
	def __init__(self, group_type, no_of_units, hitpoints, immunities, weaknesses, attack_damage, attack_damage_type, initiative):
		global group_id

		self.group_id = group_id
		group_id += 1

		self.group_type = group_type
		self.no_of_units = no_of_units
		self.hitpoints = hitpoints
		self.immunities = immunities
		self.weaknesses = weaknesses
		self.attack_damage = attack_damage
		self.attack_damage_type = attack_damage_type
		self.initiative = initiative
		self.effective_power = self.no_of_units * self.attack_damage
	
	def add_boost(self, boost):
		self.attack_damage += boost
		self.effective_power = self.no_of_units * self.attack_damage

	def take_damage(self, damage):
		units_to_lose = damage/self.hitpoints
		self.no_of_units -= units_to_lose
		if self.no_of_units<0:
			self.no_of_units = 0
		self.effective_power = self.no_of_units * self.attack_damage
		return self.no_of_units <= 0

	def __repr__(self):
		return "<id:%d t:%s u:%d ep:%d fhp:%d i:%d>" % (self.group_id, self.group_type, self.no_of_units, self.effective_power, self.no_of_units*self.hitpoints, self.initiative)

	def __str__(self):
		return "<%2d %-10sunits: %4d ep: %6d hp: %5d init: %3d dmg: %3d dmgtype: %-12s im: %s weak: %s>" % (self.group_id, self.group_type, self.no_of_units, self.effective_power, self.hitpoints, self.initiative, self.attack_damage, self.attack_damage_type, self.immunities, self.weaknesses)

	def __lt__(self, other):
		if self.effective_power != other.effective_power:
			return self.effective_power < other.effective_power
		return self.initiative < other.initiative
	
armies = {'immune': [], 'infection': []}
groups = []

if len(sys.argv) > 1 and sys.argv[1]=='-d':
	debug = True

def dprint(*arg):
	if not debug:
		return
	if arg[0] == '':
		print("")
	else:
		print(arg)

#def parse_number_from_string(line, pos):
#	rv = ''
#	act_pos = pos
#	while line[act_pos] in list('0123456789'):
#		rv += line[act_pos]
#		act_pos += 1
#	return rv, act_pos


def parse_immunities_weaknesses(iwtext):
#	print iwtext
	weaknesses=[]
	immunities=[]
	if ';' in iwtext:
		if iwtext[0]=='w':
			params = parse('weak to {}; immune to {}', iwtext)
			weaknesses = params[0].split(', ')
			immunities = params[1].split(', ')
		else:
			params = parse('immune to {}; weak to {}', iwtext)
			immunities = params[0].split(', ')
			weaknesses = params[1].split(', ')
	elif iwtext[0] == 'w':
		params = parse('weak to {}', iwtext)
		weaknesses = params[0].split(', ')
	else:
		params = parse('immune to {}', iwtext)
		immunities = params[0].split(', ')
	return immunities, weaknesses

def parse_line_for_group_params(line, group_type):
#	print(line)
	params = parse('{} units each with {} hit points{}with an attack that does {} {} damage at initiative {}', line)
	no_of_units = int(params[0])
	hitpoints = int(params[1])
	attack_damage = int(params[3])
	attack_damage_type = params[4]
	initiative = int(params[5])
#	print(no_of_units, group_type, params[2])
	if params[2] != ' ':
		param_end = len(params[2])-2
		immunities, weaknesses = parse_immunities_weaknesses(params[2][2:param_end])
	else:
		weaknesses = []
		immunities = []
	return Group(group_type, no_of_units, hitpoints, immunities, weaknesses, attack_damage, attack_damage_type, initiative)

def read_groups():
	group_type = ''
	with open(input_file) as f:
		for line in f:
			line = line.strip('\n')
			if line == 'Immune System:':
				group_type = 'immune'
				continue
			if line == 'Infection:':
				group_type = 'infection'
				continue
			if line=='' or line[0] not in '0123456789':
				continue
			new_group = parse_line_for_group_params(line, group_type)
#			if new_group.group_type == 'immune':
#				new_group.add_boost(1570)
			armies[group_type].append(new_group)
			groups.append(new_group)

def enemy_group_type(group_type):
	return 'immune' if group_type == 'infection' else 'infection'

def calc_damage_to_deal(attacking_group, defending_group):
	if attacking_group.attack_damage_type in defending_group.immunities:
		return 0
	damage = attacking_group.effective_power
	if attacking_group.attack_damage_type in defending_group.weaknesses:
		damage *= 2
	return damage

def select_target(group, chosen_targets):
	max_damage = 0
	max_damage_group = None

	for target_group in armies[enemy_group_type(group.group_type)]:
#		print('Possible target: ',group, '->', target_group)
		if target_group in chosen_targets:
			continue
		damage = calc_damage_to_deal(group, target_group)
#		print('Possible damage:', target_group, damage)
		if damage > max_damage:
			max_damage = damage
			max_damage_group = target_group
			continue
		if damage>0 and damage == max_damage:
			if target_group.effective_power > max_damage_group.effective_power:
				max_damage_group = target_group
				continue
			if target_group.effective_power == max_damage_group.effective_power:
				if target_group.initiative > max_damage_group.initiative:
					max_damage_group = target_group
	return max_damage_group, max_damage

def attack(attacking_group, defending_group):
	damage = calc_damage_to_deal(attacking_group, defending_group)
	is_killed = defending_group.take_damage(damage)
	return is_killed
			
def remove_group(group):
	global groups
	global armies
	dprint('Removing', group)
	groups.remove(group)
	armies[group.group_type].remove(group)

def play_round():
	targets = {}
	rem_units_before = count_remaining_units()
	for group in sorted(groups, reverse=True):
		target_group, maxdmg = select_target(group, targets.values())
		if target_group:
			targets[group] = target_group
			dprint('Target: ',group, '->', targets[group], ':', maxdmg)
		else:
			dprint('Target: ',group, '-> No target')

	for group in sorted(groups, reverse=True, key=lambda x: x.initiative):
		if group not in targets.keys() or group not in groups:
			continue
		dprint('Attack', str(group) , '->', str(targets[group]), calc_damage_to_deal(group, targets[group]))
		is_target_dead = attack(group, targets[group])
		if is_target_dead:
			dprint('Dead, removing', targets[group])
			remove_group(targets[group])
			if group in targets.keys():
				targets.pop(group)
	dprint(groups)
	return rem_units_before == count_remaining_units()

read_groups()
# print(armies)
for group in armies['immune']+armies['infection']:
	print group

def count_remaining_units():
	rem_units = 0
	for group in groups:
		rem_units += group.no_of_units
	return rem_units

def play_rounds_with_boosts():
	global armies
	global groups
	global debug

	boost = 0
	while True:
		armies = {'immune': [], 'infection': []}
		groups = []
		read_groups()

		print('Fight with boost: '+str(boost))
		for group in armies['immune']:
			group.add_boost(boost)

		is_draw = False
		while len(armies['immune'])>0 and len(armies['infection'])>0 and not is_draw:
			is_draw = play_round()
			dprint("")

		if not is_draw:
			print('Winner: '+groups[0].group_type + ' remaining: ' +str(count_remaining_units()))
			if len(armies['immune'])>0:
				break
		else:
			print('Draw detected, no damage dealt in a round, remaining: ' +str(count_remaining_units()))
			print(groups)
			print("")
		boost += 1

#print('Remaining units: '+str(rem_units))

play_rounds_with_boosts()

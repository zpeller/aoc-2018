#!/usr/bin/python

from parse import parse

input_file='16a.txt'
debug = True

def dprint(*arg):
	if not debug:
		return
	print(arg)

def before(line):
	return eval(parse('Before: {}', line)[0])

def after(line):
	return eval(parse('After: {}', line)[0])

def opline(line):
	return map(int, parse('{} {} {} {}', line))


def addr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] + registers[arg2]
	return registers

def addi(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] + arg2
	return registers

def mulr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] * registers[arg2]
	return registers

def muli(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] * arg2
	return registers

def banr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] & registers[arg2]
	return registers

def bani(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] & arg2
	return registers

def borr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] | registers[arg2]
	return registers

def bori(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1] | arg2
	return registers

def setr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = registers[arg1]
	return registers

def seti(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = arg1
	return registers

def gtir(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = 1 if arg1 > registers[arg2] else 0
	return registers

def gtri(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = 1 if registers[arg1] > arg2 else 0
	return registers

def gtrr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = 1 if registers[arg1] > registers[arg2] else 0
	return registers

def eqir(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = 1 if arg1 == registers[arg2] else 0
	return registers

def eqri(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = 1 if registers[arg1] == arg2 else 0
	return registers

def eqrr(input_registers, arg1, arg2, dst_reg):
	registers = list(input_registers)
	registers[dst_reg] = 1 if registers[arg1] == registers[arg2] else 0
	return registers

operators = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

opcodes={}
for opc in range(len(operators)):
	opcodes[opc] = operators

def evaluate(r0, r1, opargs):
#	print r0, r1, opargs
	global opcodes

	act_opcode = opargs[0]
	good_opcodes = []
	ok_cnt = 0
	ok_func = ''
	for func in opcodes[act_opcode]:
		result = func(r0, opargs[1], opargs[2], opargs[3])
#		print func, result
		if result[opargs[3]] == r1[opargs[3]]:
			ok_cnt += 1
			good_opcodes.append(func)
	opcodes[act_opcode] = good_opcodes
	if len(good_opcodes) == 1:
		single_func = good_opcodes[0]
		for opc in opcodes:
			if opc == act_opcode:
				continue
			if single_func in opcodes[opc]:
				opcodes[opc].remove(single_func)
		
	return ok_cnt

opcode_3 = 0
line_no = 0
with open(input_file) as f:
	for line in f:
		line = line.strip('\n')
#		print(line)
		if line_no%4 == 0:
			reg0 = before(line)
		elif line_no%4 == 1:
			op = opline(line)
		elif line_no%4 == 2:
			reg1 = after(line)
		else:
			if evaluate(reg0, reg1, op) >= 3:
				opcode_3 += 1
		line_no += 1

print("3 or more opcodes: ", opcode_3)

print(opcodes)
for opc in opcodes:
	for func in opcodes[opc]:
		print(opc, func.__name__)

line_no = 0
start_regs = [0, 0, 0, 0]
with open('16b.txt') as f:
	for line in f:
		line = line.strip('\n')
#		print(line)
		op = opline(line)
		func = opcodes[op[0]][0]
		start_regs = func(start_regs, op[1], op[2], op[3])
		print(start_regs)



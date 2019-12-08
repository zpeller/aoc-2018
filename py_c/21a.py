#!/usr/bin/pypy

import sys

if len(sys.argv)>1 and sys.argv[1]=='-d':
	lineprint=True
else:
	lineprint=False
	
if len(sys.argv)>1 and sys.argv[1]=='-p':
	ptrprint=True
else:
	ptrprint=False
	
input_file='21a.txt'
debug = True

ip_reg = -1
program = []

def dprint(*arg):
	if not debug:
		return
	print(arg)

def get_num_string(line, pos):
	rv = ''
	act_pos = pos
	while line[act_pos]!=' ':
		rv += line[act_pos]
		act_pos += 1
	return rv, act_pos

def opline(line):
	func = line[0:4]
	arg1, pos = get_num_string(line, 5)
	arg2, pos = get_num_string(line, pos+1)
	arg3 = line[pos+1:]
	return [func, int(arg1), int(arg2), int(arg3)]

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

operator_funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
operators = {}

for operator_function in operator_funcs:
	operators[operator_function.__name__] = operator_function

def read_program_from_file():
	global program
	global ip_reg
	program_line = 0

	first_line = True
	with open(input_file) as f:
		for line in f:
			line = line.strip('\n')
			if first_line:
				ip_reg = int(line[4])
				print(ip_reg)
				first_line = False
				continue
			op = opline(line)
			func = operators[op[0]]
			program.append((func, op[1], op[2], op[3]))
			print(program_line, op)
			program_line += 1


read_program_from_file()
print program

def run_program(registers, max_iter):
	i_ptr = 0
	max_i_ptr = len(program)-1
	iter_no = 0
	while i_ptr <= max_i_ptr and iter_no < max_iter:
		if iter_no %1000000000 == 0:
			print('r0:', registers[0], 'iterno:', iter_no)
		registers[ip_reg] = i_ptr
		prog_line = program[i_ptr]
		func = prog_line[0]
		new_regs = func(registers, prog_line[1], prog_line[2], prog_line[3])
		if lineprint or (ptrprint and i_ptr == 16):
			print(iter_no, "ip=", i_ptr, registers, prog_line, new_regs)
		registers = new_regs
		i_ptr = registers[ip_reg]
		i_ptr += 1
		iter_no += 1
	return registers, iter_no, i_ptr>max_i_ptr

# problem 1:
dev_registers = [0, 0, 0, 0, 0, 0]
# problem 2:
# registers = [1, 0, 0, 0, 0, 0]


# for r0 in range(1, 203000):
# 	if r0%1000 == 0:
# 		print r0
# 	dev_registers = [r0, 0, 0, 0, 0, 0]
# 	dev_registers, iter_no, is_halt = run_program(dev_registers, 100000)
# 	if is_halt:
# 		break

# 202209!
# print('lowest halt:', iter_no, r0, dev_registers, is_halt)
# sys.exit(1)

#for r0 in (194263, 202209, 10820795, 13974346):
#for r0 in (5595, 26652, 28438, 28988, 31643, 32181):
# 32181 guessed, too low!
# largest so far (still too low): ('new largest halt, iters:', 2739949429, 'r0:', 60616, [60616, 1, 1, 249, 30, 60616], True)
# ('new largest halt, iters:', 2752472783, 'r0:', 546620, [546620, 1, 1, 19, 30, 546620], True)

max_iters = 0
with open('21x2.out') as f:
	for line in f:
		r0 = int(line.strip('\n'))
		dev_registers = [r0, 0, 0, 0, 0, 0]
		dev_registers, iter_no, is_halt = run_program(dev_registers, 20000000000)
		print('lowest halt:', iter_no, r0, dev_registers, is_halt)
		if is_halt and iter_no > max_iters:
			print("!!!")
			print('new largest halt, iters:', iter_no, 'r0:', r0, dev_registers, is_halt)
			print("!!!")
			max_iters = iter_no

sys.exit(1)

max_iters = 0
for r0 in range(1, 100000000):
	if r0%1000 == 0:
		print r0
	dev_registers = [r0, 0, 0, 0, 0, 0]
	dev_registers, iter_no, is_halt = run_program(dev_registers, 10000000000)
	if is_halt and max_iters<iter_no:
		max_iters = iter_no
		print('highest halt:', max_iters, r0, dev_registers, is_halt)

print('highest halt:', iter_no, r0, dev_registers, is_halt)


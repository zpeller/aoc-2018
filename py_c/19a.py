#!/usr/bin/python

from parse import parse

input_file='19.txt'
debug = True

ip_reg = -1
program = []

def dprint(*arg):
	if not debug:
		return
	print(arg)

def opline(line):
	op = parse('{} {} {} {}', line)
	return [op[0], int(op[1]), int(op[2]), int(op[3])]

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
				ip_reg = int(parse('#ip {}', line)[0])
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

# problem 1:
# registers = [0, 0, 0, 0, 0, 0]
# problem 2:
registers = [1, 0, 0, 0, 0, 0]
i_ptr = 0
max_i_ptr = len(program)-1

iter_no = 0
while i_ptr <= max_i_ptr:
	if iter_no %100000 ==0:
		print iter_no
	registers[ip_reg] = i_ptr
	prog_line = program[i_ptr]
	func = prog_line[0]
	new_regs = func(registers, prog_line[1], prog_line[2], prog_line[3])
	print(iter_no, "ip=", i_ptr, registers, prog_line, new_regs)
	registers = new_regs
	i_ptr = registers[ip_reg]
	i_ptr += 1
	iter_no += 1

print(iter_no, registers[0])


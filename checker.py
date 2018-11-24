#!/usr/local/bin/python3.7

import ps_functions as ps

try:
	f = open("numbers")
	numbers_string = f.read()
	f.close()
except:
	print("checker.py: could not open \"numbers\"")
	exit(-1)

try:
	f = open("ops")
	ops_string = f.read()
	f.close
except:
	print("checker.py: could not open \"ops\"")
	exit(-1)

numbers_list = numbers_string.split(" ")
ops_list = ops_string.split(" ")

stack_a = []
stack_b = []

try:
	for x in numbers_list:
		stack_a.append(int(x))
except:
	print("checker.py: failed to read number strings")

for x in ops_list:
	ps.run_command(x, stack_a, stack_b)

if ps.is_sorted(stack_a) and len(stack_b) == 0:
	print("OK")
else:
	print("KO")
	print(stack_a)
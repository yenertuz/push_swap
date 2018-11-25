#!/usr/local/bin/python3.7

import os
import ps_functions as ps
import signal


def signal_handler(signal, frame):
	print(ops_list)
	exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
	f = open("numbers")
	numbers_string = f.read()
	f.close()
except:
	print("push_swap.py: could not open \"numbers\"")
	exit(-1)

try:
	f = open("ops", "w")
except:
	print("push_swap.py: could not open \"ops\"")
	exit(-1)

numbers_list = numbers_string.split(" ")
ops_list = []
stack_a = []
stack_b = []

try:
	for x in numbers_list:
		stack_a.append(int(x))
except:
	print("checker.py: could not convert number string into integers")
	exit(-1)

count = len(stack_a)

if count == 3:
	ps.sort_three(stack_a, ops_list)
elif count == 2:
	ps.sort_two(stack_a, ops_list)
else:
	ps.sort_multiple(stack_a, stack_b, ops_list)
'''
elif ps.is_sorted(stack_a) == False:
	while len(stack_a) > 3 and ps.is_sorted(stack_a) == False:
		ps.get_min_and_pb(stack_a, stack_b, ops_list)
	ps.sort_three(stack_a, ops_list)
	while len(stack_b) > 0:
		stack_b.pop(0)
		ops_list.append("pa")
'''

os.system("echo " + " ".join(ops_list) + " > ops")

f.close()

count_string = "Number count: %d \; Ops count: %d \\\n" % (len(numbers_list), len(ops_list))
os.system("echo " + count_string + " > count")
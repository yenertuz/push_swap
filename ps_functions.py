#!/usr/local/bin/python3.7

import statistics

def push_stack(stack_a, stack_b):
	stack_a.insert(0, stack_b.pop(0))

def swap_stack(stack_a):
	if len(stack_a) == 1:
		return
	tmp = stack_a[0]
	stack_a[0] = stack_a[1]
	stack_a[1] = tmp

def rotate_stack(stack_a):
	tmp = stack_a.pop(0)
	stack_a.append(tmp)

def reverse_rotate_stack(stack_a):
	tmp = stack_a.pop()
	stack_a.insert(0, tmp)

def run_command(command, stack_a, stack_b):
	command = command.strip()
	if command == "pa":
		push_stack(stack_a, stack_b)
	if command == "pb":
		push_stack(stack_b, stack_a)
	if command == "sa":
		swap_stack(stack_a)
	if command == "sb":
		swap_stack(stack_b)
	if command == "ss":
		swap_stack(stack_a)
		swap_stack(stack_b)
	if command == "ra":
		rotate_stack(stack_a)
	if command == "rb":
		rotate_stack(stack_b)
	if command == "rr":
		rotate_stack(stack_a)
		rotate_stack(stack_b)
	if command == "rra":
		reverse_rotate_stack(stack_a)
	if command == "rrb":
		reverse_rotate_stack(stack_b)
	if command == "rrr":
		reverse_rotate_stack(stack_a)
		reverse_rotate_stack(stack_b)

def is_sorted(stack):
	count = len(stack)
	index = 0
	while index < count - 1:
		if stack[index + 1] < stack[index]:
			return False
		index += 1
	return True

def sort_two(stack, ops_list):
	if len(stack) != 2:
		return
	if stack[0] > stack[1]:
		tmp = stack[0]
		stack[0] = stack[1]
		stack[1] = tmp
		ops_list.append("sa")

def sort_three(stack, ops_list):
	if len(stack) != 3 or is_sorted(stack):
		return
	elif stack[0] < stack[1] and stack[1] > stack[2] and stack[0] < stack[2]:
		ops_list.append("rra")
		ops_list.append("sa")
	elif stack[0] > stack[1] and stack[2] > stack[0]:
		ops_list.append("sa")
	elif stack[0] < stack[1] and stack[1] > stack[2]:
		ops_list.append("rra")
	elif stack[0] > stack[1] and stack[1] < stack[2]:
		ops_list.append("ra")
	else:
		ops_list.append("sa")
		ops_list.append("rra")

def get_min_and_pb(stack_a, stack_b, ops_list):
	info = get_info(stack_a)
	while info["index"] != 0:
		if info["index"] > len(stack_a) / 2:
			command = "rra"
		else:
			command = "ra"
		run_command(command, stack_a, stack_b)
		ops_list.append(command)
		info = get_info(stack_a)
	run_command("pb", stack_a, stack_b)
	ops_list.append("pb")
	

def get_info(stack):
	info = dict()
	info["min"] = min(stack)
	info["index"] = stack.index(info["min"])
	return info

def push_below_median_to_stack_b(stack_a, stack_b, ops_list, median):
	while stack_a[0] < median:
		ops_list.append("pb")
		run_command("pb", stack_a, stack_b)
	pivot = stack_a[0]
	ops_list.append("ra")
	run_command("ra", stack_a, stack_b)
	while stack_a[0] != pivot:
		if stack_a[0] < median:
			ops_list.append("pb")
			run_command("pb", stack_a, stack_b)
		else:
			ops_list.append("ra")
			run_command("ra", stack_a, stack_b)

def push_above_median_to_stack_b(stack_a, stack_b, ops_list, median):
	while stack_a[0] >= median:
		ops_list.append("pb")
		run_command("pb", stack_a, stack_b)
	pivot = stack_a[0]
	ops_list.append("ra")
	run_command("ra", stack_a, stack_b)
	while stack_a[0] != pivot:
		if stack_a[0] >= median:
			ops_list.append("pb")
			run_command("pb", stack_a, stack_b)
		else:
			ops_list.append("ra")
			run_command("ra", stack_a, stack_b)

def count_ops(index, count):
	front = index
	back = count - index
	return min(front, back)

def find_highest_and_push_to_a(stack_a, stack_b, ops_list):
	mini_index = stack_b.index(min(stack_b))
	maxi_index = stack_b.index(max(stack_b))
	mini_ops = count_ops(mini_index, len(stack_b))
	maxi_ops = count_ops(maxi_index, len(stack_b))
	if mini_ops < maxi_ops:
		is_mini = 1
		target_index = mini_index
	else:
		is_mini = 0
		target_index = maxi_index
	target = stack_b[target_index]
	if target_index < len(stack_b) / 2:
		while stack_b[0] != target:
			run_command("rb", stack_a, stack_b)
			ops_list.append("rb")
	else:
		while stack_b[0] != target:
			run_command("rrb", stack_a, stack_b)
			ops_list.append("rrb")
	ops_list.append("pa")
	run_command("pa", stack_a, stack_b)
	if is_mini == 1:
		run_command("ra", stack_a, stack_b)
		ops_list.append("ra")
	
	

def push_from_stack_b_to_a(stack_a, stack_b, ops_list):
	while len(stack_b) > 1:
		find_highest_and_push_to_a(stack_a, stack_b, ops_list)
	run_command("pa", stack_a, stack_b)
	ops_list.append("pa")

def sort_multiple(stack_a, stack_b, ops_list):
	median = statistics.median(stack_a)
	push_above_median_to_stack_b(stack_a, stack_b, ops_list, median)
	push_from_stack_b_to_a(stack_a, stack_b, ops_list)
	if is_sorted(stack_a) == True:
		return
	push_below_median_to_stack_b(stack_a, stack_b, ops_list, median)
	while is_sorted(stack_a) == False:
		ops_list.append("rra")
		run_command("rra", stack_a, stack_b)
	push_from_stack_b_to_a(stack_a, stack_b, ops_list)
	while is_sorted(stack_a) == False:
		ops_list.append("rra")
		run_command("rra", stack_a, stack_b)
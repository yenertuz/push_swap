#!/usr/local/bin/python3.7

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

def get_info(stack):
	info = dict()
	info["min"] = min(stack)
	info["index"] = stack.index(info["min"])
	return info	
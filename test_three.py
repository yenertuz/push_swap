#!/usr/local/bin/python3.7

import os

f = open("numbers.list", "r")
str = f.read()
f.close()


file_list = str.split("\n")

for x in file_list:
	if len(x) > 1:
		os.system("echo " + x + " > numbers")
		print(x)
		os.system("./push_swap.py")
		os.system("./checker.py")
		os.system("cat ops")
		print("-----")
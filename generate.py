#!/usr/local/bin/python3.7

import sys
import os
import random

a = []
i = 0
limit = int(sys.argv[1])

while i < limit:
	a.append(i)
	i += 1

random.shuffle(a)

s = []

for x in a:
	s.append(str(x))

os.system("echo " + " ".join(s) + " > numbers")
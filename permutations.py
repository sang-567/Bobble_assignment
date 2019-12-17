#!/usr/bin/env python3

# To run this file:
# > python3 permutations.py inputFile
# or:
# > chmod +x permutations.py
# > ./permutations.py inputFile

import sys
import csv
f = open(sys.argv[1])
r = csv.reader(f, delimiter=',', quotechar='\'', skipinitialspace=True)
data = []
for i in r:
    data.append(i)


output = []

def func(i, t):
    if i == len(data):
        output.append(t)
        return

    for s in data[i]:
        func(i+1, t + s)

func(0, '')

print(*output, sep=', ')

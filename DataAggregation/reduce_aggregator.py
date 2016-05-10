#!/usr/bin/python

import sys
import datetime

#map values to float or int if error
def map_float(x):
	try:
		x = float(x)
	except ValueError:
		x = int(x)
	return x

#map values to int or same if error
def map_int(x):
	try:
		x = int(x)
	except ValueError:
		return x
	return x

#dictionary for aggregating over datetime key
aggregates = {}

#map each value of the list in dictionary[k] to its sum
def map_value(key,x):
	try:
		aggregates[key][x] = aggregates[key][x] + values[x]
	except:
		aggregates[key][x] = values[x]
	return aggregates[key][x]

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	
	line = line.strip().split('\t')

	k = line[0]
	v = line[1]
	key=k

	values = map(map_float,v.strip().split(","))

	if key not in aggregates.keys():
		aggregates[key] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(19):
		if i <= 8:
			aggregates[key][i] = values[i]
		else:
			aggregates[key][i] += values[i]			

keylist = sorted(aggregates.keys())
for k in keylist:
	print k, ",".join([str(x) for x in aggregates[k]])
	
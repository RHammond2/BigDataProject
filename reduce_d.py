#!/usr/bin/python

#NOTE: Length 23 = weather

import sys

#key = None
#weather = []
#trips = []
combined={}
#times =[]

lines = sys.stdin
data = []

def mapfloat(x):
	try:
		x = float(x)
	except ValueError:
		x = x
	return x

for line in lines:
	line = line.strip().split("\t")

	k = line[0]
	v = line[1]

	if len(v.strip().split(',')) == 23:
		""" WEATHER """
		combined[k]=[v,0,0,0,0,0,0,0,0,0,0]
	else:
		data.append(line)

for line in data:
	
	#line = line.strip().split("\t",1)

	k = line[0]
	v = line[1]
	v = v.strip().split(',')

	if len(v) != 23:
		""" TRIPS """
		if (combined[k])[1] == 0:
			v = map(mapfloat,v)
			for i,val in zip(range(1,12),v):
				(combined[k])[i] = val
			#(combined[k])[1] = v.strip().split(',')
		else:

			trip_data = v
			trip_data = map(mapfloat,trip_data)

			for i in range(1,10):
				(combined[k])[i] += trip_data[i]


for key in combined:
	print key, combined[key]



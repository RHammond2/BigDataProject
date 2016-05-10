#!/usr/bin/python

import sys

key = None
weather = []
trips = []

for line in sys.stdin:
	components = line.strip().split("\t",1)

	k = components[0]
	v = components[1]

	if key == k:
		if len(v.strip().split(',')) == 23:
			weather.append(v)
		else:
			trips.append(v)

	else:
		if key:
			for w in weather:
				for t in trips:
					print "%s\t%s,%s" %(key,w,t)

			weather = []
			trips = []

		key = k

		if len(v.strip().split(',')) == 23:
			weather.append(v)
		else:
			trips.append(v)
if k == key:
	for w in weather:
		for t in trips:
			print "%s\t%s,%s" %(key,w,t)

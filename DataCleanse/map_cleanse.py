#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	
	line = line.strip().split('\t')

	k = line[0]
	v = line[1]

	v = v.strip().split(',')
	
	# filter the values that are equal to zero that should not be included
	# filter the values that are less than zero that should not be included
	zeros = [v[21],v[22],v[23],v[24]] #long,lat,passenger_count, trip_distance
	lessers = [v[23],v[24],v[25],v[26],v[27],v[28],v[29],v[30],v[31]] #passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount
	for z in zeros:
		try:
			z = float(z)
		except ValueError:
			z = z
	if '0' in zeros:
		continue
	
	i = []
	for l in lessers:
		try:
			l = float(l)
		except ValueError:
			l = l
		if l < 0:
			i .append(0)
		i.append(1)
	if '0' in i:
		continue

	print "%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(k,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14],v[15],v[16],v[17],v[18],v[19],v[20],v[21],v[22],v[23],v[24],v[25],v[26],v[27],v[28],v[29],v[30],v[31])


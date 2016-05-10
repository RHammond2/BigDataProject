#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	
	line = line.strip().split('\t')

	k = line[0]
	v = line[1]

	values = v.strip().split(",")
	
	speed = values[3]
	gust = values[4]
	visibility = values[11]
	temp = values[12]
	dewpoint = values[13]
	PCP01 = values[19]
	PCP06 = values[20]
	PCP24 = values[21]
	snow = values[22]
	passenger_count = values[25]
	trip_distance = values[26]
	fare_amount = values[27]
	extra = values[28]
	mta_tax = values [29]
	tip_amount = values[30]
	tolls_amount = values[31]
	improvement_surcharge = values[32]
	total_amount = values[33]

	print "%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1" \
		%(k, speed,gust,visibility,temp,dewpoint,PCP01,PCP06,PCP24,snow,passenger_count, \
		trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount)

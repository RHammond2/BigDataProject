#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	
	line = line.strip().split('\t')

	k = line[0]

	if 'p_d_status,month' in k:
		continue

	v = line[1]
	
	v = v.strip().split(",")

	#key.month,key,season(key), direction,speed,gust,cloud_ceiling,sky_cover,low_cloud,middle_cloud,high_cloud, 8
	#visibility,temp,dewpoint,sea_level_pressure,altimeter,station_pressure,max_temp,min_temp,PCP01,PCP06,PCP24,PCPXX,snow_depth 13	
	#pickup_longitude,pickup_latitude, 2
	#passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount
	
	speed = v[1]
	gust = v[2]
	visibility = v[9]
	temp = v[10]
	dewpoint = v[11]
	PCP01 = v[17]
	PCP06 = v[18]
	PCP24 = v[19]
	snow = v[20]
	passenger_count = v[23]
	trip_distance = v[24]
	fare_amount = v[25]
	extra = v[26]
	mta_tax = v [27]
	tip_amount = v[28]
	tolls_amount = v[29]
	improvement_surcharge = v[30]
	total_amount = v[31]
	
	print "%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1" \
		%(k, speed,gust,visibility,temp,dewpoint,PCP01,PCP06,PCP24,snow,passenger_count, \
		trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount)
	
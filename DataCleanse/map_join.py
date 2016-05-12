#!/usr/bin/python

import sys
from datetime import datetime, timedelta, date, time
'''
def season(x):
	winter1 = datetime(2015,12,22,0,0)
	nye = datetime(2015,12,31,23,59)
	nyd = datetime(2015,1,1,0,0)
	winter2 = datetime(2015,3,19,23,59)
	spring1 = datetime(2015,3,20,0,0)
	spring2 = datetime(2015,6,20,23,59)
	summer1 = datetime(2015,6,21,0,0)
	summer2 = datetime(2015,9,21,23,59)
	autumn1 = datetime(2015,9,22,0,0)
	autumn2 = datetime(2015,12,21,23,59)
	if (winter1 <= x <= nye) or (nyd <= x <= winter2):
		season = 'Winter'
	elif spring1 <= x <= spring2:
		season = 'Spring'
	elif summer1 <= x <= summer2:
		season = 'Summer'
	elif autumn1 <= x <= autumn2:
		season = 'Autumn'
	return season
'''
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	
	line = line.strip().split(',')

	if 'USAF' in line:
		continue

	if 'VendorID' in line:
		continue
	
	if len(line) == 33:

		for i in range(33):
			line[i] = line[i].replace("*","")
			line[i] = line[i].replace("T","")
			if line[i] == "":
				line[i] = "0.0"

		USAF = line[0]
		WBAN = line[1]
		dateTime = line[2]
		key = datetime(year=int(dateTime[0:4]),month=int(dateTime[4:6]),day=int(dateTime[6:8]),hour=int(dateTime[8:10]),minute=int(dateTime[10:]))
		
		if key.minute != 51:
			continue

		direction = line[3]
		speed = line[4]
		gust = line[5]
		cloud_ceiling = line[6]
		sky_cover = line[7]
		low_cloud = line[8]
		middle_cloud = line[9]
		high_cloud = line[10]
		visibility = line[11]
		mw1 = line[12] #do not need -- removed
		mw2 = line[13] #do not need -- removed
		mw3 = line[14] #do not need -- removed
		mw4 = line[15] #do not need -- removed
		aw1 = line[16] #do not need -- removed
		aw2 = line[16] #do not need -- removed
		aw3 = line[17] #do not need -- removed
		aw4 = line[18] #do not need -- removed
		w = line[19] #do not need -- removed
		temp = line[20]
		dewpoint = line[21]
		sea_level_pressure = line[22]
		altimeter = line[23]
		station_pressure = line[24]
		max_temp = line[25]
		min_temp = line[26]
		PCP01 = line[27]
		PCP06 = line[28]
		PCP24 = line[29]
		PCPXX = line[30]
		snow_depth = line[31]

		print 'p,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' %(key.month,key, direction,speed,gust,cloud_ceiling,sky_cover,low_cloud,middle_cloud,high_cloud,visibility,temp,dewpoint,sea_level_pressure,altimeter,station_pressure,max_temp,min_temp,PCP01,PCP06,PCP24,PCPXX,snow_depth)
		print 'd,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' %(key.month,key, direction,speed,gust,cloud_ceiling,sky_cover,low_cloud,middle_cloud,high_cloud,visibility,temp,dewpoint,sea_level_pressure,altimeter,station_pressure,max_temp,min_temp,PCP01,PCP06,PCP24,PCPXX,snow_depth)
	elif len(line) == 19:
		
		key = []
		value = []
		VendorID = line[0]

		tpep_pickup = datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S')
		key1 = datetime(year=tpep_pickup.year,month=tpep_pickup.month,day=tpep_pickup.day,hour=tpep_pickup.hour,minute=tpep_pickup.minute)
		if key1.minute > 51:
			key1 += timedelta(hours=1)
			key1 = key1.replace(minute = 51)
		else:
			key1 = key1.replace(minute = 51)

		tpep_dropoff = datetime.strptime(line[2], '%Y-%m-%d %H:%M:%S')
		key2 = datetime(year=tpep_dropoff.year,month=tpep_dropoff.month,day=tpep_dropoff.day,hour=tpep_dropoff.hour,minute=tpep_dropoff.minute)
		if key2.minute > 51:
			key2 += timedelta(hours=1)
			key2 = key2.replace(minute = 51)
		else:
			key2 = key2.replace(minute = 51)

		tpep_dropoff = line[2]
		passenger_count = line[3]
		trip_distance = line[4]
		pickup_longitude = line[5]
		pickup_latitude = line[6]
		RatecodeID = line[7]
		store_and_fwd_flag = line[8]
		dropoff_longitude = line[9]
		dropoff_latitude = line[10]
		payment_type = line[11]
		fare_amount = line[12]
		extra = line[13]
		mta_tax = line[14]
		tip_amount = line[15]
		tolls_amount = line[16]
		improvement_surcharge = line[17]
		total_amount = line[18]

		print "p,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(key1.month,key1, pickup_longitude,pickup_latitude,passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount)
		print "d,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(key2.month,key2, dropoff_longitude,dropoff_latitude,passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount)

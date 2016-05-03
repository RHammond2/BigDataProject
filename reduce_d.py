#!/usr/bin/python

#NOTE: Length 23 = weather

import sys
import re
import string


#key = None
#weather = []
#trips = []
combined={}
#times =[]
data = []

def mapfloat(x):
	try:
		x = float(x)
	except ValueError:
		return x	# x = x
	return x

for line in sys.stdin:

	line = line.strip().split("\t",1)

	k = line[0]
	v = line[1]
	#print k

	v=v.strip().split(',')

	if len(v) == 23:
		""" WEATHER """
		#v_string = '%s' %(v)
		#v_string = v_string.translate(string.maketrans('', ''), '[')
		#v_string = v_string.translate(string.maketrans('', ''), ']')
		combined[k]=[v,None]#combined[k]=[v,0,0,0,0,0,0,0,0,0,0]
	else:
		data.append(line)
	#print len()


for line in data:
	

	#line = line.strip().split("\t",1)

	k = line[0]
	v = line[1]

	v = map(mapfloat,v.strip().split(','))

	#if len(v.strip().split(',')) != 23:
	""" TRIPS """
	if (combined[k])[1] == None:
		(combined[k])[1] = v
		#for i,val in zip(range(1,11),v):
				#(combined[k])[i] = val
	else:

		#trip_data = v.strip().split(',')
		#trip_data = map(mapfloat,trip_data)
		trip_data = v

		for i in range(10):
			((combined[k])[1])[i] += float(trip_data[i])


	#print k
print ("year","month","day","hour","minute","USAF","WBAN","direction","speed","gust","cloud_ceiling","sky_cover","low_cloud","middle_cloud","high_cloud","visibility","temp","dewpoint","sea_level_pressure","altimeter","station_pressure","max_temp","min_temp","PCP01","PCP06","PCP24","PCPXX","snow_depth","passenger_count","trip_distance","fare_amount","extra","mta_tax","tip_amount","tolls_amount","improvement_surcharge","total_amount","Count")
for key in combined:

	final = '%s,%s,%s' %(key, combined[key][0],combined[key][1])
	try:
		final = final.translate(string.maketrans('', ''), '[')
	except:
		dummy = 0
	try:
		final = re.sub(']', '',final)
	except:
		dummy = 3

	print final

#print "year,month,day,hour,minute,weather,agg_trips"
#for line in data:
	#print line



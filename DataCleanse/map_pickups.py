#!/usr/bin/python

import sys
from datetime import datetime, timedelta, date, time

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

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)

		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in xrange(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)

		self.bound = (minx,miny,maxx,maxy)

	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]
			
			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)

			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c

	def bounds(self):
		return self.bound

#Manhattan and bronx coordiantes
manbro=Polygon([Point(40.914299, -73.909715), Point(40.749086, -74.008936), Point(40.719169, -74.012026), Point(40.702513, -74.015459), Point(40.708759, -74.001383), Point(40.710841, -73.989710), Point(40.711622, -73.978037), Point(40.729316, -73.972200), Point(40.736340, -73.975977), Point(40.744404, -73.972200), Point(40.777430, -73.943018), Point(40.783669, -73.944391), Point(40.796666, -73.930658),
Point(40.801814,-73.924958), Point(40.785273, -73.935154), Point(40.794831, -73.915247), Point(40.807695, -73.897768), Point(40.803652, -73.883202), Point(40.806225, -73.868636), Point(40.817616, -73.798720), Point(40.843333, -73.817170), Point(40.886661, -73.822025), Point(40.849944, -73.801147), Point(40.878585, -73.786581), Point(40.890331, -73.822511), Point(40.914299, -73.909715)])

#Brooklyn and queens
brooque=Polygon([Point(40.576871, -74.010411), Point(40.578346, -73.933697), Point(40.588671, -73.910877), Point(40.588671, -73.900681), Point(40.579083, -73.894855), Point(40.585721, -73.878347), Point(40.604155,-73.885144), Point(40.624058, -73.896312), Point(40.654638, -73.856983), Point(40.652059, -73.823967), Point(40.629954, -73.781241), Point(40.605998, -73.803089), Point(40.628111, -73.776385),
Point(40.613738, -73.769588), Point(40.554371, -73.940009), Point(40.546624, -73.938553), Point(40.597150, -73.740456), Point(40.625532, -73.769588), Point(40.649849, -73.740456), Point(40.656479, -73.726861), Point(40.723851, -73.733658), Point(40.735993, -73.705498), Point(40.752546, -73.703555), Point(40.780494, -73.751623), Point(40.765418, -73.755993), Point(40.790787, -73.784154), Point(40.793361, -73.850186), Point(40.789685, -73.909421), Point(40.740775, -73.958945), Point(40.700297, -73.973511), Point(40.680049, -74.016723), Point(40.668633, -73.999244), Point(40.617055, -74.039543), Point(40.595307, -74.00215)])

#Staten Island
stis=Polygon([Point(40.499385, -74.245142), Point(40.513481, -74.25132), Point(40.519223, -74.243082), Point(40.545317, -74.245828), Point(40.556274, -74.213556), Point(40.616763, -74.194330), Point(40.632397, -74.199136), Point(40.643860, -74.176477), Point(40.637608, -74.153818), Point(40.647507, -74.081720), Point(40.626144, -74.074167), Point(40.602167, -74.055628), Point(40.549491, -74.131845), Point(40.516091, -74.201196), Point(40.499385, -74.245142)])

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

		print '%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' %(key.month,key,season(key), USAF,WBAN,direction,speed,gust,cloud_ceiling,sky_cover,low_cloud,middle_cloud,high_cloud,visibility,temp,dewpoint,sea_level_pressure,altimeter,station_pressure,max_temp,min_temp,PCP01,PCP06,PCP24,PCPXX,snow_depth)
	elif len(line) == 19:
		
		key = []
		value = []
		VendorID = line[0]
		tpep_pickup = datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S')
		key = datetime(year=tpep_pickup.year,month=tpep_pickup.month,day=tpep_pickup.day,hour=tpep_pickup.hour,minute=tpep_pickup.minute)
		
		if key.minute > 51:
			key += timedelta(hours=1)
			key = key.replace(minute = 51)
		else:
			key = key.replace(minute = 51)

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

		# filter the values that are equal to zero that should not be included
		# filter the values that are less than zero that should not be included
		zeros = [pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude]
		lessers = [passenger_count,trip_distance,fare_amount,extra,mta_tax,tolls_amount,improvement_surcharge,total_amount]
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
			if l <= "0":
				i .append(0)
			i.append(1)
		if '0' in i:
			continue

		#check if the pickup location is in NYC
		try:
			pickup_latitude = float(pickup_latitude)
		except ValueError:
			pickup_latitude = pickup_latitude
		try:
			pickup_longitude = float(pickup_longitude)
		except ValueError:
			pickup_longitude = pickup_longitude
		pt=Point(pickup_latitude, pickup_longitude)
		
		if((manbro.contains(pt) or brooque.contains(pt) or stis.contains(pt))):
			pass
		else:
			continue

		print "%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(key.month,key,season(key), pickup_longitude,pickup_latitude,passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount)
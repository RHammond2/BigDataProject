#!/usr/bin/python

import sys

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
	
	line = line.strip().split('\t')

	k = line[0]
	v = line[1]
	
	v = v.strip().split(',')
	
	#check if the pickup location is in NYC
	try:
		latitude = float(v[22])
	except ValueError:
		latitude = v[22]
	try:
		longitude = float(v[21])
	except ValueError:
		longitude = v[21]
	point=Point(latitude, longitude)
	
	if((manbro.contains(point) or brooque.contains(point) or stis.contains(point))):
		pass
	else:
		continue
	
	print "%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(k,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14],v[15],v[16],v[17],v[18],v[19],v[20],v[21],v[22],v[23],v[24],v[25],v[26],v[27],v[28],v[29],v[30],v[31])
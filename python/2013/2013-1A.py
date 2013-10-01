#!/usr/bin/python

from __future__ import division

for case in range(1,int(raw_input())+1):          #For all test cases
	data = raw_input().split(" ")                  #Get the case size (unused)
	#1cm radii circle = pi*radii^2 cm2 area = 1ml paint
	radius = int(data[0])
	paint_ml = float(data[1])

	rings = 1

	total_ml = ((2*radius)-(2*rings)-1)

	while paint_ml >= total_ml:
		rings+=1
		total_ml = ((2*radius)-(2*rings)-1)
		print paint_ml,total_ml

	print "Case #%d: %d" % (case, rings)


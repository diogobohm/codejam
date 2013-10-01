#!/usr/bin/env python

from heapq import *
from datetime import *

for case in range(1,int(raw_input())+1):           #For all test cases

	T = timedelta(0,0,0,0,int(raw_input()))
	sizes = raw_input().split(" ")
	tripsa, tripsb = int(sizes[0]), int(sizes[1])
	trips = []
	for trip in range(tripsa+tripsb):
		times = raw_input().split(" ")
		trips.append([datetime.strptime(times[0], "%H:%M"), datetime.strptime(times[1], "%H:%M"), 0 if trip<tripsa else 1])

	trips.sort()

	start = [0, 0]
	trains = [[], []]

	for trip in trips:
		d = trip[2]
		if trains[d] and trains[d][0] <= trip[0]:
			# We're using the earliest train available, and
			# we have to delete it from this station's trains.
			heappop(trains[d])
		else:
			# No train was available for the current trip,
			# so we're adding one.
			start[d] += 1
		# We add an available train in the arriving station at the
		# time of arrival plus the turnaround time.
		heappush(trains[1 - d], trip[1] + T)

	print "Case #%d: %d %d" % (case, start[0], start[1])

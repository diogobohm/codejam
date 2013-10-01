#!/usr/bin/env python

from datetime import *

def travel(turnaround, current, trips_a, trips_b, route, routeList):
	route.add(current)
	endpoint = True

	if current.isA:
		for trip in trips_b:
			if (current.arrival+turnaround <= trip.departure):
				new_trips_b = trips_b[:]
				new_trips_b.remove(trip)
				travel(turnaround, trip, trips_a[:], new_trips_b, route, routeList)
				endpoint = False
	else:
		for trip in trips_a:
			if (current.arrival+turnaround <= trip.departure):
				new_trips_a = trips_a[:]
				new_trips_a.remove(trip)
				travel(turnaround, trip, new_trips_a, trips_b[:], route, routeList)
				endpoint = False

	if endpoint and routeList.count(route) == 0:
		routeList.append(route)

class Trip:
	def __init__(self, isA, departure, arrival):
		self.isA = isA
		self.departure = departure
		self.arrival = arrival

	def __repr__(self):
		return "%s - %s %s" % ("A" if self.isA else "B", self.departure.strftime("%H:%M"), self.arrival.strftime("%H:%M"))

for case in range(1,int(raw_input())+1):
	turnaround = timedelta(0,0,0,0,int(raw_input()))
	sizes = raw_input().split(" ")
	size_a = int(sizes[0])
	size_b = int(sizes[1])

	trips_a = []
	trips_b = []

	for i in range(size_a):
		trip = raw_input().split(" ")
		trips_a.append(Trip(True, datetime.strptime(trip[0], "%H:%M"), datetime.strptime(trip[1], "%H:%M")))

	for i in range(size_b):
		trip = raw_input().split(" ")
		trips_b.append(Trip(False, datetime.strptime(trip[0], "%H:%M"), datetime.strptime(trip[1], "%H:%M")))

	trains_a = 0
	trains_b = 0

	routes_from_a = []
	for trip in trips_a:
		new_trips_a = trips_a[:]
		new_trips_a.remove(trip)
		travel(turnaround, trip, new_trips_a, trips_b[:], set([]), routes_from_a)

	routes_from_b = []
	for trip in trips_b:
		new_trips_b = trips_b[:]
		new_trips_b.remove(trip)
		travel(turnaround, trip, trips_a[:], new_trips_b, set([]), routes_from_b)

	'''
	print "A routes"
	print routes_from_a

	print "B routes"
	print routes_from_b
	'''

	final_a_routes = routes_from_a[:]
	final_b_routes = routes_from_b[:]
	for route_a in routes_from_a:
		for route_b in routes_from_b:
			if route_a.issubset(route_b):
				if final_a_routes.count(route_a) > 0:
					final_a_routes.remove(route_a)
			elif route_b.issubset(route_a):
				if final_b_routes.count(route_b) > 0:
					final_b_routes.remove(route_b)
	'''
	print "A routes"
	print final_a_routes

	print "B routes"
	print final_b_routes
	'''
	print "Case #%d: %d %d" % (case, len(final_a_routes), len(final_b_routes))

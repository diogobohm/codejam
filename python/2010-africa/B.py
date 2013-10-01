#!/usr/bin/env python

for case in range(1,int(raw_input())+1):                  # For all test cases
	town_len, office = map(int, raw_input().split(" "))   # Get amount of towns and office

	carriers = [[] for x in xrange(town_len)]             # Create new lists for every town
	capacities = town_len * [0]                           # Initialize "capacity of transportation"
	payload = town_len * [0]                              # Initialize "cargo" for each town

	for i in range(int(raw_input())):                     # Get and go through employee list
		town, capacity = map(int, raw_input().split(" ")) # Get the current employee info
		if town == office:                                # If employee is from office town
			continue                                      #   No need to commute, ignore

		town -= 1                                         # Adjust "town" to zero-based index
		payload[town] += 1                                # Employee needs to commute, count

		if capacity != 0:                                 # If employee has a car
			capacities[town] += capacity                  # Add to our capacities for the town
			carriers[town].append(capacity)               # Append its car capacity

	resultStr = ""                                        # Create our result string

	for i in range(town_len):                             # For all towns
		if capacities[i] < payload[i]:                    # If we can't carry everyone
			resultStr = "IMPOSSIBLE "                     #   declare it impossible, give up
			break;

		cars = 0                                          # We can carry, start with 0 cars
		carriers[i].sort()                                # Sort and reverse the car list
		carriers[i].reverse()
		for car in carriers[i]:                           # So we can start from the bigger ones
			if (payload[i] <= 0):                         # If we're carrying everybody already
				break                                     #  we're done for this town

			payload[i] -= car                             # Else, fill a car, report as being used
			cars += 1

		resultStr += str(cars)+" "                        # Add this town filled vehicles

	print "Case #%d: %s" % (case, resultStr[:-1])         # Report results, remove last space

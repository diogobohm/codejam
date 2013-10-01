#!/usr/bin/python

for case in range(1,int(raw_input())+1):          #For all test cases
	size = int(raw_input())                   #Get the case size (unused)
	vector = []

	for i in raw_input().split(" "):          #Split the case values by spaces
		vector.append(float(i))           #Store its values as floats

	for i in range(1,len(vector)-1):          #From second to second-to-last
		med = (vector[i-1]+vector[i+1])/2 #Get average from neighboors
		if vector[i] > med:               #Am I bigger?
			vector[i] = med           #Then average I am

	print "Case #%d: %.6f" % (case, vector[-2])


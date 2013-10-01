#!/usr/bin/python

for case in range(1,int(raw_input())+1):                #For all test cases
	size = int(raw_input())                         #Get the case size
	heights = []
	paths = []

	for i in raw_input().split(" "):                #Split the case values by spaces
		heights.append(int(i))                  #Store its values as integers

	paths.append([heights[0]])                      #Starts first list with first value
	for i in range(1, size):                        #Iterate from second member on
		for path in paths:                      #For evety path
			if heights[i] > max(path):      #Is the current height bigger than my maximum?
				path.append(heights[i]) #Append its value, so it will be crescent
			else:
				path.append(0)          #Else, ignore it

		paths.append(heights[:i+1])             #Create a new path with the heights so far
		cur_num = paths[-1][-1]                 #Get the current height

		for j in reversed(range(0, i)):         #Iterate down to the first height
			if cur_num > heights[j]:        #If the next value is smaller, keep it
				cur_num = heights[j]
			else:
				paths[-1][j] = 0        #If it's not smaller, ignore it

	min_houses = size
	for path in paths:
		min_houses = min(min_houses, path.count(0)) #Get the path with least ignored members

	print "Case #%d: %d" % (case, min_houses)

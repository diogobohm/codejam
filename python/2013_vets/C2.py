#!/usr/bin/python

for case in range(1,int(raw_input())+1):                               #For all test cases
	size = int(raw_input())                                        #Get the case size
	heights = []
	pointers = [0] * size                                          #Create the pointer list
	length = 0                                                     #Sequence length

	for i in raw_input().split(" "):                               #Split the case values by spaces
		heights.append(int(i))                                 #Store its values as integers

	for i in range(size):                                          #For all the sequence
		j = 0
		for k in range(length+1):                              #For all the sequence until the current length
			if heights[pointers[k]] < heights[i]:          #Compare the values on pointers to the current value
				j = max(j, k)                          #Get the maximum value index

		if j == length or heights[i] < heights[pointers[j+1]]: #If the value is a "keeper"
			if j < size-1:
				pointers[j+1] = i                      #Keeps its index
			length = max(length, j+1)                      #Update the length

	print "Case #%d: %d" % (case, size-length)

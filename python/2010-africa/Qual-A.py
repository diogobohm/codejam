#!/usr/bin/env python

for case in range(1,int(raw_input())+1):      # For all test cases

	credit = int(raw_input())                 # Get the test's credit
	raw_input()                               # Discard the number of items
	strItems = raw_input().split(" ")         # Get the items as strings
	items = []
	for item in strItems:
		items.append(int(item))               # Convert the items to integers

	out = False
	i = 0
	j = i+1
	for i in range(0,len(items)-1):           # first item can be any of the items, but the last
		for j in range(i+1,len(items)):       # the second will be any of the items after the first
			if items[i] + items[j] == credit:
				out = True                    # Found, get out
				break
		if out: break


	print "Case #%d: %d %d" % (case, i+1, j+1)# Reports results

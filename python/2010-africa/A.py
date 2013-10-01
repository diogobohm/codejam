#!/usr/bin/env python

for case in range(1,int(raw_input())+1):        # For all test cases
	raw_input()                                 # Discard the guest list size
	guests = raw_input().split(" ")             # Get the list of guest IDs

	guestList = []                              # Create an empty guest list

	for guest in guests:                        # For all guests
		if guestList.count(guest) > 0:          # If it's already on the final list
			guestList.remove(guest)             #    if is a couple, remove
		else:                                   # If it's not in the list yet
			guestList.append(guest)             #    Add its ID

	print "Case #%d: %s" % (case, guestList[0]) # Reports results

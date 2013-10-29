#!/usr/bin/python

from __future__ import division
import math

for case in range(1,int(raw_input())+1): # For all test cases
	size = int(raw_input())              # Since we're informed, save array size
	x = map(int, raw_input().split(" ")) # Get all X parameters
	y = map(int, raw_input().split(" ")) # Get all Y parameters

	x.sort()                             # Sort both vectors
	y.sort()                             # And sort-reverse Y
	y.reverse()                          # So we can match the bigger/smaller values

	msp = 0
	for i in range(size):                # For all the array's len
		msp += x[i]*y[i]                 # Sum "forward" on X and "backwards" on Y

	print "Case #%d: %d" % (case, msp)   # Print the sum

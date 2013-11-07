#!/usr/bin/env python

from decimal import *                              # Improved math

getcontext().prec = 1024                           # Adjust the precision
base = (Decimal(3) + Decimal(5).sqrt())            # Calculate the base

for case in range(1,int(raw_input())+1):           # For all test cases
	exp = (int(raw_input()) - 3) % 100 + 3         # Get the recurrent exponent

	num = str(base ** Decimal(exp))                # Calculate
	ans = num[:num.find('.')]                      # Get only the integer part

	print "Case #%d: %03d" % (case, int(ans[-3:])) # Zero-lead the last 3 digits

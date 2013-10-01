#!/usr/bin/env python

from mpmath import *


mp.dps = 100
calc = mpf('5.2360679775')


for case in range(1,int(raw_input())+1):
	number = ((calc**mpf(raw_input())) % 1000)
	print "Case #%d: %03d" % (case, number)

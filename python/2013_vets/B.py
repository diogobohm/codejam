#!/usr/bin/python

from __future__ import division                            #Get python3 revised division operator

def asInches(strFeetInches):                               #Function converting Foot/inches string to inches
	nums = strFeetInches[:-1].split("\'")              #Split string on ' and remove " marks
	return int(nums[0])*12 + int(nums[1])              #1 foot = 12 inches, convert

for case in range(1,int(raw_input())+1):                   #For all test cases
	vector = []
	boy = False
	father = -1
	mother = -1

	for i in raw_input().split(" "):                   #Split the case values by spaces
		if i == "B":                               #Is it a boy?
			boy = True                         
		elif i == "G":                             #Is it a girl?
			boy = False                        
		elif father == -1:                         #If father is not yet known, get it
			father = asInches(i)               #Store his height in inches
		else:                                      #Father is known, so get mother this time
			mother = asInches(i)               #Store in inches

	height = (mother + father + (5 if boy else -5))/2  #Baby height math
	inc = 4.0                                          #Range default value

	lower = height-inc                                 #Get lower range
	if lower != int(lower):                            #If number is a fraction
		lower += 0.5                               #Reduce range size

	higher = height+inc                                #Get higher range
	if higher != int(higher):                          #If number is a fraction
		higher -= 0.5                              #Reduce range size

	print "Case #%d: %1d'%1d\" to %1d'%1d\"" % (case, lower/12, lower%12, higher/12, higher%12)

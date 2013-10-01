#!/usr/bin/env python

for case in range(1,int(raw_input())+1):           # For all test cases
	words = raw_input().split(" ")                 # Get the list of words
	words.reverse()                                # Reverse word list
	print "Case #%d: %s" % (case, " ".join(words)) # Reports results, add spaces

#!/usr/bin/env python

# Build a map with the number to write and its repetition count
t9 = {
		"a" : ["2", 1], "b" : ["2", 2], "c": ["2", 3],
		"d" : ["3", 1], "e" : ["3", 2], "f": ["3", 3],
		"g" : ["4", 1], "h" : ["4", 2], "i": ["4", 3],
		"j" : ["5", 1], "k" : ["5", 2], "l": ["5", 3],
		"m" : ["6", 1], "n" : ["6", 2], "o": ["6", 3],
		"p" : ["7", 1], "q" : ["7", 2], "r": ["7", 3], "s": ["7", 4],
		"t" : ["8", 1], "u" : ["8", 2], "v": ["8", 3],
		"w" : ["9", 1], "x" : ["9", 2], "y": ["9", 3], "z": ["9", 4],
		" " : ["0", 1],
}

for case in range(1,int(raw_input())+1): # For all test cases
	message = raw_input()                # Get the list of words

	attr = t9[message[0]]                # Start with the first character
	t9str = attr[0]*attr[1]              # Initialize t9str with first T9 "word"

	for i in range(1,len(message)):      # From the second character on
		attr = t9[message[i]]            # Get the map values
		if t9str[-1] == attr[0]:         # If it's the same number as the last
			t9str += " "                 # Add a space

		t9str = t9str+attr[0]*attr[1]    # Append the new T9 "word"

	print "Case #%d: %s" % (case, t9str) # Reports results

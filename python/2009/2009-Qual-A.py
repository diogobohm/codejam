#!/usr/bin/python

import re, string, sys

from array import *

ST_HEADER=1
ST_WORDS=2
ST_PATTERNS=3
ST_EXIT=4

state =ST_HEADER 
cases = 0
casen = 1
wordnum = 0
wordlen = 0

words = list()
patterns = list()


while state != ST_EXIT :
	line = raw_input()

	if state == ST_HEADER:
		header = line.split(" ")
		wordlen = int(header[0])
		wordnum = int(header[1])
		cases = int(header[2])

		state = ST_WORDS
	elif state == ST_WORDS:
		words.append(line)
		if len(words) == wordnum:
			state = ST_PATTERNS

	elif state == ST_PATTERNS:
		expr = ""
		insor = False
		justin = False

		for i in range(len(line)):
			if line[i] == '(':
				expr += '('
				insor = True
				justin = True
			elif line[i] == ')':
				expr += ')'
				insor = False
				justin = False
			else:
				if insor == True:
					if justin != True:
						expr += '|'
					justin = False
				
				expr += line[i]

		p = re.compile(expr)	
		matches = 0

		for i in words:
			if p.match(i) != None:
				matches+=1

		print "Case #%d: %d" % (casen,matches)
		casen+=1

		if casen-1 == cases:
			state = ST_EXIT
	else:
		state = ST_EXIT
	
exit()
"""

Input

The first line of input contains 3 integers, L, D and N separated by a space. D lines follow, each containing one word of length L. These are the words that are known to exist in the alien language. N test cases then follow, each on its own line and each consisting of a pattern as described above. You may assume that all known words provided are unique.

Output

For each test case, output

Case #X: K
where X is the test case number, starting from 1, and K indicates how many words in the alien language match the pattern.

Example: 

Input 
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

Output
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0

"""

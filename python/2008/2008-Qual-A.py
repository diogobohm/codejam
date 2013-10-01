#!/usr/bin/env python

for case in range(1,int(raw_input())+1):           #For all test cases
	size = int(raw_input())                        #Get the case searches size
	engines = []
	for engine in range(size):
		engines.append(raw_input())

	size_searches = int(raw_input())
	searches = []
	remaining_engines = engines[:]
	changes = 0
	for search in range(size_searches):
		cur_search = raw_input()
		if remaining_engines.count(cur_search) > 0:
			remaining_engines.remove(cur_search)
			if len(remaining_engines) == 0:
				changes+=1
				remaining_engines = engines[:]
				remaining_engines.remove(cur_search)

	print "Case #%d: %d" % (case, changes)

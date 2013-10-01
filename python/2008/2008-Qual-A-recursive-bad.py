#!/usr/bin/env python

def recursive_search(engines, cur_engine, searches_left, changes):
	must_change = cur_engine == searches_left[0]
	if must_change == True:
		changes += 1

	if len(searches_left) == 1:
		return changes

	new_searches = searches_left[1:]
	if must_change == True:
		best_scenario = len(engines)
		for engine in engines:
			if cur_engine != engine:
				best_scenario = min(best_scenario, recursive_search(engines, engine, new_searches, changes))

		return best_scenario
	else:
		return recursive_search(engines, cur_engine, new_searches, changes)


for case in range(1,int(raw_input())+1):           #For all test cases
	size = int(raw_input())                        #Get the case searches size
	engines = []
	for engine in range(size):
		engines.append(raw_input())

	size_searches = int(raw_input())
	searches = []
	for search in range(size_searches):
		searches.append(raw_input())

	if (size_searches < 2): #Will always have at least 2 search engines
		print "Case #%d: 0" % (case)
		continue

	best_scenario = len(engines)
	for engine in engines:
		best_scenario = min(best_scenario, recursive_search(engines, engine, searches, 0))

	print "Case #%d: %d" % (case, best_scenario)

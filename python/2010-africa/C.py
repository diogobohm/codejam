#!/usr/bin/env python

for case in range(1,int(raw_input())+1):          # For all test cases
	info = map(int, raw_input().split(" "))       # Get test case information
	problems = info[0]                            # Fetch number of problems
	needed = info[1]                              # Fetch number of needed problems to pass
	results = info[2:]                            # Fetch results for each problem

	qualified = 0                                 # Initialize our results

	if (problems == needed):                      # For this case, we can expect
		results.sort()                            # as many contestants as the
		qualified = results[len(results)-needed]  # least solved problem

	else:                                         # For this case, we use a solution
		out = False                               # similar to the winning one
		while not out:
			out = True
			qualified = sum(results)/needed       # Reduce the number of possible qualifiers
			for i in range(len(results)):         # And for all results
				if results[i] > qualified:        # Limit their values to the current qualifiers
					results[i] = qualified
					out = False                   # Until they all "match" the qualifiers number

	print "Case #%d: %s" % (case, str(qualified)) # Report results

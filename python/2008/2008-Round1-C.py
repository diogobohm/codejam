#!/usr/bin/env python

from bigfloat import *

index = []
countIndex = 0
i = 1
value = 3+sqrt(5)
while countIndex < 5:
	newIndex = BigFloat.exact(value**i)
	'''
	if index.count(newIndex) > 0 and newIndex == index[countIndex]:
		countIndex+=1
	else:
		countIndex = 0

	'''
	index.append(newIndex)
	i += 1
	print i,str(index[-1])
	if i > 110:
		break;

exit(1)

for case in range(1,int(raw_input())+1):
	num = int(raw_input())
	result = index[num%len(index)]

	print "Case #%d: %03d" % (case, result)

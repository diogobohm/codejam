#!/usr/bin/env python

def scalar_p(a, b):
	scalar = 0
	for i in range(len(a)):
		scalar += a[i]*b[i]
	return scalar

for case in range(1,int(raw_input())+1):
	length = int(raw_input())

	a = []
	b = []
	prod = []

	a_str = raw_input().split(" ")
	b_str = raw_input().split(" ")
	for i in range(length):
		a.append(int(a_str[i]))
		b.append(int(b_str[i]))
		prod.apend(a[-1]*b[-1])

	cur_scalar = scalar_p(a,b)

	a_sorted = sorted(a)
	b_sorted = sorted(b)

	
	scalar = min(cur_scalar,scalar_p(a,b))
	print "Case #%d: %d" % (case, scalar)

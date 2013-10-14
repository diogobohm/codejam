#!/usr/bin/python

from __future__ import division

def treeGenerator(n, A, B, C, D, x0, y0, M):
	treeList = []
	X = x0
	Y = y0
	treeList.append([X, Y])
	for i in range(1,n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		treeList.append([X, Y])

	return treeList

for case in range(1,int(raw_input())+1):           #For all test cases
	n, A, B, C, D, x0, y0, M = map(int, raw_input().split(" "))
	triangles = 0
	pastTriangles = []

	treeList = treeGenerator(n, A, B, C, D, x0, y0, M)

	for x1 in treeList:
		treeListX2 = treeList[:]
		treeListX2.remove(x1)
		for x2 in treeListX2:
			treeListX3 = treeListX2[:]
			treeListX3.remove(x2)
			for x3 in treeListX3:
				curTri = {treeList.index(x1), treeList.index(x2), treeList.index(x3)}
				if pastTriangles.count(curTri) == 0:
					pastTriangles.append(curTri)
					treeListXC = treeListX3[:]
					treeListXC.remove(x3)
					if (x1[0] + x2[0] + x3[0]) % 3  == 0 and (x1[1] + x2[1] + x3[1]) % 3 == 0:
						triangles += 1

	print "Case #%d: %d" % (case, triangles)


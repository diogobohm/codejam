#!/usr/bin/python

from numpy import *
from array import *

alphabet = "abcdefghijklmnopqrstuvwxyz"
cur_basin = 0
ma = [['a']]

"""
N W E S
"""

def rec( m, ma, h, w, l, a, cur_basin):
    lv = 65535
    lh = 0
    lw = 0

    if (l != 0):
        if (m[l-1][a] < lv):
            lh = l-1
            lw = a
            lv = m[lh][lw]
    if (a != 0):
        if (m[l][a-1] < lv):
            lh = l
            lw = a-1
            lv = m[lh][lw]
    if (a != w-1):
        if (m[l][a+1] < lv):
            lh = l
            lw = a+1
            lv = m[lh][lw]
    if (l != h-1):
        if (m[l+1][a] < lv):
            lh = l+1
            lw = a
            lv = m[lh][lw]


    if ma[l][a] < 'a':
        if lv >= m[l][a]:
            cur_basin+=1
            ma[l][a] = alphabet[cur_basin]

        else:
            if ma[lh][lw] >= 'a':
                ma[l][a] = ma[lh][lw]

            else:
                cur_basin+=1
                ma[l][a] = alphabet[cur_basin]
                ma[lh][lw] = ma[l][a]
    else:
        if lv > m[l][a]:
            if (l != h-1):
                ma,cur_basin = rec(m, ma, h, w, l+1, a, cur_basin)
            elif (a != w-1):
                ma,cur_basin = rec(m, ma, h, w, l, a+1, cur_basin)
            elif (a != 0):
                ma,cur_basin = rec(m, ma, h, w, l, a-1, cur_basin)
            elif (l != 0):
                ma,cur_basin = rec(m, ma, h, w, l-1, a, cur_basin)
            
        elif lv < m[l][a]:
            if ma[lh][lw] < 'a':
                ma[lh][lw] = ma[l][a]

    return ma,cur_basin

line = raw_input()

cases = int(line)

for i in range(cases):
    header =  str.split(raw_input())
    h = int(header[0])
    w = int(header[1])

    m = zeros((h,w))
    ma = [['a']]

    cur_basin = 0
    maxh= 0

    for l in range(h):
        mapline = str.split(raw_input())
        ma.append(mapline)
        if l == 0:
            ma.pop(0)
        for a in range(len(mapline)):
            m[l][a] = int(mapline[a])
            maxh = max(maxh,m[l][a])

    ma[0][0] = alphabet[cur_basin]

    for l in range(h):
        for a in range(w):
            ma,cur_basin = rec(m, ma, h, w, l, a, cur_basin)

    print "Case #%d:" % int(i+1)
    for l in range(h):
        for a in range(w):
            if a < w-1:
                print "%c" % ma[l][a],
            else:
                print "%c" % ma[l][a]

exit()


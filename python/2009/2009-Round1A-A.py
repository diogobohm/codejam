#!/usr/bin/python

#Create an 11x1000 array
index = [[-1]*1000] * 11

def baseN(base, num, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // base, base, numerals).lstrip(numerals[0]) + numerals[num % base])

def getNext(base, num):
	ret = 0
	while (num > 0):
		ret += (num % base) * (num % base)
		num /= base

	return ret;

def isHappy(base, num):
	if index[base][num] > -1:
		return index[base][num] == 1

	index[base][num] = 0
	nextNum = getNext(base, num)
	print base, num, nextNum

	if nextNum == 1:
		index[base][nextNum]=1
		return True

	elif nextNum == 0:
		index[base][nextNum]=0
		return False

	if isHappy(base, nextNum):
		index[base][num] = 1

	return index[base][num] == 1

def buildIndex():
	for base in range(2, len(index)):
		for number in range(len(index[0])):
			isHappy(base, number)

buildIndex()
print len(index), len(index[0]), index[0]
print index[2][3],index[2][143]

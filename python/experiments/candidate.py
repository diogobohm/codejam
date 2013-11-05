#!/usr/bin/env python

def soma(num1, num2):
	n1 = num1
	n2 = num2
	if len(n1) < len(n2):
		n1 = ((len(n2)-len(n1))*"0") + n1
	elif len(n1) > len(n2):
		n2 = ((len(n1)-len(n2))*"0") + n2

	#print "%s + %s" % (n1, n2)

	n1 = list(n1)
	n1.reverse()
	n2 = list(n2)
	n2.reverse()

	#print n1
	#print n2

	carry = (len(n1)+1) * [0]
	ret = (len(n1)+1) * [0]
	for i in range(len(n2)):
		n = int(n1[i]) + int(n2[i])
		ret[i] = (n + carry[i])  % 10
		carry[i+1] += (n + carry[i]) // 10

	ret[i+1] = carry[i+1]
	ret.reverse()
	#print carry
	#print ret

	r = ""
	leading = True
	for number in ret:
		if number == 0 and leading:
			continue
		else:
			leading = False
			r += str(number)

	#return str(int(num1) + int(num2))
	return r

def mult(num1, num2):
	finalCommaPos = 0
	if num1.count(',') > 0:
		finalCommaPos += len(num1)-1 - num1.find(',')
		num1 = num1.replace(',', '')
	if num2.count(',') > 0:
		finalCommaPos += len(num2)-1 - num2.find(',')
		num2 = num2.replace(',', '')

	results = []

	countO = 0
	for i in range(len(num2)-1, -1, -1):
		resInt = []

		countI = 0
		for j in range(len(num1)-1, -1, -1):
			mult = int(num1[j]) * int(num2[i])
			#print "%d * %d = %d" % (int(num1[j]), int(num2[i]), mult)
			resInt.insert(0, str(mult)+(countI*"0"))
			countI += 1

		#print "Res %d: %s" % (i, str(resInt))
		resI = "0"
		for resultI in resInt:
			resI = soma(resI, resultI)

		for j in range(countO):
			resI = resI+"0"
		countO += 1

		results.append(resI)

	#print results
	ret = "0"
	for result in results:
		ret = soma(ret, result)

	if finalCommaPos > 0:
		ret = ret[:-finalCommaPos]+','+ret[-finalCommaPos:]

	return ret


#print mult("123,45","9876")
#print soma("999","9991")
#exit()

index = ["0"]

for case in range(1,int(raw_input())+1):
	exp = int(raw_input())

	num = "1"
	for i in range(1,exp+1,1):
		if len(index) <= i:
			index.append(mult(num, "5,236067977"))
		num = index[i]

	ans = num[:num.find(',')]
	ans = ans[-3:]
	ans = (3-len(ans))*"0" + ans
	print index

	print "Case #%d: %s" % (case, ans)


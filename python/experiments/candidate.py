#!/usr/bin/env python

def mult(num1, num2):
	finalCommaPos = 0
	if num1.count(',') > 0:
		finalCommaPos += len(num1)-1 - num1.find(',')
		num1 = num1.replace(',', '')
	if num2.count(',') > 0:
		finalCommaPos += len(num2)-1 - num2.find(',')
		num2 = num2.replace(',', '')

	ret = str(int(num1) * int(num2))
	if finalCommaPos > 0:
		ret = ret[:-finalCommaPos]+','+ret[-finalCommaPos:]
	return ret

index = ["0"]
def exp(num, expo):
	ret = num
	limit = int(expo)
	i = 1
	while i < limit:
		if len(index) <= i:
			index.append(mult(ret, num))
		ret = index[i]
		i += 1

	#print index

	return ret

sqrt = "5,23606797749978969640917366873127623544023934501328345221035248001151932202514279802475771763425882454612292349338531494140625"

for case in range(1,int(raw_input())+1):

	num = exp(sqrt, raw_input())
	ans = num[:num.find(',')]

	print "Case #%d: %03d" % (case, int(ans[-3:]))


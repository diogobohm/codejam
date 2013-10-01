#!/usr/bin/env python

NOT_SURE = 2
TRUE = 1
FALSE = 0

class Expression():
	def __init__(self):
		self.conditions = []

	def saysIsDifFrom(self, origin, different, fr):
		self.conditions.append(str(origin)+'?'+str(different)+'!'+str(fr)+':'+str(different)+'='+str(fr))

	def saysIsEqTo(self, origin, equals, to):
		self.conditions.append(str(origin)+'?'+str(equals)+'='+str(to)+':'+str(equals)+'!'+str(to))

	def saysIsLiar(self, origin, liar):
		self.conditions.append(str(origin)+'?'+str(origin)+'!'+str(liar)+':'+str(origin)+'!'+str(liar))

	def saysIsTrue(self, origin, true):
		self.conditions.append(str(origin)+'?'+str(origin)+'='+str(true)+':'+str(origin)+'='+str(true))

	def __repr__(self):
		out = ""
		for expr in self.conditions:
			out += "("+expr+")|"
		return out[:-1]

	def evaluateEquals(origin, resultGroup, condition):
		target,value = map(int, condition.split("="))
		target -= 1
		value -= 1
		if resultGroup[target].getState() == NOT_SURE or resultGroup[value].getState() == NOT_SURE:
			if resultGroup[target].getState() != NOT_SURE:
				resultGroup[value].setState(resultGroup[target].getState())
			elif resultGroup[value].getState() != NOT_SURE:
				resultGroup[target].setState(resultGroup[value].getState())

		elif resultGroup[target].getState() != resultGroup[value].getState():
			print "Conflicting condition: "+condition
			return True,True,resultGroup

	def evaluateDifferent(origin, resultGroup, condition):
		target,value = map(int, condition.split("!"))
		target -= 1
		value -= 1
		if resultGroup[target].getState() == NOT_SURE or resultGroup[value].getState() == NOT_SURE:
			if resultGroup[target].getState() != NOT_SURE:
				resultGroup[value].setState(resultGroup[target].getOppositeState())
			elif resultGroup[value].getState() != NOT_SURE:
				resultGroup[target].setState(resultGroup[value].getOppositeState())

		elif resultGroup[target].getState() != resultGroup[value].getState():
			print "Conflicting condition: "+condition
			return True,True,resultGroup

	def evaluateNotSureOrigin(origin, resultGroup, condition1, condition2):

	def solveExpression(self, group, expression):
		print "entered solveexpression: "+str(group)+" , "+expression
		resultGroup = group[:]
		tokens = expression.split("?")
		conds = tokens[1].split(":")
		origin = int(tokens[0])-1
		condition = ""

		target = 0
		value = 0

		if (resultGroup[origin].getState() == TRUE):
			condition = conds[0]
		elif (resultGroup[origin].getState() == FALSE):
			condition = conds[1]
		else:
			return self.evaluateNotSureOrigin(origin, resultGroup, cond[0], cond[1])

		if condition.count("=") > 0:
			return self.evaluateEquals(origin, resultGroup, condition)

		else:
			return self.evaluateDifferent(origin, resultGroup, condition)

		return True,False,resultGroup

	def applyToGroup(self, group):
		resultGroup = group[:]
		print "entered applytogroup: "+str(group)
		for expression in self.conditions:
			remove, error, resultGroup = self.solveExpression(resultGroup, expression)
			print "return from solve - rem:  "+str(remove)+" err: "+str(error)+" retGr: "+str(resultGroup)
			if error == True:
				return True, resultGroup

		return False, resultGroup

class Member():
	def __init__(self):
		self.state = NOT_SURE
		self.depends = 0
		self.dependState = NOT_SURE
		self.same = 0
		self.differ = 0
		self.isorigin = False
		self.expression = Expression()

	def isOrigin(self):
		return self.isorigin

	def setIsOrigin(self, isorigin):
		self.isorigin = isorigin

	def getExpression(self):
		return self.expression

	def setExpression(self, expression):
		self.expression = expression

	def getState(self):
		return self.state

	def getOppositeState(self):
		return TRUE if self.state == TRUE else FALSE if self.state == FALSE else NOT_SURE

	def setState(self, state):
		self.state = state

	def getDepends(self):
		return self.depends, self.dependState

	def setDepends(self, dependIdx, dependState):
		self.depends = dependIdx
		self.dependState = dependState

	def getSame(self):
		return self.same

	def setSame(self, sameIdx, dependIdx, dependState):
		self.same = sameIdx
		self.setDepends(dependIdx, dependState)

	def getDiffer(self):
		return self.differ

	def setDiffer(self, differIdx, dependIdx, dependState):
		self.differ = differIdx
		self.setDepends(dependIdx, dependState)

	def clone(self):
		clone = Member()
		clone.setState(self.getState())
		clone.setExpression(self.getExpression())
		clone.setIsOrigin(self.isOrigin())
		return clone

	def __repr__(self):
		stateStr = "T" if self.state == TRUE else "L" if self.state == FALSE else "-"
		return stateStr+("" if self.depends == 0 else "d"+str(self.depends)+("T" if self.dependState == TRUE else "F" if self.dependState == FALSE else "-"))+("" if self.same == 0 else "S"+str(self.same))+("" if self.differ == 0 else "D"+str(self.differ))


def getMemberListFromStatement(sampleGroup, statement):
	stTrueGroup = [Member() for x in xrange(len(sampleGroup))]
	stFalseGroup = [Member() for x in xrange(len(sampleGroup))]

	stList = statement.split(" ")
	origin = int(stList[0])
	modifier = stList[1]
	args = map(int, stList[2:])
	sampleGroup[origin-1].setIsOrigin(True)
	for arg in args:
		sampleGroup[arg-1].setIsOrigin(True)

	# Build "true premise" group
	if modifier == 'T':
		stTrueGroup[args[0]-1].setState(TRUE)
		stTrueGroup[origin-1].setState(TRUE)
		sampleGroup[args[0]-1].getExpression().saysIsTrue(origin, args[0])

	elif modifier == 'L':
		stTrueGroup[args[0]-1].setState(FALSE)
		stTrueGroup[origin-1].setState(TRUE)
		sampleGroup[args[0]-1].getExpression().saysIsLiar(origin, args[0])

	elif modifier == 'S':
		if args[0] == origin or args[1] == origin:
			stTrueGroup[args[0]-1].setState(TRUE)
			stTrueGroup[args[1]-1].setState(TRUE)


		else:
			stTrueGroup[args[0]-1].setSame(args[1], origin, TRUE)
			stTrueGroup[args[1]-1].setSame(args[0], origin, TRUE)

		sampleGroup[args[0]-1].getExpression().saysIsEqTo(origin, args[0], args[1])
		sampleGroup[args[1]-1].getExpression().saysIsEqTo(origin, args[0], args[1])

	else: # modifier == 'D'
		if args[0] == origin:
			stTrueGroup[args[0]-1].setState(TRUE)
			stTrueGroup[args[1]-1].setState(FALSE)
		elif args[1] == origin:
			stTrueGroup[args[0]-1].setState(FALSE)
			stTrueGroup[args[1]-1].setState(TRUE)
		else:
			stTrueGroup[args[0]-1].setDiffer(args[1], origin, TRUE)
			stTrueGroup[args[1]-1].setDiffer(args[0], origin, TRUE)

		sampleGroup[args[0]-1].getExpression().saysIsDifFrom(origin, args[0], args[1])
		sampleGroup[args[1]-1].getExpression().saysIsDifFrom(origin, args[0], args[1])

	# Build "false premise" group
	if modifier == 'T':
		stFalseGroup[origin-1].setState(FALSE) #Set origin first to be overwritten if equal
		stFalseGroup[args[0]-1].setState(FALSE)

	elif modifier == 'L':
		stFalseGroup[origin-1].setState(FALSE) #Set origin first to be overwritten if equal
		stFalseGroup[args[0]-1].setState(TRUE)

	elif modifier == 'S':
		if args[0] == origin:
			stFalseGroup[args[0]-1].setState(FALSE)
			stFalseGroup[args[1]-1].setState(TRUE)
		elif args[1] == origin:
			stFalseGroup[args[0]-1].setState(TRUE)
			stFalseGroup[args[1]-1].setState(FALSE)
		else:
			stFalseGroup[args[0]-1].setDiffer(args[1], origin, FALSE)
			stFalseGroup[args[1]-1].setDiffer(args[0], origin, FALSE)

	else: # modifier == 'D':
		if args[0] == origin or args[1] == origin:
			stFalseGroup[args[0]-1].setState(FALSE)
			stFalseGroup[args[1]-1].setState(FALSE)
		else:
			stFalseGroup[args[0]-1].setSame(args[1], origin, FALSE)
			stFalseGroup[args[1]-1].setSame(args[0], origin, FALSE)

	return stTrueGroup, stFalseGroup

def cloneGroup(group):
	newGroup = []
	for member in group:
		newGroup.append(member.clone())
	return newGroup

def getResultGroups(groupList, resultList, group, index):
	stateList = [NOT_SURE, TRUE, FALSE]
	if not group[index].isOrigin():
		stateList = [NOT_SURE]

	for state in stateList:
		group[index].setState(state)
		if index == len(group)-1:
			error = False
			clone = cloneGroup(group)
			signature = str(clone)
			sigOut = False
			while not error and not sigOut:
				for member in clone:
					error, clone = member.getExpression().applyToGroup(clone)
					print "return from applytogroup err: "+str(error)+" group: "+str(clone)
					if error == True: break;
				newSig = str(clone)
				if signature == newSig:
					sigOut = True
				else:
					signature = newSig

			if error == False:
				print "Adding to list: "+str(group)+" thisClone: "+str(clone)
				groupList.append(cloneGroup(group))
		else:
			getResultGroups(groupList, resultList, group, index+1)

for case in range(1,int(raw_input())+1):          # For all test cases
	group_len, statement_len = map(int, raw_input().split(" ")) # Get test case information

	group = [Member() for x in xrange(group_len)]
	statements = []

	for i in range(statement_len):
		statements.append(raw_input())

	for statement in statements:
		print "Statement: "+statement
		getMemberListFromStatement(group, statement);

	resultGroups = []
	resultStates = []

	# brute force com possibilidades para verificar dependencias.
	getResultGroups(resultGroups, resultStates, group, 0)
	print resultGroups

	print "Case #%d: %s" % (case, " ".join([str(group[x]) for x in xrange(len(group))])) # Report results

#!/usr/bin/python

# "Constants" - gotta be careful because there's no native solution in python
target = "welcome to code jam"
nullify= '-'

# Our "solve for X" function
def rec(line, pointer, letterIndex, times):

    #If our letterIndex turned out the same as our phrase length, we can count
    if (letterIndex == len(target)-1):
        times += 1
        return times

    #If not, we've got work to do. While we still have the current expected letter on the string, do
    while line[pointer:len(line)].count(target[letterIndex+1]) > 0:
        #print "Searching letter %c, %d occurrences left on line \"%s\" from position %d" % (target[int(letterIndex+1)], line[pointer:len(line)].count(target[letterIndex+1]), line, pointer)

        #Go look for the next letter, from where the current letter is
        times = rec(line, line.index(target[letterIndex+1], pointer, len(line)), letterIndex+1, times)
        #"Erase" our current letter position, so we don't search it again from here
        line = line[:pointer]+line[pointer:len(line)].replace(target[letterIndex+1], nullify, 1)

    return times

# Get header
line = raw_input()
cases = int(line)

# Solve test cases
for i in range(cases):
    line = raw_input()

    times = 0
    letterIndex = -1
    pointer = 0

    times = rec(line, pointer, letterIndex, times)

    # Prints only last 4 digits
    fnum = "%04d" % times
    print "Case #%d: %s" % (int(i+1), fnum[max(0,len(fnum)-4):len(fnum)])

exit()


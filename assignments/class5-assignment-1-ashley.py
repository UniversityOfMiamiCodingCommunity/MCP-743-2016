# Turn in your hand-written answers at the beginning of class.  Be sure to include your name.
# At 12 noon before class, post a dictionary of your answers to GitHub in the assignments directory.
# The format of this dictionary should be answerDict = {1:answer1, 2:answer2, ..., N:answerN}.
####################################################################################################

# These four variables are defined here, and are used throughout the assignment.
################################################################################

city = "chicago"
cityAsList = list(city)
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

answerDict = {}

#################################################################################
# String and list questions.
#################################################################################

#1) What is the value of c?
c = city[0:]
answerDict[1] = c

#2) What is the value of c?
b = int(len(city)/2)
c = city[0:b]
answerDict[2] = c

#3) What is the value of c?
b = int(len(city)/2)
c = city[0:-b]
answerDict[3] = c

#4) What is the value of c?
b = int(len(city)/2)
d = b - 1
c = city[d:b]
answerDict[4] = c

#5) What is the value of c?
b = int(len(city)/2)
c = city[:b]
answerDict[5] = c

#6) What is the final value of the string orwell?
l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
		orwell += x
answerDict[6] = orwell

#7) What is the final value of the string orwell?
orwell = ""
l1[6] = "present"
l1[13] = "past"
for x in l1 + l2:
		orwell += x
answerDict[7] = orwell	

#8) What is the final value of the string orwell?
orwell = ""
l2[6] = "past"
l2[13] = "future"
for x in l1 + l2:
		orwell += x
answerDict[8] = orwell

#9) What is the final value of the string orwell?
orwell = ""
l2[6] = "past"
l2[13] = "future"
for x in l1 + l2:
		orwell += x
l3 = orwell.split("past")
orwell = ""
for x in l3:
		if "Who" in x:
				orwell += (x + "past")
		else:
				orwell += x
answerDict[9] = orwell

#10) What is the value of i after the statement is evaluated?
i = 0
if "e" in city:
		i += 1
answerDict[10] = i

#11) What is the value of i after the statement is evaluated?
i = 0
if "e" not in consonants:
		i += 1
answerDict[11] = i

#12) What is the value of i after the statement is evaluated?
i = 0
if "e" not in city:
		i += 1
else:
		i -=1
answerDict[12] = i

#13) What is the value of i after the while loop runs to completion?
i = 0
while i < len(city):
		i += 1
answerDict[13] = i

#14) Which statement is inside the loop?
answerDict[14] = "i += 1 is inside the while loop"

#15) Which statement is outside the loop?
answerDict[15] = "i = 0 is outside the while loop"

#16) What is the term that describes the expression (i < len(city))?
answerDict[16] = "i < len(city) is a conditional statement"

#17) What is the value of earth after the while loop runs to completion?
earth = 0
while earth < len(city):
		earth += 1
answerDict[17] = i
		
#18) What is the value of i after the for loop runs to completion?
i = 0
for x in city:
		i += 1
answerDict[18] = i

#19) What is the value of i after this code runs to completion?
i = 0
for x in city:
		i += 1
for x in city:
		i += 1
answerDict[19] = i

#20) What is the value of i after the while loop runs to completion?
i = len(city)
while i > 0:
		i -= 1
answerDict[20] = i

#21) What is the value of i after the while loop runs to completion?
i = len(city)
j = int(len(city)/2)
while i > len(city[0:j]):
		i -= 1
answerDict[21] = i

#22) What is the value of i after this code runs to completion?
i = 0
for x in city:
		if x in vowels:
				i += 1
answerDict[22] = i

#23) What is the value of i after this code runs to completion?
i = 0
for x in city:
		if x not in consonants:
				i += 1
answerDict[23] = i

#24) What is the value of i after this code runs to completion?
i = 0
for x in city:
		if x not in consonants:
				continue
		else:
				i += 1
answerDict[24] = i

#25) What is the value of i after this code runs to completion?
i = 0
for x in city:
		if x in consonants:
				i += 1
answerDict[25] = i

#26) What is the value of i after this code runs to completion?
i = 0
for x in city:
		if x not in consonants:
				i += 1
answerDict[26] = i

#27) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
		if x in vowels:
				j += 1
		i += 1
statement27 = "i = " + str(i) + " and j = " + str(j)
answerDict[27] = statement27

#28) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
		if x in vowels:
				j *= 2
		i += 1
statement28 = "i = " + str(i) + " and j = " + str(j)
answerDict[28] = statement28

#29) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
		if x not in vowels:
				j *= 1
		i += 2
statement29 = "i = " + str(i) + " and j = " + str(j)
answerDict[29] = statement29

#30) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
		if x == "e":
				j *= 1
		i += 1
statement30 = "i = " + str(i) + " and j = " + str(j)
answerDict[30] = statement30

#31) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
		if x != "e":
				j *= 1
		i += 1
statement31 = "i = " + str(i) + " and j = " + str(j)
answerDict[31] = statement31

#32) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
		if x == "e":
				break
		i += 1
statement32 = "i = " + str(i) + " and j = " + str(j)
answerDict[32] = statement32

#33) What are the values of i, j, k after this code runs to completion?
i = 0
j = 0
k = 0
for x in city:
		j = 0
		while j < len(city):
				k += 1
				j += 1
		i += 1
statement33 = "i = " + str(i) + ", j = " + str(j) + ", and k = " + str(k)
answerDict[33] = statement33

#34) What are the values of i, j, k, a after this code runs to completion?
i = 0
j = 0
k = 0
a = 0
for x in city:
		j = 0
		while j < len(city):
				if city[j] in vowels:
						a += 1
				k += 1
				j += 1
		i += 1
statement34 = "i = " + str(i) + ", j = " + str(j) + ", k = " + str(k) + ", and a = " + str(a)
answerDict[34] = statement34

print answerDict



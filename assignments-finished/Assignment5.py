city = "albuquerque"
cityAsList = list(city)
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

#################################################################################
# String and list questions.
#################################################################################

# 1) What is the value of c?
#################################################################################
c = city[0:]
print(c)

# 2) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:b]
print(c)

# 3) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:-b]
print(c)

# 4) What is the value of c? 
################################################################################# 
b = int(len(city)/2)
d = b-1
c = city[d:b]
print(c)

# 5) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[:b]
print(c)

# 6) What is the final value of the string orwell?
#################################################################################
l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
	orwell += x
print(orwell)

# 7) What is the final value of the string orwell?
#################################################################################
orwell = ""
l1[6] = "present"
l1[13] = "past"
for x in l1 + l2:
	orwell += x
print(orwell)

# 8) What is the final value of the string orwell?
#################################################################################
orwell = ""
l2[6] = "past"
l2[13] = "future"
for x in l1 + l2:
	orwell += x
print(orwell)

# 9) What is the final value of the string orwell?
#################################################################################
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
print(orwell)

# 10) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" in city:
	i += 1
print(i)

# 11) What is the value of i after the statement is evaluated?
#################################################################################
i=0	
if "e" not in consonants:
	i += 1
print(i)

# 12) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" not in city:
	i += 1 
else:
	i -= 1
print(i)

#################################################################################
# 13) What is the value of i after the while loop runs to completion? 
i=0
while i < len(city):
	i += 1
print(i)

# There are three statements (i.e. lines) in this loop.
i=0
while i < len(city):
	i += 1
	
# 14) Which statement is inside the loop?
print("i += 1")
# 15) Which statement is outside the loop?
print("i=0")
# 16) What is the term that describes the expression (i < len(city))?
print("conditional")
#################################################################################

# 17) What is the value of earth after the while loop runs to completion?
#################################################################################
earth = 0
while earth < len(city):
	earth += 1
print(earth)

# 18) What is the value of i after the for loop runs to completion?
#################################################################################
i=0
for x in city:
	i += 1
print(i)

# 19) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	i += 1
for x in city:
	i += 1
print(i)

# 20) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
while i > 0:
	i -= 1
print(i)

# 21) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
j = int(len(city)/2)
while i > len(city[0:j]):
	i -= 1
print(i)	

# 22) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x in vowels:
		i += 1
print(i)

# 23) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		i += 1
print(i)

# 24) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		continue
	else:
		i += 1
print(i)

# 25) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
    if x in consonants:
        i += 1
print(i)

# 26) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
    if x not in consonants:
        i += 1
print(i)

# 27) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x in vowels:
		j += 1 
	i += 1
print("i=", i)
print("j=", j)	

# 28) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x in vowels:
		j *= 2
	i += 1
print("i=", i)
print("j=", j)	

# 29) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x not in vowels:
		j *= 1 
	i += 2
print("i=", i)
print("j=", j)

# 30) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x == "e":
		j *= 1 
	i += 1
print("i=", i)
print("j=", j)

# 31) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x != "e":
		j *= 1 
	i += 1
print("i=", i)
print("j=", j)

# 32) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x == "e":
		break 
	i += 1
print("i=", i)
print("j=", j)

# 33) What are the values of i, j, k after this code runs to completion?
#################################################################################
i=0
j=0
k=0
for x in city:
	j=0
	while j < len(city):
		k += 1
		j += 1 
	i += 1	
print("i=", i)
print("j=", j)
print("k=", k)

# 34) What are the values of i, j, k, a after this code runs to completion?
#################################################################################
i=0
j=0
k=0
a=0
for x in city:
	j=0
	while j < len(city):
		if city[j] in vowels:
			a += 1 
		k += 1
		j += 1 
	i += 1
print("i=", i)
print("j=", j)
print("k=", k)
print("a=", a)

answerDict = {}

answerDict[1] = "albuquerque"
answerDict[2] = "albuq"
answerDict[3] = "albuqu"
answerDict[4] = "q"
answerDict[5] = "albuq"
answerDict[6] = "Who controls the past, controls the future. Who controls the present, controls the past."
answerDict[7] = "Who controls the present, controls the past. Who controls the present, controls the past."
answerDict[8] = "Who controls the present, controls the past. Who controls the past, controls the future."
answerDict[9] = "Who controls the present, controls the past. Who controls the past, controls the future."
answerDict[10] = "i=1"
answerDict[11] = "i=1"
answerDict[12] = "i=-1"
answerDict[13] = "i=11"
answerDict[14] = "i += 1"
answerDict[15] = "i = 0"
answerDict[16] = "conditional"
answerDict[17] = "i=11"
answerDict[18] = "i=11"
answerDict[19] = "i=22"
answerDict[20] = "i=0"
answerDict[21] = "i=5"
answerDict[22] = "i=6"
answerDict[23] = "i=6"
answerDict[24] = "i=5"
answerDict[25] = "i=5"
answerDict[26] = "i=6"
answerDict[27] = "i=11, j=6"
answerDict[28] = "i=11, j=0"
answerDict[29] = "i=22, j=0"
answerDict[30] = "i=11, j=0"
answerDict[31] = "i=11, j=0"
answerDict[32] = "i=6, j=0"
answerDict[33] = "i=11, j=11, k=121"
answerDict[34] = "i=11, j=11, k=121, a=66"

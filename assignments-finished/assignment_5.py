# Turn in your hand-written answers at the beginning of class. Be sure to include your name.
# At 12 noon before class, post a dictionary of your answers to GitHub in the assignments directory.
# The format of this dictionary should be answerDict = {1:answer1, 2:answer2, ..., N:answerN}.
####################################################################################################
# These four variables are defined here, and are used throughout the assignment.
#################################################################################

city = "jacksonville"
cityAsList = list(city)
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
answerDict = {}
#################################################################################
# String and list questions.
#################################################################################
# 1) What is the value of c?

#################################################################################
c = city[0:]
answerDict[1] = c

# 2) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:b]
answerDict[2] = c

# 3) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:-b]
answerDict[3] = c

# 4) What is the value of c?
#################################################################################
b = int(len(city)/2)
d = b - 1
c = city[d:b]
answerDict[4] = c

# 5) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[:b]
answerDict[5] = c


# 6) What is the final value of the string orwell?
#################################################################################
l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
    orwell += x
answerDict[6] = orwell


# 7) What is the final value of the string orwell?
#################################################################################
orwell = ""
l1[6] = "present"
l1[13] = "past"
for x in l1 + l2:
    orwell += x
answerDict[7] = orwell

# 8) What is the final value of the string orwell?
#################################################################################
orwell = ""
l2[6] = "past"
l2[13] = "future"
for x in l1 + l2:
    orwell += x
answerDict[8] = orwell

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
answerDict[9] = orwell

# 10) What is the value of i after the statement is evaluated?
#################################################################################
i = 0
if "e" in city:
    i += 1
answerDict[10] = i
# 11) What is the value of i after the statement is evaluated?
#################################################################################
i = 0
if "e" not in consonants:
    i += 1
answerDict[11] = i
# 12) What is the value of i after the statement is evaluated?
#################################################################################
i = 0
if "e" not in city:
    i += 1
else:
    i -= 1
answerDict[12] = i

#################################################################################
# Loop questions.
#################################################################################
# 13) What is the value of i after the while loop runs to completion?
# There are three statements (i.e. lines) in this loop.
# 14) Which statement is inside the loop?
# 15) Which statement is outside the loop?
# 16) What is the term that describes the expression (i < len(city))?
#################################################################################
i = 0
while i < len(city):
    i += 1
answerDict[13] = i
answerDict[14] = 'Line 3'
answerDict[15] = 'Line 1'
answerDict[16] = 'This statement is a coditional loop which will continue to run as long as i is less than the length of city'

# 17) What is the value of earth after the while loop runs to completion?
#################################################################################
earth = 0
while earth < len(city):
    earth += 1
answerDict[17] = earth
# 18) What is the value of i after the for loop runs to completion?
#################################################################################
i = 0
for x in city:
    i += 1
answerDict[18] = i
# 19) What is the value of i after this code runs to completion?
#################################################################################
i = 0
for x in city:
    i += 1
for x in city:
    i += 1
answerDict[19] = i

# 20) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
while i > 0:
    i -= 1
answerDict[20] = i
# 21) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
j = int(len(city)/2)
while i > len(city[0:j]):
    i -= 1
answerDict[21] = i
# 22) What is the value of i after this code runs to completion?
#################################################################################
i = 0
for x in city:
    if x in vowels:
        i += 1
answerDict[22] = i
# 23) What is the value of i after this code runs to completion?
#################################################################################
i = 0
for x in city:
    if x not in consonants:
        i += 1
answerDict[23] = i
# 24) What is the value of i after this code runs to completion?
#################################################################################
i = 0
for x in city:
    if x not in consonants:
        continue
    else:
        i += 1
answerDict[24] = i
# 25) What is the value of i after this code runs to completion?
#################################################################################
i = 0
for x in city:
    if x in consonants:
        i += 1
answerDict[25] = i
# 26) What is the value of i after this code runs to completion?
#################################################################################
i = 0
for x in city:
    if x not in consonants:
        i += 1
answerDict[26] = i
# 27) What are the values of i and j after this code runs to completion?
#################################################################################
i = 0
j = 0
for x in city:
    if x in vowels:
        j += 1
    i += 1
answerDict[27] = (i, j)

# 28) What are the values of i and j after this code runs to completion?
#################################################################################
i = 0
j = 0
for x in city:
    if x in vowels:
        j *= 2
    i += 1
answerDict[28] = (i, j)

# 29) What are the values of i and j after this code runs to completion?
#################################################################################
i = 0
j = 0
for x in city:
    if x not in vowels:
        j *= 1
    i += 2
answerDict[29] = (i, j)
# 30) What are the values of i and j after this code runs to completion?
#################################################################################
i = 0
j = 0
for x in city:
    if x == "e":
        j *= 1
    i += 1
answerDict[30] = (i, j)
# 31) What are the values of i and j after this code runs to completion?
#################################################################################
i = 0
j = 0
for x in city:
    if x != "e":
        j *= 1
    i += 1
answerDict[31] =(i, j)
# 32) What are the values of i and j after this code runs to completion?
#################################################################################
i = 0
j = 0
for x in city:
    if x == "e":
        break
    i += 1
answerDict[32] = i
# 33) What are the values of i, j, k after this code runs to completion?
#################################################################################
i = 0
j = 0
k = 0
for x in city:
    j = 0
    while j < len(city):
        k += 1
        j += 1
    i += 1
answerDict[33] = (i, j, k)
# 34) What are the values of i, j, k, a after this code runs to completion?
#################################################################################
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
answerDict[34] = (i, j, k, a)
print(answerDict)
fileOutput_1 = open("/Users/Chris/Documents/Chris/python/MCP-743/dataFiles/assignment5Dictionary.py", "w")
fileOutput_1.write(str(answerDict))
fileOutput_1.close()

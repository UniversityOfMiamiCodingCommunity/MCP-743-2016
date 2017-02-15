# Turn in your hand-written answers at the beginning of class. Be sure to include your name.
# At 12 noon before class, post a dictionary of your answers to GitHub in the assignments directory.
# The format of this dictionary should be answerDict = {1:answer1, 2:answer2, ..., N:answerN}.

#################################################################################
# Dictionary of answers
#################################################################################
annaAnswerDict = {
					1:"charlotte",
					2:"char",
					3:"charl",
					4:"r",
					5:"char",
					6:"Who controls the past, controls the future.\nWho controls the present, controls the past.\n",
					7:"Who controls the present, controls the past.\nWho controls the present, controls the past.\n",
					8:"Who controls the present, controls the past.\nWho controls the past, controls the future.\n",
					9:"Who controls the present, controls the past.\nWho controls the past, controls the future.\n",
					10:"i = 1",
					11:"i = 1",
					12:"i = -1",
					13:"i = 9",
					14:"i += 1",
					15:"i=0",
					16:"while loop",
					17:"earth = 9",
					18:"i = 9",
					19:"i = 18",
					20:"i = 0",
					21:"i = 4",
					22:"i = 3",
					23:"i = 3",
					24:"i = 6",
					25:"i = 6",
					26:"i = 3",
					27:"i = 9, j = 3",
					28:"i = 9, j = 0",
					29:"i = 18, j = 0",
					30:"i = 9, j = 0",
					31:"i = 9, j = 0",
					32:"i = 8, j = 0",
					33:"i = 9, j = 9, k = 81",
					34:"i = 9, j = 9, k = 81, a = 27"
					}

#################################################################################
# These four variables are defined here, and are used throughout the assignment.
#################################################################################
city = "charlotte"
cityAsList = list(city)
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

#################################################################################
# String and list questions.
#################################################################################
# 1) What is the value of c?
#################################################################################
question = 1
c = city[0:]

answer1 = "charlotte"

# 2) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:b]

answer2 = "char"

# 3) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:-b]

answer3 = "charl"

# 4) What is the value of c?
#################################################################################
b = int(len(city)/2)
d=b-1
c = city[d:b]

answer4 = "r"

# 5) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[:b]

answer5 = "char"

# 6) What is the final value of the string orwell?
#################################################################################
l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
	orwell += x

answer6 = "Who controls the past, controls the future.\nWho controls the present, controls the past.\n"

# 7) What is the final value of the string orwell?
#################################################################################
orwell = ""
l1[6] = "present"
l1[13] = "past"
for x in l1 + l2:
	orwell += x

answer7 = "Who controls the present, controls the past.\nWho controls the present, controls the past.\n"

# 8) What is the final value of the string orwell?
#################################################################################
orwell = ""
l2[6] = "past"
l2[13] = "future"
for x in l1 + l2:
	orwell += x

answer8 = "Who controls the present, controls the past.\nWho controls the past, controls the future.\n"

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

answer9 = "Who controls the present, controls the past.\nWho controls the past, controls the future.\n"

# 10) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" in city:
	i += 1

answer10 = "i = 1"

# 11) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" not in consonants:
	i += 1

answer11 = "i = 1"

# 12) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" not in city:
	i += 1
else:
	i -= 1

answer12 = "i = -1"

#################################################################################
# Loop questions.
#################################################################################

# 13) What is the value of i after the while loop runs to completion?
# There are three statements (i.e. lines) in this loop.
# 		14) Which statement is inside the loop?
# 		15) Which statement is outside the loop?
# 16) What is the term that describes the expression (i < len(city))?
#################################################################################
i=0
while i < len(city):
	i += 1

answer13 = "i = 9"
answer14 = "i += 1"
answer15 = "i=0"
answer16 = "while loop"

# 17) What is the value of earth after the while loop runs to completion?
#################################################################################
earth = 0
while earth < len(city):
	earth += 1

answer17 = "earth = 9"

# 18) What is the value of i after the for loop runs to completion?
#################################################################################
i=0
for x in city:
	i += 1

answer18 = "i = 9"

# 19) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	i += 1
for x in city:
	i += 1

answer19 = "i = 18"

# 20) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
while i > 0:
	i -= 1

answer20 = "i = 0"

# 21) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
j = int(len(city)/2)
while i > len(city[0:j]):
	i -= 1

answer21 = "i = 4"

# 22) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city: 
	if x in vowels:
		i += 1

answer22 = "i = 3"

# 23) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		i += 1

answer23 = "i = 3"

# 24) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		continue
	else:
		i += 1

answer24 = "i = 6"

# 25) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x in consonants:
		i += 1

answer25 = "i = 6"

# 26) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		i += 1

answer26 = "i = 3"

# 27) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x in vowels:
		j += 1
	i += 1

answer27i = "9"
answer27j = "3"

# 28) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x in vowels:
		j *= 2
	i += 1

answer28i = "9"
answer28j = "0"

# 29) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x not in vowels:
		j *= 1
	i += 2

answer29i = "18"
answer29j = "0"

# 30) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x == "e":
		j *= 1
	i += 1

answer30i = "9"
answer30j = "0"

# 31) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x != "e":
		j *= 1
	i += 1

answer31i = "9"
answer31j = "0"
# 32) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x == "e":
		break
	i += 1

answer32i = "8"
answer32j = "0"

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

answer33i = "9"
answer33j = "9"
answer33k = "81"

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

answer34i = "9"
answer34j = "9"
answer34k = "81"
answer34a = "27"

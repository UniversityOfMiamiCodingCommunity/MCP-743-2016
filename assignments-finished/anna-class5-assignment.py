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
annaAnswerDict2 = {}

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

answer = "charlotte"

annaAnswerDict2[question] = answer
question += 1

# 2) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:b]

answer = "char"

annaAnswerDict2[question] = answer
question += 1

# 3) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[0:-b]

answer = "charl"

annaAnswerDict2[question] = answer
question += 1

# 4) What is the value of c?
#################################################################################
b = int(len(city)/2)
d=b-1
c = city[d:b]

answer = "r"

annaAnswerDict2[question] = answer
question += 1

# 5) What is the value of c?
#################################################################################
b = int(len(city)/2)
c = city[:b]

answer = "char"

annaAnswerDict2[question] = answer
question += 1

# 6) What is the final value of the string orwell?
#################################################################################
l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
	orwell += x

answer = "Who controls the past, controls the future.\nWho controls the present, controls the past.\n"

annaAnswerDict2[question] = answer
question += 1

# 7) What is the final value of the string orwell?
#################################################################################
orwell = ""
l1[6] = "present"
l1[13] = "past"
for x in l1 + l2:
	orwell += x

answer = "Who controls the present, controls the past.\nWho controls the present, controls the past.\n"

annaAnswerDict2[question] = answer
question += 1

# 8) What is the final value of the string orwell?
#################################################################################
orwell = ""
l2[6] = "past"
l2[13] = "future"
for x in l1 + l2:
	orwell += x

answer = "Who controls the present, controls the past.\nWho controls the past, controls the future.\n"

annaAnswerDict2[question] = answer
question += 1

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

answer = "Who controls the present, controls the past.\nWho controls the past, controls the future.\n"

annaAnswerDict2[question] = answer
question += 1

# 10) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" in city:
	i += 1

answer = 1

annaAnswerDict2[question] = answer
question += 1

# 11) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" not in consonants:
	i += 1

answer = 1

annaAnswerDict2[question] = answer
question += 1

# 12) What is the value of i after the statement is evaluated?
#################################################################################
i=0
if "e" not in city:
	i += 1
else:
	i -= 1

answer = -1

annaAnswerDict2[question] = answer
question += 1

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

answer = 9

annaAnswerDict2[question] = answer
question += 1

answer = "i += 1"

annaAnswerDict2[question] = answer
question += 1

answer = "i=0"

annaAnswerDict2[question] = answer
question += 1

answer = "while loop"

annaAnswerDict2[question] = answer
question += 1


# 17) What is the value of earth after the while loop runs to completion?
#################################################################################
earth = 0
while earth < len(city):
	earth += 1

answer = 9

annaAnswerDict2[question] = answer
question += 1

# 18) What is the value of i after the for loop runs to completion?
#################################################################################
i=0
for x in city:
	i += 1

answer = 9


annaAnswerDict2[question] = answer
question += 1

# 19) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	i += 1
for x in city:
	i += 1

answer = 18

annaAnswerDict2[question] = answer
question += 1

# 20) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
while i > 0:
	i -= 1

answer = 0

annaAnswerDict2[question] = answer
question += 1

# 21) What is the value of i after the while loop runs to completion?
#################################################################################
i = len(city)
j = int(len(city)/2)
while i > len(city[0:j]):
	i -= 1

answer = 4

annaAnswerDict2[question] = answer
question += 1

# 22) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city: 
	if x in vowels:
		i += 1

answer = 3

annaAnswerDict2[question] = answer
question += 1

# 23) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		i += 1

answer = 3

annaAnswerDict2[question] = answer
question += 1

# 24) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		continue
	else:
		i += 1

answer = 6

annaAnswerDict2[question] = answer
question += 1

# 25) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x in consonants:
		i += 1

answer = 6

annaAnswerDict2[question] = answer
question += 1

# 26) What is the value of i after this code runs to completion?
#################################################################################
i=0
for x in city:
	if x not in consonants:
		i += 1

answer = 3

annaAnswerDict2[question] = answer
question += 1

# 27) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x in vowels:
		j += 1
	i += 1

answer = 3,9

annaAnswerDict2[question] = answer
question += 1

# 28) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x in vowels:
		j *= 2
	i += 1

answer = 9,0

annaAnswerDict2[question] = answer
question += 1

# 29) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x not in vowels:
		j *= 1
	i += 2

answer = 18,0

annaAnswerDict2[question] = answer
question += 1


# 30) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x == "e":
		j *= 1
	i += 1

answer = 9,0

annaAnswerDict2[question] = answer
question += 1

# 31) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x != "e":
		j *= 1
	i += 1

answer = 9,0

annaAnswerDict2[question] = answer
question += 1

# 32) What are the values of i and j after this code runs to completion?
#################################################################################
i=0
j=0
for x in city:
	if x == "e":
		break
	i += 1

answer = 8,0

annaAnswerDict2[question] = answer
question += 1

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

answer = 9,9,81

annaAnswerDict2[question] = answer
question += 1

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

answer = 9,9,81,27

annaAnswerDict2[question] = answer
question += 1

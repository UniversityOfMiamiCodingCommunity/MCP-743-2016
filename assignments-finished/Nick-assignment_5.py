city = "columbus"
cityAsList = list(city)
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

answerDict = {}

# 1) What is the value of c?
c = city[0:]

answerDict['1'] = 'columbus'

# 2) What is the value of c?
b = int(len(city)/2)
c = city[0:b]

answerDict['2'] = 'colu'

# 3) What is the value of c?
b = int(len(city)/2)
c = city[0:-b]

answerDict['3'] = 'colu'

# 4) What is the value of c?
b = int(len(city)/2)
d = b - 1
c = city[d:b]

answerDict['4'] = 'u'

# 5) What is the value of c?
b = int(len(city)/2)
c = city[:b]

answerDict['5'] = 'colu'

# 6) What is the final value of the string orwell?
l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
	orwell += x

answerDict['6'] = 'Who controls the past, controls the future. Who controls the present, controls the past.'

# 7) What is the final value of the string orwell?
orwell = ""
l1[6] = 'present'
l1[13] = 'past'

for x in l1 + l2:
	orwell += x

answerDict['7'] = 'Who controls the present, controls the past. Who controls the present, controls the past.'

# 8) What is the final value of the string orwell?
orwell = ""
l2[6] = 'past'
l2[13] = 'future'

for x in l1 + l2:
	orwell += x

answerDict['8'] = 'Who controls the present, controls the past. Who controls the past, controls the future.'

# 9) What is the final value of the string orwell?
orwell = ""
l2[6] = 'past'
l2[13] = 'future'

for x in l1 + l2:
	orwell += x
l3 = orwell.split("past")
#~ print(l3)

orwell = ""
for x in l3:
	if "Who" in x:
		orwell += (x + 'past')
	else:
		orwell += x

answerDict['9'] = 'Who controls the present, controls the past. Who controls the past, controls the future.'

# 10) What is the value of i after the statement is evaluated?
i = 0
if "e" in city:
	i += 1

answerDict['10'] = '0'

# 11) What is the value of i after the statement is evaluated?
i = 0
if "e" not in consonants:
	i += 1

answerDict['11'] = '1'

# 12) What is the value of i after the statement is evaluated?
i = 0
if "e" not in city:
	i += 1
else:
	i -= 1

answerDict['12'] = '1'

# 13) What is the value of i after the while loop runs to completion?
# There are three statements (i.e. lines) in this loop.
# 14) Which statement is inside the loop?
# 15) Which statement is outside the loop?
# 16) What is the term that describes the expression (i < len(city))?
i = 0
while i < len(city):
	i += 1

answerDict['13'] = '8'
answerDict['14'] = 'i += 1'
answerDict['15'] = 'i = 0'
answerDict['16'] = 'Condition'

# 17) What is the value of earth after the while loop runs to completion?
earth = 0
while earth < len(city):
	earth += 1

answerDict['17'] = '8'

# 18) What is the value of i after the for loop runs to completion?
i = 0
for x in city:
	i += 1

answerDict['18'] = '8'

# 19) What is the value of i after this code runs to completion?
i = 0
for x in city:
	i += 1
for x in city:
	i += 1

answerDict['19'] = '16'

# 20) What is the value of i after the while loop runs to completion?
i = len(city)
while i > 0:
	i -= 1

answerDict['20'] = '0'

# 21) What is the value of i after the while loop runs to completion?
i = len(city)
j = int(len(city)/2)
while i > len(city[0:j]):
	i -= 1

answerDict['21'] = '4'

# 22) What is the value of i after this code runs to completion?
i = 0
for x in city:
	if x in vowels:
		i += 1

answerDict['22'] = '3'

# 23) What is the value of i after this code runs to completion?
i = 0
for x in city:
	if x not in consonants:
		i += 1

answerDict['23'] = '3'

# 24) What is the value of i after this code runs to completion?
i = 0
for x in city:
	if x not in consonants:
		continue
	else:
		i += 1

answerDict['24'] = '5'

# 25) What is the value of i after this code runs to completion?
i = 0
for x in city:
	if x in consonants:
		i += 1

answerDict['25'] = '5'

# 26) What is the value of i after this code runs to completion?
i = 0
for x in city:
	if x not in consonants:
		i += 1

answerDict['26'] = '3'

# 27) What are the values of i and j after this code runs to completion? 
i = 0
j = 0
for x in city:
	if x in vowels:
		j += 1
	i += 1

answerDict['27'] = 'i = 8, j = 3'

# 28) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
	if x in vowels:
		j *= 2
	i += 1

answerDict['28'] = 'i = 8, j = 0'

# 29) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
	if x not in vowels:
		j *= 1
	i += 2
	
answerDict['29'] = 'i = 16, j = 0'

# 30) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
	if x == "e":
		j *= 1
	i += 1
	
answerDict['30'] = 'i = 8, j = 0'

# 31) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
	if x != "e":
		j *= 1
	i += 1

answerDict['31'] = 'i = 8, j = 0'

# 32) What are the values of i and j after this code runs to completion?
i = 0
j = 0
for x in city:
	if x == "e":
		break
	i =+ 1

answerDict['32'] = 'i = 1, j = 0'

# 33) What are the values of i, j, k after this code runs to completion?
i = 0
j = 0
k = 0
for x in city:
	j = 0
	while j < len(city):
		k += 1
		j += 1
	i += 1

answerDict['33'] = 'i = 8, j = 8, k = 64'

# 34) What are the values of i, j, k, a after this code runs to completion?
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

answerDict['34'] = 'i = 8, j = 8, k = 64, a = 24'

print(answerDict)


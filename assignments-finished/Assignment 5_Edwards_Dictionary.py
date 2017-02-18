#Assignment for 2/15/17



answerDict = { }

answerDict [1] = "miami"
answerDict [2] = "mi"
answerDict [3] = "mia"
answerDict [4] = "i"
answerDict [5] = "mi"
answerDict [6] = "Who controls the past controls the future. Who controls the present, controls the past"
answerDict [7] = "Who controls the present, controls the past. x2" 
answerDict [8] = "Who controls the present, controls the past. Who controls the past, controls the future"
answerDict [9] = "Same as 8"
answerDict [10] = "i = 0"
answerDict [11] = "i = 1"
answerDict [12] = "i = 1"
answerDict [13] = "i = 5"
answerDict [14] = "i += 1"
answerDict [15] = "i = 0"
answerDict [16] = "i < 5, Conditional Statement"
answerDict [17] = "earth = 5"
answerDict [18] = "i = 5"
answerDict [19] = "i = 10"
answerDict [20] = "i = 0"
answerDict [21] = "i = 2"
answerDict [22] = "i = 3"
answerDict [23] = "i = 3"
answerDict [24] = "i = 2"
answerDict [25] = "i = 2"
answerDict [26] = "i = 3"
answerDict [27] = "i = 5 , j = 3"
answerDict [28] = "i = 5 , j = 0"
answerDict [29] = "i = 10 , j = 0"
answerDict [30] =  "i = 5 , j = 0"
answerDict [31] = "i = 5 , j = 0" 
answerDict [32] = "i= 5, j = 0" 
answerDict [33] = "i = 5 , j = 5 , k = 25" 
answerDict [34] = "i = 5, j = 5, k = 25 , a = 15"

print(answerDict)

city = "miami"
cityAsList = list(city)
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

c = city[0:]
print(c)

b = int(len(city)/2)
c = city[0:b]
print(c)

b = int(len(city)/2)
c = city[0:-b]
print(c)

b = int(len(city)/2)
d = b - 1
c = city[d:b]
print(c)

b = int(len(city)/2)
c = city[:b]
print(c)

l1 = ["Who", " ", "controls", " ", "the", " ", "past", ",", " ", "controls", " ", "the", " ", "future", ".", "\n"]
l2 = ["Who", " ", "controls", " ", "the", " ", "present", ",", " ", "controls", " ", "the", " ", "past", ".", "\n"]
orwell = ""
for x in l1 + l2:
	orwell += x
print(orwell)

orwell = ""
l1[6] = "present"
l1[13] = "past"
for x in l1 + l2:
	orwell += x
print(orwell)

orwell = "" 
l2[6] = "past" 
l2[13] = "future" 
for x in l1 + l2: 
	orwell += x 
print(orwell)

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

i = 0 
if "e" in city: 
	i += 1
print(i)

i = 0 
if "e" not in consonants: 
	i += 1 
print(i)

i = 0 
if "e" not in city: 
	i += 1 
else: 
		i -= 1 
print(i)

i = 0 
while i < len(city): 
	i += 1 
print(i)

earth = 0 
while earth < len(city): 
	earth += 1 
print(earth)

i = 0 
for x in city: 
	i += 1 
print(i)

i = 0 
for x in city: 
	i += 1 
for x in city: 
	i += 1
print(i)

i = len(city) 
while i > 0: 
	i -= 1 
print(i)

i = len(city) 
j = int(len(city)/2) 
while i > len(city[0:j]): 
	i -= 1 
print(i)

i = 0 
for x in city: 
	if x in vowels: 
		i += 1 
print(i)

i = 0 
for x in city: 
	if x not in consonants: 
		i += 1 
print(i)

i = 0 
for x in city: 
	if x not in consonants: 
		continue 
	else: 
		i += 1 
print(i)

i = 0 
for x in city: 
	if x in consonants: 
		i += 1
print(i)

i = 0 
for x in city: 
	if x not in consonants: 
		i += 1 
print(i)

i = 0 
j = 0 
for x in city: 
	if x in vowels: 
		j += 1 
	i += 1 
print(i)
print(j)

i = 0 
j = 0 
for x in city: 
	if x in vowels: 
		j *= 2 
	i += 1 
print(i)
print(j)

i = 0 
j = 0 
for x in city: 
	if x not in vowels: 
		j *= 1 
	i += 2 
print(i)
print(j)

i = 0 
j = 0 
for x in city: 
	if x == "e": 
		j *= 1 
	i += 1
print(i)
print(j)

i = 0 
j = 0 
for x in city: 
	if x != "e": 
		j *= 1 
	i += 1 
print(i)
print(j)

i = 0 
j = 0 
for x in city: 
	if x == "e": 
		break 
	i += 1 
print(i)
print(j)

i = 0 
j = 0 
k = 0 
for x in city: 
	j = 0 
	while j < len(city): 
		k += 1 
		j += 1 
	i += 1
print(i)
print(j)
print(k)

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
print(i)
print(j)
print(k)
print(a)

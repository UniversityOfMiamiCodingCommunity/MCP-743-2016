#Assignment for 2/15/17



Dict = { }
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

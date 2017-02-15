city = "sacramento"
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

# 4) What is the value of c? ################################################################################# b = int(len(city)/2)
d=b-1
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

# 10) What is the value of i after the statement is evaluated? ################################################################################# i=0
i = 0
if "e" in city:
	i += 1
print(i)

# 11) What is the value of i after the statement is evaluated? ################################################################################# i=0
i = 0	
if "e" not in consonants:
	i += 1
print(i)

# 12) What is the value of i after the statement is evaluated? ################################################################################# i=0
i = 0
if "e" not in city:
	i += 1 
else:
	i -= 1
print(i)

# 13) What is the value of i after the while loop runs to completion? # There are three statements (i.e. lines) in this loop.
# 14) Which statement is inside the loop?
# 15) Which statement is outside the loop?
# 16) What is the term that describes the expression (i < len(city))? ################################################################################# i=0
i = 0
while i < len(city):
	i += 1
print(i)

# 17) What is the value of earth after the while loop runs to completion?
#################################################################################
earth = 0
while earth < len(city):
	earth += 1
print(earth)


# 18) What is the value of i after the for loop runs to completion? ################################################################################# i=0
i = 0
for x in city:
	i += 1
print(i)

# 19) What is the value of i after this code runs to completion? ################################################################################# i=0
i = 0
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

# 22) What is the value of i after this code runs to completion? ################################################################################# i=0
i = 0
for x in city:
	if x in vowels:
		i += 1
print(i)

# 23) What is the value of i after this code runs to completion? ################################################################################# i=0
i = 0
for x in city:
	if x not in consonants:
		i += 1
print(i)

# 24) What is the value of i after this code runs to completion? ################################################################################# i=0
i = 0
for x in city:
	if x not in consonants:
		continue
	else:
		i += 1
print(i)

# 25) What is the value of i after this code runs to completion? ################################################################################# i=0
i = 0
for x in city:
    if x in consonants:
        i += 1
print(i)

# 26) What is the value of i after this code runs to completion? ################################################################################# i=0
i = 0
for x in city:
    if x not in consonants:
        i += 1
print(i)

# 27) What are the values of i and j after this code runs to completion? ################################################################################# i=0
i = 0
j=0
for x in city:
	if x in vowels:
		j += 1 
	i += 1
print("i=", i)
print("j=", j)	

# 28) What are the values of i and j after this code runs to completion? ################################################################################# i=0
i = 0
j=0
for x in city:
	if x in vowels:
		j *= 2
	i += 1
print("i=", i)
print("j=", j)	

# 29) What are the values of i and j after this code runs to completion? ################################################################################# i=0
i=0
j=0
for x in city:
	if x not in vowels:
		j *= 1 
	i += 2
print("i=", i)
print("j=", j)

# 30) What are the values of i and j after this code runs to completion? ################################################################################# i=0
i=0
j=0
for x in city:
	if x == "e":
		j *= 1 
	i += 1
print("i=", i)
print("j=", j)

# 31) What are the values of i and j after this code runs to completion? ################################################################################# i=0
i=0
j=0
for x in city:
	if x != "e":
		j *= 1 
	i += 1
print("i=", i)
print("j=", j)

# 32) What are the values of i and j after this code runs to completion? ################################################################################# i=0
i=0
j=0
for x in city:
	if x == "e":
		break 
	i += 1
print("#32i=", i)
print("#32j=", j)

# 33) What are the values of i, j, k after this code runs to completion? ################################################################################# i=0
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

# 34) What are the values of i, j, k, a after this code runs to completion? ################################################################################# i=0
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


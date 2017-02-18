# Date: 2017.01.28
###################

<<<<<<< HEAD
#####################################################################################################################
=======
>>>>>>> refs/remotes/origin/master
# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

#################################################################################
# Numbers
# If you need help or need to explore something new regarding numbers start here:
# Introduction: https://docs.python.org/3/tutorial/introduction.html#strings
# String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
#################################################################################

# Strings are sequences of characters concatenated into "words". 
# They are assigned and indicated using either single or double quotes. 
#######################################################################
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/master
startCodon = "ATG"
dna = "GTCAATGAACATAGACATGCTGCCATGCGAGTATATGCACCGTAGATAACTGCTAGCCCGGGCCAATTAGCCGGG"

# Because strings are sequences, the positions in the string are indexed from 0 to n.
# In the string "ATG", A is at index 0, T is at index 1, and G is at index 2.
# You can access a specific character (or portion) of a string using indices.
# Here are some examples:
#####################################################################################
# Get the individual bases of the string variable startCodon.
#############################################################
firstBase = startCodon[0]
secondBase = startCodon[1]
thirdBase = startCodon[2]
firstAndSecondBase = startCodon[0:2] # this is called a slice
secondAndThirdBase = startCodon[1:] # a second number is not needed because you are slicing to the end of the string
thirdBase = startCodon[-1] # you can also index from the reverse direction in the string

# The most widely used method for combining strings, known as concatenation, is to add them together. 
#####################################################################################################
allThreeBases = firstBase + secondBase + thirdBase
print("Concatenated bases:", allThreeBases)

# A common trick!
# Say you wanted every character in the string but the last, which is useful for removing "\n" from file lines.
# This slicing technique works and you will use it millions of times.
###############################################################################################################
thirdBase = startCodon[0:-1] # give me a new string missing the last character
print("Missing last index:", thirdBase)

# There is an extensive library of string methods, that enable you to manipulate and work with strings. 
# The methods are listed and described at: https://docs.python.org/3/library/stdtypes.html#string-methods
# When you are coding, you are usually solving a specific problem related to your unique research.
# Searching the string methods library for a method you can use will often be a part of that process. 
# After many years of coding, I still search the string methods library for desired functionality. 
# If the function you need does not exist in the string methods library, you will have to write it yourself.
# Below are a few working examples of how to use the string methods library. 
############################################################################################################ 

##########################################################################################################################
# The syntax for using string library methods, or any method for that matter, is dot accession:
# <your string name here>.method()
# Sometimes the methods take arguments, sometimes they don't. 
# Whether or not a method accepts arguments is fully described for each method on the string-methods web page cited above.
##########################################################################################################################

# In this example I will use the string "find" method.
# The objective is to use this method to find the first instance of the "startCodon" variable in the string "dna".
# The find method accepts an argument (i.e. startCodon): the string you are trying to find!  
###########################################################################################################################
result1 = dna.find(startCodon) # this method returns the start index of the query string if it is found
result2 = dna.find("Dan") # if the query string is not found, it returns -1 in Python2.7, and may return False in Python3.0

# Let's shake things up a bit to find stop codons in the DNA using a for loop.
##############################################################################
stopCodons = ["TAG", "TGA", "TAA"]
for stopCodon in stopCodons:
	stopCodonSearchResult = dna.find(stopCodon)
	print("Found stop codon (method 1):", stopCodon)

# Here is another way to search for the stop codons that doesn't use the find() method.
# You will use this version more often that find in your scientfic coding.
########################################################################################
for stopCodon in stopCodons:
	if stopCodon in dna:
		print("Found stop codon (method 2):", stopCodon)

# Here is a version that searches for each stop codon, and also finds the index at which it they occur.
# This code also counts the total number of stop codons that are encountered.
#######################################################################################################
stopCodonCount = 0
for stopCodon in stopCodons:
	# This is while loop. It will keep looping as long as the statement after "while" keyword is true.
	# Note: len() is a built-in Python function that returns the length of strings, list, and dictionaries.
	# See this page for the full list of built-in functions: https://docs.python.org/3/library/functions.html
	######################################################################################################### 
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == stopCodon:
			print("Found stop codon (method 3)", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			stopCodonCount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)

# There are many other string methods. 
# Here are examples of a few more so that you can see how they work. 
####################################################################
# Convert the dna string variable from upper case to lower case.
################################################################
dnaLowerCase = dna.lower() # note that the dna string variable is still in upper case
print("DNA sequence in lower case:", dnaLowerCase)
# Count the number of potential start codons in the string variable DNA.
########################################################################
startCodonCount = dna.count(startCodon)

# By far, the most important string variable method for your programming will be the split() method.
####################################################################################################
testString = "At the end of 8 weeks you will all be dangerous programmers."
print(testString.split()) # split with no arguments divides the string into a list object by its empty spaces
print(testString.split("8")) # you can split a string using a substring it contains
print(testString.split("weeks you will")) # another example using a substring to split a string

# A practical example of using split: this is relevant to how you will parse information from data files.
##########################################################################################################
examplePdbFileLine1 = "ATOM     11  N   PRO A   7     -10.147  38.272   8.252  1.00 71.52           N"
examplePdbFileLine2 = "ATOM     11  C   PRO A   7     -11.147  39.272   9.252  1.00 71.52           N"
# Parse and do type conversions on line 1.
##########################################
splitExamplePdbFileLine1 = examplePdbFileLine1.split() # split the string by empty space
xCoordinateAsString1 = splitExamplePdbFileLine1[6] # just like strings, you can access the elements of a list by their index
yCoordinateAsString1 = splitExamplePdbFileLine1[7]
zCoordinateAsString1 = splitExamplePdbFileLine1[8]
# Using the built-in Python function float() to convert each coordinate from a string type to a float type. 
# Note: there are built-in functions for converting to each standard type: str(), list(), int(), float().
# Again, you will find these built-in functions listed here: https://docs.python.org/3/library/functions.html
#############################################################################################################
x1 = float(xCoordinateAsString1) # string to float type conversion
y1 = float(yCoordinateAsString1)
z1 = float(zCoordinateAsString1)
# Parse and do type conversions on line 2.
##########################################
splitExamplePdbFileLine2 = examplePdbFileLine2.split() 
xCoordinateAsString2 = splitExamplePdbFileLine2[6] 
yCoordinateAsString2 = splitExamplePdbFileLine2[7]
zCoordinateAsString2 = splitExamplePdbFileLine2[8]
x2 = float(xCoordinateAsString2)
y2 = float(yCoordinateAsString2)
z2 = float(zCoordinateAsString2)

# Measure the distance, in Angstroms, between the two atoms.
############################################################
# Import the sqrt function from the Python math library module. I will teach you more about libraries/modules in class.
#######################################################################################################################
from math import sqrt # This is how you import the sqrt function from the Python math library.
distance = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) # This is the equation for the distance between two 3D-points.
print("The distance between the two atoms is:", distance, "Angstroms")

########################################################################################################################
# Assignment
<<<<<<< HEAD
# 1) Identify the index of each start codon in the DNA sequence provided below. ***DONE
# 2) Get the index of the first start codon. ***DONE
# 3) Identify the index of each stop codon. ***DONE
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence. ***DONE
# 5) Count the number of G bases. ***DONE
# 6) Identify each index that corresponds to an A base.  *DONE
# 7) Identify the length of the DNA sequence. ***DONE
# 8) Split the DNA sequence into a list using the start codon. ***DONE
# Note: all of the answers to this assignment are directly or indirectly provided in the code above.
#########################################################################################################################


dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

startcodon = "ATG"

#1 index of each start codon

startcodonCount = 0
for startCodon in startcodon:
	# This is while loop. It will keep looping as long as the statement after "while" keyword is true.
	# Note: len() is a built-in Python function that returns the length of strings, list, and dictionaries.
	# See this page for the full list of built-in functions: https://docs.python.org/3/library/functions.html
	######################################################################################################### 
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == startcodon:
			print("Found start codon", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			startcodonCount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of start codons found in the DNA sequence is:", startcodonCount)

#Kicked back; 20, 38, 48 and 78. 




# 2) Index of first start codon

startcodon = "ATG" 
print(dna.find(startcodon))

#kicked back "20"- first start coodon starts at position 20. However, I see 4 of them

startCodonCount = (dna.count(startcodon))
print(startCodonCount)

#confirmed there are 4 start codons




# 3) Identify index of each stop codon

stopcodon = ['TAG', 'TGA','TAA']

stopcodon1 = 'TAG' 
stopcodon2 = 'TGA' 
stopcodon3 = 'TAA'

print(stopcodon)


print(dna.find(stopcodon1))
Codon1count = (dna.count(stopcodon1))
print(Codon1count)

# TAG is at index 70, but there are 2



print(dna.find(stopcodon2))
Codon2count = (dna.count(stopcodon2))
print(Codon2count)

#TGA is at index 39, but there are 2 



print(dna.find(stopcodon3))
Codon3count = (dna.count(stopcodon3))
print(Codon3count)


#TAA is at index 7, but there are 5


stopcodon = ['TAG', 'TGA','TAA']

stopCodonCount = 0
for stopcodon in stopcodon:
	# This is while loop. It will keep looping as long as the statement after "while" keyword is true.
	# Note: len() is a built-in Python function that returns the length of strings, list, and dictionaries.
	# See this page for the full list of built-in functions: https://docs.python.org/3/library/functions.html
	######################################################################################################### 
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i + 3]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == stopcodon:
			print("Found stop codon", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			stopCodonCount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)

#TAG at 70 and 89, TGA at 39 and 75, TAA at 7, 36, 65, 81, 85. There are 9 stop codons



#4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.

#want only index of TGA at position 39...

stopcodon = "TGA", "TAG", "TAA"
stopcodon2 = "TGA" 
print(dna.find(stopcodon2))

stopCodonCount = 0
for stopcodon in stopcodon:
	# This is while loop. It will keep looping as long as the statement after "while" keyword is true.
	# Note: len() is a built-in Python function that returns the length of strings, list, and dictionaries.
	# See this page for the full list of built-in functions: https://docs.python.org/3/library/functions.html
	######################################################################################################### 
	i = 0
	while i < len(dna):
		iCodon = dna[39:i + 3]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == stopcodon:
			print("Found stop codon", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			stopCodonCount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)



#5: find "G's" 

base = "G"

print(dna.find(base))
#Base 'G' at position 0

Gcount = (dna.count(base))
print(Gcount)

#Kicked back 23, there are 23 G bases.




#6 Identify each index that corresponds to an A base.


Abase = "A"

AbaseCount = 0
for Abase in Abase:
	# This is while loop. It will keep looping as long as the statement after "while" keyword is true.
	# Note: len() is a built-in Python function that returns the length of strings, list, and dictionaries.
	# See this page for the full list of built-in functions: https://docs.python.org/3/library/functions.html
	######################################################################################################### 
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == Abase:
			print("Found A base", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			AbaseCount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of A bases found in the DNA sequence is:", AbaseCount)

#Kicked back 37, there are 37 A bases. Kicked back indexes: 2,8,9,10, 11,15,16,17,18, 19,20,24,25, 28,35,37, 38, 41,42,43,48,57,60,63,66,67,69, 71,77,78, 82,83,84,86,87,88,90



#7) Length of Sequence
baseA = 'A' 
baseT = 'T'
baseC = 'C' 
baseG ='G'
Acount = (dna.count(baseA))
Tcount = (dna.count(baseT))
Ccount = (dna.count(baseC))
Gcount = (dna.count(baseG))
print (Acount)
print (Tcount)
print (Ccount)
print (Gcount)

# 37, 18, 17 ,23, add them: 

length = (Acount + Tcount + Ccount + Gcount)
print(length)

#95 bases in DNA sequence- simplier way...

total = len(dna)
print(total)




#8 Split the DNA sequence into a list using the start codon

dna2 = "G G A C G T T T A A A A G G G A A A A A A T G G A A C C A C C C G G G A T A A T G A A A T T T T A T G G G C C C C A C C A G G A C T A A G A T A G C G T G A A T G T A A A T A A A T A G C C C"

print(dna2.split())
print (dna.split(startcodon))

#Split at each start codon, kicked back 4 lists. 
=======
=======
# 1) Identify the index of each start codon in the DNA sequence provided below. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon.
>>>>>>> refs/remotes/origin/master
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# 5) Count the number of G bases. 
# 6) Identify each index that corresponds to an A base.  
# 7) Identify the length of the DNA sequence. 
# 8) Split the DNA sequence into a list using the start codon. 
# Note: all of the answers to this assignment are directly or indirectly provided in the code above.
<<<<<<< HEAD

=======
#########################################################################################################################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
>>>>>>> refs/remotes/origin/master

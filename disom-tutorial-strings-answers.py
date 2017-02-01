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
result1 = dna.find(startCodon) # this methods return the start index of the query string if it is found
result2 = dna.find("Dan") # if the query string is not found, it returns -1 in Python2.7, and may return False in Python3.0

# Let's shake things up a bit to find stop codons in the DNA using a for loop.
##############################################################################
stopCodons = ["TAG", "TGA", "TAA"]
for stopCodon in stopCodons:
	stopCodonSearchResult = dna.find(stopCodon)
	print("Found stop codon (method 1):", stopCodon)

# Here is another way to search for a string that doesn't use the find method.
# You will use this version more often that find in your scientfic coding.
##############################################################################
for stopCodon in stopCodons:
	if stopCodon in dna:
		print("Found stop codon (method 2):", stopCodon)

# Here is a version that searches for the stop codon, and also finds the index at which it occurs.
# This code also counts the total number of stop codons that are encountered.
##################################################################################################
stopCodonCount = 0
for stopCodon in stopCodons:
	# This is while loop. It will keep running as long as the statement after "while" keyword is true.
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
# Here are exampls of a few more so that you can see how they work. 
###################################################################
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
print(testString.split()) # split with no arguments divides the string by its empty spaces into a list object
print(testString.split("8")) # you can split a string using a substring it contains
print(testString.split("weeks you will")) # another example using a substring

# A practical example of using split: this is relevant to how you will parse information from data files.
##########################################################################################################
examplePdbFileLine1 = "ATOM     11  N   PRO A   7     -10.147  38.272   8.252  1.00 71.52           N"
examplePdbFileLine2 = "ATOM     11  C   PRO A   7     -11.147  39.272   9.252  1.00 71.52           N"
# Parse and do type conversions on line 1.
##########################################
splitExamplePdbFileLine1 = examplePdbFileLine1.split() # split the string by empty space
xCoordinateAsString1 = splitExamplePdbFileLine1[6] # just like strings, you can access the elements of a list by index
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
# 1) Identify the index of each start codon in the DNA sequence provided below. 
# 2) Get the index of the first start codon.
# 3) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# 4) Count the number of G bases. 
# 5) Identify each index that corresponds to an A base.  
# 6) Identify the length of the DNA sequence. 
# 7) Split the DNA sequence into a list using the start codon. 
# Note: all of the answers to this assignment are directly or indirectly provided in the code above.
#########################################################################################################################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

# 1)
i = 0
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	# If the current codon is equal to (double == in Python), then tell me so. 
	##########################################################################
	if iCodon == startCodon:
		print("Found start codon", iCodon, "at index", i) 
	# Increment the index counter (i += 1 is shorthand for saying i = i + 1.
	########################################################################
	i += 1

# 2)
# Using the string method find()...
###################################
startCodonIndex = dna.find(startCodon)
print("The index of the first start codon is:", startCodonIndex)

# 3) 
minStopCodon, minStopCodonIndex = "", 10000000 # variables for storing the answer
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == stopCodon:
			stopCodonIndex = i
			# Uses the modulo operation (%) to identify substring slices exactly divisible by 3.
			####################################################################################
			if ((stopCodonIndex + 3) - startCodonIndex) % 3 == 0:
				# The condition was true, so a stop codon has been found. 
				# Record the find by resetting minStopCodon and minStopCodonIndex
				#################################################################
				minStopCodon = iCodon
				minStopCodonIndex = stopCodonIndex
				print("In frame codon is:", iCodon, i)
				break # Once you find the first instance of each codon type, you can quit the loop
		# Increment the index counter.
		##############################
		i += 1
print("The first in frame stop codon is:", minStopCodon, "at index", minStopCodonIndex)

# 4) 
# Using the string method count()...
####################################
numberOfGs = dna.count("G")
print("The numbers of G bases in the DNA sequence is:", numberOfGs)

# 5)
i = 0 
aIndices = []
for base in dna:
	# If the current base is equal to A...
	######################################
	if base == "A":
		# Save the index in the list aIndices.
		######################################
		aIndices.append(i)
	i += 1
print("Indices of A bases in the DNA sequence:", aIndices)

#6) 
# Using the built-in function len()...
######################################
dnaLength = len(dna)
print("The length of the DNA sequence is:", dnaLength)

#7)
# Using the string method split()...
#################################### 
splitDnaOnStartCodons = dna.split(startCodon)
print("DNA sequence split by start codon:", splitDnaOnStartCodons)





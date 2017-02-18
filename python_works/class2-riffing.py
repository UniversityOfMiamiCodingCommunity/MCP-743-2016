# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
#################################################################

# Numbers
# https://docs.python.org/3/tutorial/introduction.html#numbers
##############################################################
#select, right click, format, commit lines or ctrl E
a = 1
b = 1
print(a + b)
a = 2
print(a + b)
#Floor, no decimals
a = 17 // 3
print(a)
#Remainder
a = 17 % 3
print(a)
#Normal Value, have decimals
a = 17 / 3
print(a)
 

# Strings
# Introduction: https://docs.python.org/3/tutorial/introduction.html#strings
# List Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
##############################################################################

startcodon = "ATG"
stopCodons = ["TAG","TGA", "TAA"]
dna = "GTCAAACATAGACATGCTGCCCGAGTATCACCGTAGACTGC"
print(dna.find(startcodon))
#kicked back 13, ATG starts after 14th position (start with 0)
atgStartIndex = dna.find(startcodon)
#Show me character at atgstartindex
print(dna [atgStartIndex])
# FShow me first start codon is in the string dna. can count in for eithe direction
print(dna [atgStartIndex:atgStartIndex + 3])

#Test string dna for lowercase, "False" cause there are no lowercase letters
print(dna.islower ())
#change form uppercase to lowercase
dnaLower = dna.lower()
print(dnaLower)
print(dna)



# The MOST IMPORTANT string method!!!
##################################### SPLIT, converts string to list (put in empty spaces)

dna2 = "G T C A A A C A T A G A C A T G C T G C C C G A G T A T C A C C G T A G A C T G C"
print(dna2.split())
print (dna.split(startcodon))
#Everything be4 ATG, then everything after


# \t is tab   \n is new line

# Lists
# Introduction: https://docs.python.org/3/tutorial/introduction.html#lists
# List Methods: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
####################################################################################

#Loop

testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for trump in testList:
	if trump == 5:
		print("hello")
	elif trump == 7:
		print("you're lucky")
	else:
		print("Lord help us")
	
 #dont use "in" or "for" for lists variable



# Reading and writing files.
# Introduction: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#############################################################################################

# Control flow statements
# while loop: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
# Introduction: https://docs.python.org/3/tutorial/controlflow.html
################################################################################################## 

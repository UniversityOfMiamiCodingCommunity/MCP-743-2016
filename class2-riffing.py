# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
#################################################################

# Numbers
# https://docs.python.org/3/tutorial/introduction.html#numbers
##############################################################
# a = 1
# b = 1
# print a + b
# a = 2
# print a + b

# Strings
# Introduction: https://docs.python.org/3/tutorial/introduction.html#strings
# String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
##############################################################################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GTCAAACATAGACATGCTGCCCGAGTATCACCGTAGACTGC"

# Find where the first start codon is in the string dna.
atgStartIndex = dna.find(startCodon)
# Show me the character at index atgStartIndex.
print dna[atgStartIndex]
print dna[atgStartIndex:atgStartIndex + 3]

# Test string dna for lowercase
print dna.islower()

# Change string dna from uppercase to all lowercase
dnaLower = dna.lower()
print dnaLower
print dna

# The MOST IMPORTANT string method!!!
#####################################
dna2 = "G T C A A A C A T A G A C A T G C T G C C C G A G T A T C A C C G T A G A C T G C"
print dna2.split()
print dna.split(startCodon)

atom = "ATOM     11  N   PRO A   7     -10.147  38.272   8.252  1.00 71.52           N"
print atom.split()
xCoordinate = atom.split()[6]
yCoordinate = atom.split()[7]
# Convert each coordinate from a string type to a float type.
print "\n\n"
print xCoordinate, yCoordinate, xCoordinate + yCoordinate
xCoordinate = float(xCoordinate)
yCoordinate = float(yCoordinate)
print xCoordinate + yCoordinate

# Lists
# Introduction: https://docs.python.org/3/tutorial/introduction.html#lists
# List Methods: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
####################################################################################
exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print "\n\n"
for trump in exampleList:
	if trump == 5:
		print trump, "hello"
	elif trump == 7:
		print trump, "your lucky"
	else:
		print trump, "thank god trump is president"

# Reading and writing files.
# Introduction: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#############################################################################################

# Control flow statements
# while loop: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
# Introduction: https://docs.python.org/3/tutorial/controlflow.html
################################################################################################## 
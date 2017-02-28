#~ # Date: 2017.01.28
#~ ###################


###################################
# Start of ZPR assignment, strings.
###################################

########################################################################################################################
# Assignment
# 1) Identify the index of each start codon in the DNA sequence provided below. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon.
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# 5) Count the number of G bases. 
# 6) Identify each index that corresponds to an A base.  
# 7) Identify the length of the DNA sequence. 
# 8) Split the DNA sequence into a list using the start codon. 
# Note: all of the answers to this assignment are directly or indirectly provided in the code above.
#########################################################################################################################
startCodon = ["ATG"]
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"


# 1) Identify the index of each start codon in the DNA sequence provided below. 
#######################################################################
# Remember in order to do a while loop you must have what you are looking for in a list. 
# i.e. startCodon = ["ATG"] (must be in brackets cannot be open.)
#######################################################################
startCodonCount = 0
for startCodon in startCodon:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == startCodon:
			print("Found start codon", iCodon, "at index", i) 
			startCodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", startCodonCount)


#
print("\n")
#


# 2 Get the index of the first start codon.
#######################################################################
startCodon = "ATG"
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
result1 = dna.find(startCodon)
print("The first start codon 'ATG' appears at postion:", result1)

#
print("\n")
#

# 3 Identify the index of each stop codon.
#######################################################################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
stopCodons = ["TAG", "TGA", "TAA"]
stopCodonIndices = []

for stopCodon in stopCodons:
	i = 0
	while i < len(dna)-2:
		i = dna.find(stopCodon, i)
		if i == -1:
			break
		stopCodonIndices.append(i)
		i += 3
print("The stop codon indices are:", stopCodonIndices)
#


print("\n")

# 4 Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
#######################################################################
firstStartCodon = dna.find(startCodon)
lengthofDNA = len(dna)
readingFrame = list(range(firstStartCodon, lengthofDNA,3)) 

stopCodonIndices_in_readingFrame = [val for val in stopCodonIndices if val in readingFrame]
firstStopCodon_in_readingFrame = (min(stopCodonIndices_in_readingFrame))

print("The first in-frame stop codon is:",dna[firstStopCodon_in_readingFrame:firstStopCodon_in_readingFrame+3], "and its index position is", firstStopCodon_in_readingFrame)

#
print("\n")
#


	
# 5 Count the number of G bases.
#######################################################################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
guanine = "G"
guanineBasecount = dna.count(guanine)
print("The total number of guanines in the DNA sequence is:", guanineBasecount)


#
print("\n")
#


#6 Identify each index that corresponds to an A base.
#######################################################################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
(dna.split())

indices = [i for i, x in enumerate(dna) if x == "A"]
print("The base 'A' occurs at the following indices:", indices)


#
print("\n")
#



# 7 Identify the length of the DNA sequence.
#######################################################################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
print("The total number of bases in the DNA sequence is:", len(dna))


#
print("\n")
#




#8 Split the DNA sequence into a list using the start codon.
#######################################################################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
print(dna.split('ATG'))

dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"



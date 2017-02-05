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
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

# 1) Identify the index of each start codon in the DNA sequence
index = 0
startCodonIndices = []

while index < len(dna):
	index = dna.find(startCodon, index)
	if index == -1:
		break
	startCodonIndices.append(index)
	index += 3

print("Here is the index of each start codon:", startCodonIndices)

# 2) Get the index of the first start codon.
print("Here is the index of the first start codon:", dna.find(startCodon))

# 3) Identify the index of each stop codon.
stopCodonIndices = []

for stopCodon in stopCodons: # this lets you repeat the loop for each stop codon
	index = 0 # index starts at zero so it searches from the beginning of the line
	while index < len(dna)-2: # while the index is less than the length of dna -2 (so it doesn't search past end of sequence)
		index = dna.find(stopCodon, index) # search for the position of the stop codon and define that as index (overwrites)
		if index == -1: # breaks out in case loop gets stuck
			break
		stopCodonIndices.append(index) # append the index for the stop codon to the stopCodonIndices list
		index += 3 # add three to the index and overwrite the index so the loop starts searching again after this codon

print("Here is the index of each stop codon:", stopCodonIndices) # print out the list of the stop codons

# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
firstStartCodon = dna.find(startCodon) # identify and define index for first start codon
lengthofDNA = len(dna) # identify and define length of dna
readingFrame = list(range(firstStartCodon,lengthofDNA,3)) # create a list of the first index for each codon in the reading frame

stopCodonIndices_in_readingFrame = [val for val in stopCodonIndices if val in readingFrame] # create a list of indices for stop codons in reading frame
firstStopCodon_in_readingFrame = (min(stopCodonIndices_in_readingFrame)) # identify and define the lowest index of the above list

print("The first stop codon in the reading frame is", dna[firstStopCodon_in_readingFrame:firstStopCodon_in_readingFrame+3], "and it is located at position", firstStopCodon_in_readingFrame, ".") # print the three nucleotides starting at the index defined above

# 5) Count the number of G bases. 
countG = dna.count("G") # count the occurences of G in the string dna

print('There are', countG, 'guanine bases.') # output the count of G

# 6) Identify each index that corresponds to an A base.  
index = 0
aIndices = []

while index < len(dna):
	index = dna.find('A', index)
	if index == -1:
		break
	aIndices.append(index)
	index += 3

print("Here is the index of each A base:", aIndices)

# 7) Identify the length of the DNA sequence. 
print("The length of the DNA sequence is", len(dna), "nucleotides.")

# 8) Split the DNA sequence into a list using the start codon. 
print(dna.split(startCodon))




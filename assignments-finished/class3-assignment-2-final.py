########################################################################################################################
# Assignment
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

# 1) Identify the index of each start codon in the DNA sequence provided below. 

print("Question #1:")
i = 0
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		print("Start codon", iCodon, "at index", i)
	i += 1
print("The total number of start codons is", i)
print("\n")

# 2) Get the index of the first start codon.
print("Question #2:")
firstStartCodon = dna.find(startCodon)
print("The first start codon can be found at index", firstStartCodon)
print('\n')

# 3) Identify the index of each stop codon.
print("Question #3:")
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print("The stop codon", iCodon, "has been found at index", i)
		i += 1
print('\n')

# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
print("Question #4:")
stopCodonList = []
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			stopCodonIndex = i
			if ((i + 3) - 20) % 3 == 0:
				stopCodonList.append(i)
				# print("There is a stop codon that is in frame with the first start codon at index", i)
		i += 1
print("The first in-frame stop codon is", dna[min(stopCodonList) : min(stopCodonList) + 3], "and occurs at index", min(stopCodonList))

print('\n')

# 5) Count the number of G bases. 
print("Question #5:")
guanineCount = dna.count("G")
print("This DNA sequence contains", guanineCount, "guanines")
print("\n")

# 6) Identify each index that corresponds to an A base. 
print("Question #6:")
i = 0
for base in dna:
	adenine = "A"
	if base == adenine:
		print("There is an adenine at index", i)
	i += 1
print('\n')

# 7) Identify the length of the DNA sequence. 
print("Question #7:")
length = len(dna)
print('The length of the DNA sequence is', length, "base pairs")
print('\n')

# 8) Split the DNA sequence into a list using the start codon. 
print("Question #8:")
startCodonSplit = dna.split(startCodon)
print(startCodonSplit)

# Note: all of the answers to this assignment are directly or indirectly provided in the code above.
#########################################################################################################################

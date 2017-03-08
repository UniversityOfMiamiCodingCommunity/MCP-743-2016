########################################################################
# Assignment
# 1) Identify the index of each start codon in the DNA sequence 
# provided below. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon.
# 4) Identify the stop codon, and it's index that is in frame with the 
# first start codon encountered in the DNA sequence.
# 5) Count the number of G bases. 
# 6) Identify each index that corresponds to an A base.  
# 7) Identify the length of the DNA sequence. 
# 8) Split the DNA sequence into a list using the start codon. 
# Note: all of the answers to this assignment are directly or 
# indirectly provided in the code above.
########################################################################

startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

########################################################################

#  1)

index=0
while index < len(dna) - 2:
	codon=dna[index:index+3]
	if codon==startCodon:
		print(codon, index)
	index=index + 1

#  2)

startIndex=dna.find(startCodon)
print(startIndex)

#  3) and 4)

for stopCodon in stopCodons:
	index=0
	while index < len(dna) - 2:
		codon=dna[index:index+3]
		if codon==stopCodon:
			stopIndex = index
			if ((stopIndex + 3) - startIndex) % 3 == 0:
				firstStopCodon=codon
				firstStopCodonIndex=stopIndex
				print(codon, index)
		index=index + 1 
print("First in-frame stop codon: " + firstStopCodon, firstStopCodonIndex)

#  5)

Gs=dna.count("G")
print(Gs)

#  6)

index=0
As = []
for nucleo in dna:
	if nucleo == "A":
		As.append(index)
	index=index + 1
print(As)

#  7)

print(len(dna))

#  8)

print(dna.split(startCodon))

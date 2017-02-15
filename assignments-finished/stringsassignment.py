# # Date: 2017.01.28

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

# 1
i = 0
while True:
	i = dna.find(startCodon, i + 1)
	if i == -1: break
	print("Found start codon at index:", i)

# 2)
results1 = dna.find(startCodon)
print(results1)

#3
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print("Found stop codon", iCodon, "at index", i) 
		i += 1

#4
for stopCodon in stopCodons:
	i = dna.find(startCodon)
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			if ((i-19) + 2) % 3 == 0:
				print("Found stop codon", iCodon, "at index", i) 			
		i += 1
#Since it is the closest to the first start codon, TAA at position 65:67 is the first in frame stop codon
print("Found in frame stop codon TAA at index 65")

#5
G_bases = "G"
GCount = dna.count(G_bases)
print(GCount)

6
i = 0
while True:
	i = dna.find("A", i + 1)
	if i == -1: break
	print("Found A base at index:", i)

#7
print(len(dna))

#8
print(dna.split(startCodon))
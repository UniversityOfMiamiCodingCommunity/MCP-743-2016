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

#Question 1 - Identify the index of each start codon in the DNA sequence 
i = 0
j = len(dna)-2
while i < j:
	icodon = dna[i:i+3]
	if icodon == startCodon:
		print("Found startCodon", startCodon, "at index", i)
	i += 1

#Question 2 - Get the index of the first start codon
result1 = dna.find(startCodon)
print("First startCodon appears at index",result1)

#Question 3 - Identify the index of each stop codon
for stopCodon in stopCodons:
	i = 0
	while i <len(dna)-2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print("Found stopCodon", iCodon, "at index", i)
		i += 1

#Question 4 - Identify the stop codon, and it;s index that is in fram with the first start codon in the DNA sequence
for stopCodon in stopCodons:
	i = 0
	while i < len(dna)-2:
		sCodon = dna[i:i+3]
		if sCodon == stopCodon:
			if ((i + 3) - 20) % 3 == 0:
				print(i)
		i += 1
			

#Question 5 - Count the number of G bases
G_count = dna.count("G")
print("There are", G_count, "Guanines in the DNA sequence")

#Question 6 - Identify each index that corresponds to an A base
i = 0
while i < len(dna):
	A_base = dna[i:i+1]
	if A_base == "A":
		print("There is an Adenine at index", i)
	i += 1

#Question 7 - Identify the length of the DNA sequence
print("The length of the DNA sequence is:", len(dna), "nucleotides")

#Question 8 - Split the DNA sequence into a list using the start codon
print(dna.split(startCodon))

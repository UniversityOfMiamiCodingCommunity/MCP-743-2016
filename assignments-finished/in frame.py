#In frame, strings assignment question 4

dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]

#Found index of 1st start codon

startCodonIndex = dna.find(startCodon)
print(startCodonIndex)

#Find indencies of all stop codons

i = startCodonIndex
firststopCodonIndex = 0
firststopCodon = ""
while i < len(dna) - 2:
	iCodon = dna[i: i + 3]
	if iCodon in stopCodons:
		print(iCodon, i)
		firststopCodon = iCodon
		firststopCodonIndex = i
		break
	i += 1
print("The stop codon in frame with start codon is", firststopCodon, "at index", firststopCodonIndex)

#print intraspection is my best friend :)
	

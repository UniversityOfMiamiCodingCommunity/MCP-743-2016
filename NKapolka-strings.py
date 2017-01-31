##########################
# Nick's string assignment
##########################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

#~ for start in startCodon:
	#~ if start in dna:
		#~ print("Found start codon:", startCodon)
#~ print(startCodon)

# 1) Identify the index of each start codon in the DNA sequence provided below.
###############################################################################
i = 0
while i < len(dna) - 2:
	Codon = dna[i:i + 3]
	if Codon == startCodon:
		print("Identified start codon", Codon, "at index:", i)
	i += 1

# 2) Get the index of the first start codon.
############################################
startCodonIndex = dna.find(startCodon)
print("Identified first start codon in sequence at index:", startCodonIndex)

# 3) Identify the index of each stop codon.
###########################################
for stopCodon in stopCodons:
	i = 0
	while i <len(dna) -2:	
		Codon = dna[i:i + 3]
		if Codon == stopCodon:
			print("Identified stop codon", stopCodon, "at index:", i)
		i += 1

# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
#########################################################################################################################	
#~ print(' '.join([dnaORF[i:i+3] for i in range (0, len(dnaORF), 3)]))
#~ dnaSplitORF = ' '.join([dnaORF[i:i+3] for i in range (0, len(dnaORF), 3)])
#~ if stopCodon in dnaSplitORF:
	#~ print("Identified stop codon in frame:", stopCodon, "at index", i)

for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		Codon = dna[i:i + 3]
		if Codon == stopCodon:
			if ((i + 3) - 20) % 3 == 0:
				print("Identified stop codon", Codon, "in frame at index:", i)
		i += 1	

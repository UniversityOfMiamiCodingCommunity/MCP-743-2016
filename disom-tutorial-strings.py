
#########################################################################################################################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

# 1) Identify the index of each start codon in the DNA sequence provided below. 
startCodonCount = dna.count(startCodon)
print(startCodonCount)
startCodon1 = dna.find(startCodon)
sliceoffcount = startCodon1
dnaslice1 = dna[1+startCodon1:]
startCodon2 = dnaslice1.find(startCodon)
sliceoffcount1 = startCodon1+startCodon2+1
dnaslice2 = dnaslice1[1+startCodon2:]
startCodon3 = dnaslice2.find(startCodon)
sliceoffcount2 = startCodon1+startCodon2+startCodon3+2
dnaslice3 = dnaslice2[1+startCodon3:]
startCodon4 = dnaslice3.find(startCodon)
sliceoffcount3 = startCodon1+startCodon2+startCodon3+startCodon4+3
print(sliceoffcount,sliceoffcount1,sliceoffcount2,sliceoffcount3)

# 2) Get the index of the first start codon.
result2 = dna.find(startCodon)
print(result2)

# 3) Identify the index of each stop codon.
stopCodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == stopCodon:
			print("Found stop codon (method 3)", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			stopCodonCount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)

# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
print('The first stop codon is ' ,dna[7:10])
# 5) Count the number of G bases. 
result5 = dna.count("G")
print(result5)
# 6) Identify each index that corresponds to an A base.  
ABASEs = ["A"]
ABASECount = 0
for ABASE in ABASEs:
	i = 0
	while i < len(dna) - 0:
		iCodon = dna[i:i+1]
		# If the current codon is equal to (double == in Python), then tell me so. 
		##########################################################################
		if iCodon == ABASE:
			print("Found A Base (method 3)", iCodon, "at index", i) 
			# Increment the stop codon count.
			#################################
			ABASECount += 1
		# Increment the index counter.
		##############################
		i += 1
print("The total number of A Bases found in the DNA sequence is:", ABASECount)
# 7) Identify the length of the DNA sequence. 
result7 = len(dna)
print(result7)
# 8) Split the DNA sequence into a list using the start codon. 
result8 = dna.split("ATG")
print(result8)

# Note: all of the answers to this assignment are directly or indirectly provided in the code above.

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
#1
startCodonCount = 0
for startCodon1 in startCodon:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == startCodon1:
			print("Found start codon (method 3)", iCodon, "at index", i) 
			startCodonCount += 1
		i += 1
#2
startCodon = "ATG"
result2 = dna.find(startCodon)
print(result2)
#3 
stopCodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print("Found stop codon (method 3)", iCodon, "at index", i) 
			stopCodonCount += 1
		i += 1
#4
result4a = dna.find("TAG")
print(result4a)
result4b = dna.find("TGA")
print(result4b)
result4c = dna.find("TAA")
print(result4c)
answerfor4 = result4c
print (answerfor4)
#5
result5 = dna.count("G")
print(result5)
#6
As = ("A")
Ascount = 0
for A in As:
	i = 0
	while i < len(dna) - 0:
		iCodon = dna[i:i+1]
		if iCodon == A:
			print("Found A (method 3)", iCodon, "at index", i) 
			Ascount += 1
		i += 1
#7
result7 = len(dna)
print (result7)
#8
result8 = dna.split("ATG")
print (result8)xxx


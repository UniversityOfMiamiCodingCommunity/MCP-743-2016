startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

# 1
i = 0
while True:
	i = dna.find(startCodon, i + 1)
	if i == -1: break
	print("Start codon at index ", i)

# 2)
results2 = dna.find(startCodon)
print(results2)

#3
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print("Stop codon", iCodon, "at index", i) 
		i += 1

#4
for stopCodon in stopCodons:
	i = dna.find(startCodon)
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			if ((i-19) + 2) % 3 == 0:
				print("Stop codon", iCodon, "at index", i) 			
		i += 1
print("Found at index ",i)

#5
Gbase = "G"
Gcount = dna.count(Gbase)
print(Gcount)

#6
i = 0
while True:
	i = dna.find("A", i + 1)
	if i == -1: break
	print("Found A residue at index:", i)

#7
print(len(dna))

#8
print(dna.split(startCodon))
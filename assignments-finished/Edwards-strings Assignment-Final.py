#Strings Assignment (Final Version) :) ~Jazzy


dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

startcodon = "ATG"

#1 index of each start codon

i = 0
startcodonCount = 0
for startCodon in startcodon:
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == startcodon:
			print("Found start codon", iCodon, "at index", i) 
			startcodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", startcodonCount)

#Kicked back; 20, 38, 48 and 78. Four start codons




# 2) Index of first start codon

startcodon = "ATG" 
print(dna.find(startcodon))

#kicked back "20"- first start coodon starts at position 20.



# 3) Identify index of each stop codon


stopCodons = ['TAG', 'TGA', 'TAA']
stopCodonCount = 0
for stopCodon in stopCodons:
	i =0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			stopCodonCount += 1
			print("Found stop codon", iCodon, "at index", i)
		i += 1




#4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.


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





#5: find "G's" 

base = "G"

print(dna.find(base))
#Base 'G' at position 0

Gcount = (dna.count(base))
print(Gcount)

#Kicked back 23, there are 23 G bases.




#6 Identify each index that corresponds to an A base.


Abase = "A"

i = 0
AbaseCount = 0
for Abase in Abase:
	while i < len(dna) - 2:
		iCodon = dna[i]
		if iCodon == Abase:
			print("Found A base", iCodon, "at index", i) 
			AbaseCount += 1
		i += 1
print("The total number of A bases found in the DNA sequence is:", AbaseCount)

#Kicked back 37, there are 37 A bases. Kicked back indexes: 2,8,9,10, 11,15,16,17,18, 19,20,24,25, 28,35,37, 38, 41,42,43,48,57,60,63,66,67,69, 71,77,78, 82,83,84,86,87,88,90



#7) Length of Sequence
baseA = 'A' 
baseT = 'T'
baseC = 'C' 
baseG ='G'
Acount = (dna.count(baseA))
Tcount = (dna.count(baseT))
Ccount = (dna.count(baseC))
Gcount = (dna.count(baseG))
print (Acount)
print (Tcount)
print (Ccount)
print (Gcount)

# 37, 18, 17 ,23, add them: 

length = (Acount + Tcount + Ccount + Gcount)
print(length)

#95 bases in DNA sequence- simplier way...

total = len(dna)
print(total)




#8 Split the DNA sequence into a list using the start codon

dna2 = "G G A C G T T T A A A A G G G A A A A A A T G G A A C C A C C C G G G A T A A T G A A A T T T T A T G G G C C C C A C C A G G A C T A A G A T A G C G T G A A T G T A A A T A A A T A G C C C"

print(dna2.split())
print (dna.split(startcodon))

#Split at each start codon, kicked back 4 lists. 


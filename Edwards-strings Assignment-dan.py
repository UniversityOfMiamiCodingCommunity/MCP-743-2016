#Strings Assignment


dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"


# Approach #1
#############################
startCodons = ["ATG"]

#1 index of each start codon

i = 0
startcodonCount = 0
for startCodon in startCodons:
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == startCodon:
			print("Found start codon", iCodon, "at index", i) 
			startcodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", startcodonCount)

# Approach #2
##############################
startCodon = "ATG"

#1 index of each start codon

i = 0
startcodonCount = 0
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		print("Found start codon", iCodon, "at index", i) 
		startcodonCount += 1
	i += 1
print("The total number of start codons found in the DNA sequence is:", startcodonCount)

#Kicked back; 20, 38, 48 and 78. Four start codons

# 2) Index of first start codon

startcodon = "ATG" 
print("First start codon index", dna.find(startcodon))

#kicked back "20"- first start coodon starts at position 20. However, I see 4 of them

# startCodonCount = (dna.count(startcodon))
# print(startCodonCount)

#confirmed there are 4 start codons




#~ # 3) Identify index of each stop codon

#~ stopcodon = ['TAG', 'TGA','TAA']

#~ stopcodon1 = 'TAG' 
#~ stopcodon2 = 'TGA' 
#~ stopcodon3 = 'TAA'

#~ print(stopcodon)


#~ print(dna.find(stopcodon1))
#~ Codon1count = (dna.count(stopcodon1))
#~ print(Codon1count)

#~ # TAG is at index 70, but there are 2



#~ print(dna.find(stopcodon2))
#~ Codon2count = (dna.count(stopcodon2))
#~ print(Codon2count)

#~ #TGA is at index 39, but there are 2 



#~ print(dna.find(stopcodon3))
#~ Codon3count = (dna.count(stopcodon3))
#~ print(Codon3count)


#~ #TAA is at index 7, but there are 5

stopCodons = ['TAG', 'TGA', 'TAA']

stopCodonIndices = []
for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print ("Found stop codon", stopCodon, "at index", i)
			stopCodonIndices.append(i)
		i += 1

# stopcodon1 = 'TAG' 
# stopcodon2 = 'TGA'
# stopcodon3 = 'TAA'

# i = 0
# stopCodonCount = 0
# for stopcodon in stopcodon1:
# 	while i < len(dna) - 2:
# 		iCodon = dna[i:i + 3]
# 		if iCodon == stopcodon1:
# 			print("Found stop codon", iCodon, "at index", i) 
# 			stopCodonCount += 1
# 		i += 1
# print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)

# i = 0
# stopCodonCount = 0
# for stopcodon in stopcodon2:
# 	while i < len(dna) - 2:
# 		iCodon = dna[i:i + 3]
# 		if iCodon == stopcodon2:
# 			print("Found stop codon", iCodon, "at index", i) 
# 			stopCodonCount += 1
# 		i += 1
# print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)


# i = 0
# stopCodonCount = 0
# for stopcodon in stopcodon3:
# 	while i < len(dna) - 2:
# 		iCodon = dna[i:i + 3]
# 		if iCodon == stopcodon3:
# 			print("Found stop codon", iCodon, "at index", i) 
# 			stopCodonCount += 1
# 		i += 1
# print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)



#TAG at 70 and 89, TGA at 39 and 75, TAA at 7, 36, 65, 81, 85. There are 9 stop codons




#4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.

#want only index of TGA at position 39...

#~ stopcodon = "TGA", "TAG", "TAA"
#~ stopcodon2 = "TGA" 
#~ print(dna.find(stopcodon2))

#Don't understand this question




#~ i = 0
#~ stopCodonCount = 0
#~ for stopcodon in stopcodon:
	#~ # This is while loop. It will keep looping as long as the statement after "while" keyword is true.
	#~ # Note: len() is a built-in Python function that returns the length of strings, list, and dictionaries.
	#~ # See this page for the full list of built-in functions: https://docs.python.org/3/library/functions.html
	#~ ######################################################################################################### 
	#~ while i < len(dna):
		#~ iCodon = dna[39:i + 3]
		#~ # If the current codon is equal to (double == in Python), then tell me so. 
		#~ ##########################################################################
		#~ if iCodon == stopcodon:
			#~ print("Found stop codon", iCodon, "at index", i) 
			#~ # Increment the stop codon count.
			#~ #################################
			#~ stopCodonCount += 1
		#~ # Increment the index counter.
		#~ ##############################
		#~ i += 1
#~ print("The total number of stop codons found in the DNA sequence is:", stopCodonCount)





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

#95 bases in DNA sequence- simplier way...

total = len(dna)
print(total)

len(dna)



#8 Split the DNA sequence into a list using the start codon

dna2 = "G G A C G T T T A A A A G G G A A A A A A T G G A A C C A C C C G G G A T A A T G A A A T T T T A T G G G C C C C A C C A G G A C T A A G A T A G C G T G A A T G T A A A T A A A T A G C C C"

print(dna2.split())
print (dna.split(startcodon))

#Split at each start codon, kicked back 4 lists. 


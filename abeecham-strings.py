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

## 1) Identify the index of each start codon in the DNA sequence provided below.

print 'Question 1'
i = 0
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		print "Found start codon " + str(iCodon) + " at index " + str(i) 
	# Increment the index counter.
	##############################
	i += 1
		
## 2) Get the index of the first start codon.

firststart = dna.find(startCodon)
print '\n'
print 'Question 2'
print 'The first start codon is found at index ' + str(firststart)

## 3) Identify the index of each stop codon.

print '\n'
print 'Question 3'
for stopCodon in stopCodons: 
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			print "Found stop codon " + str(iCodon) + " at index " + str(i) 
		# Increment the index counter.
		##############################
		i += 1
		
## 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.

print '\n'
print 'Question 4'
ORF = dna[firststart:]	
index=[]
for stopCodon in stopCodons:
	stopCodonSearchResult = ORF.find(stopCodon)
	index.append(stopCodonSearchResult)
minimum = min(index)
codon_label = ORF[minimum:minimum+3]
final_index = firststart + minimum	
print "The stop codon that is in frame with the first start codon is " + codon_label + ", located at index " + str(final_index)

## 5) Count the number of G bases.

print '\n'
print 'Question 5'
BaseCount = 0
BaseLabel = 'G'
i = 0
while i < len(dna):
	iCodon = dna[i]
	if iCodon == BaseLabel:
		BaseCount += 1
	i += 1
print "The total number of " + BaseLabel + " found in the DNA sequence is: " + str(BaseCount)

## 6) Identify each index that corresponds to an A base.
	
print '\n'
print 'Question 6'
BaseLabel = 'A'
i = 0
while i < len(dna):
	iCodon = dna[i]
	if iCodon == BaseLabel:
		print "Found base " + BaseLabel + " at index " + str(i)
	i += 1
	
## 7) Identify the length of the DNA sequence.

print '\n'
print 'Question 7'
dna_length = len(dna)
print "The length of the DNA sequence is " + str(dna_length)	

## 8) Split the DNA sequence into a list using the start codon.

print '\n'
print 'Question 8'
dna_split = dna.split(startCodon)
print dna_split

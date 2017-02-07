# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################
from os import sep
fileInput = open("dataFiles" + sep + "sequence-p53.fasta", "r")

dna = ""
for line in fileInput:
	dna += line[0:-1]
#print(dna)
#print("\n")

# 2)
# Find all possible start codons in parsed DNA sequence.
start_codon = "ATG"
total_start_codon = dna.find('ATG')
#print("Total number of start codons in this sequence is:", total_start_codon)

start_codon_count = 0
while start_codon_count < len(dna):
    start_codon_count = dna.find('ATG', start_codon_count)
    if start_codon_count == -1:
        break
    #print('Start codon found at index', start_codon_count)
    start_codon_count += 2
#print("\n")

#in terminal: to redirect output:
#python hw2-class4.py > startCodonIndices.txt


# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
stop_codons = ["TAG", "TGA", "TAA"]

stop_codon_count = 0
for stop_codon in stop_codons:
	i = 0
	while i < len(dna) -2:
		iCodon = dna[i:i+3]
		if iCodon == stop_codon:
			#print("Found stop codon", iCodon, "at index", i)
			stop_codon_count += 1
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stop_codon_count)
print("\n")

stop_codon_count = 0
for stop_codon in stop_codons:
	i = 0
	while i < len(dna) -2:
		iCodon = dna[i:i+3]
		if iCodon == stop_codon:
			print("Found stop codon", iCodon, "at index", i)
			stop_codon_count += 1
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stop_codon_count)
print("\n")


#in terminal: to redirect output:
#python hw2-class4.py > stopCodonIndices.txt


# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################


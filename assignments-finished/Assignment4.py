from os import listdir

# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################

fileInput = open('sequence-p53.fasta', "r")
dna = ""
for line in fileInput:
	if line[0] == ">":
		continue
	dna += line[0:-1]
print(dna)

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

startCodon = "ATG"
startCodonCount = dna.count(startCodon)
startCodonList = []

i = 0
while i < len(dna)-2:
	codon = dna[i:i+3]
	if codon == startCodon:
		startCodonList.append(i)
	i += 1
print(startCodonList)

fileOutput = open("startCodonIndices.txt", "w")
fileOutput.write("Total start codons: " + str(startCodonCount) + "\n")
for index in startCodonList:
	fileOutput.write(str(index) + "\n")
fileOutput.close()

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################

stopCodons = ["TAG", "TGA", "TAA"]
stopCodonCount = dna.count(stopCodons[0]+stopCodons[1]+stopCodons[2])
stopCodonList = []

i = 0
while i < len(dna)-2:
	codon = dna[i:i+3]
	if codon == stopCodons:
		stopCodonList.append(i)
	i += 1
print(stopCodonList)

fileOutput = open("stopCodonIndices.txt", "w")
fileOutput.write("Total stop codons: " + str(startCodonCount) + "\n")
for index in startCodonList:
	fileOutput.write(str(index) + "\n")
fileOutput.close()

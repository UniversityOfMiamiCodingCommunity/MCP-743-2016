# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################
# from os import listdir
# for x in listdir("/Users/SamuelDelOlio/GitHub/MCP-743/assignments/dataFiles"):
# 	print(x)


fileInput = open("/Users/SamuelDelOlio/GitHub/MCP-743/assignments/dataFiles/sequence-p53.fasta", "r")
dna = ""
for line in fileInput:
	dna += line[0:-1]
# print(dna)

# 2)
# Find all possible start codons in parsed DNA sequence.
fileOutput_1 = open("/Users/SamuelDelOlio/GitHub/MCP-743/assignments/startCodonIndices.txt", "w")

startCodon = "ATG"

startCodonCount = dna.count(startCodon)
fileOutput_1.write(str(startCodonCount) + "\n")	

i = 0
while i < len(dna)-2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		fileOutput_1.write("Start Codon Found at Index:" + " " + str(i) + "\n")
	i += 1


# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################


# 3)
# Find all possible stop codons in parsed DNA sequence.
fileOuput_2 = open("/Users/SamuelDelOlio/GitHub/MCP-743/assignments/stopCodonIndices.txt", "w")

stopCodons = ["TAG", "TGA", "TAA"]
for stopCodon in stopCodons:
	i = 0
	while i <len(dna)-2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			fileOuput_2.write("Found stopCodon" + str(iCodon) + "at index" + str(i) + "\n")
		i += 1

stopCodonCount = dna.count(stopCodon)
fileOuput_2.write(str(stopCodonCount) + "\n")
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################







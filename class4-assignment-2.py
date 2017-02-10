from os import sep

# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################

# Open a file to work in.
fileInput = open("dataFiles" + sep + "sequence-p53.fasta", "r")

dna = ""
for line in fileInput:
	dna += line[0:-1]
#~ print(dna)

# Alternative code using methods I don't understand:
#~ with open("dataFiles" + sep + "sequence-p53.fasta", "r") as p53Sequence:
	#~ dna = p53Sequence.read().replace("\n", "")
###########################################################################

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

# Count the total number of start codons in dna.
startCodon = "ATG"
startCodonCount = dna.count(startCodon)
#~ print("The total number of start codons in this sequence: " + str(startCodonCount))

# Create an empty list that will contain identified start codon indices.
startCodonList = []

# Use a while loop to identify all start codons and add their indices to the list using the append function.
# Note that this list will contain the index value as an integer.
i = 0	
while i  < len(dna)-2:
	Codon = dna[i:i + 3]
	if Codon == startCodon:
		startCodonList.append(i)			
	i += 1

#~ print(startCodonList)

# To write file named startCodonIndices.txt:
# Open a file to work in.
fileOutput = open("dataFiles" + sep + "startCodonIndices.txt", "w")

# Write first line to report the total number of start codons.
# This needs to be separate from the for loop below.
fileOutput.write("The total number of start codons in this sequence: " + str(startCodonCount) + "\n")

# This is a for loop to report the index of each identified start codon on a new line, and write it to the file. 
# We can only write a file in the format of a string, so the index integer must be converted into a string.
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

stopCodons = ["TAG", "TAA", "TGA"]

stopCodonList = []
stopCodonCount = 0

for stopCodon in stopCodons:
	i = 0
	while i < len(dna) - 2:
		Codon = dna[i:i+3]
		if Codon == stopCodon:
			stopCodonList.append(i)
			stopCodonCount += 1
		i +=1

#~ print(stopCodonList)
#~ print("The total number of stop codons in this sequence: " + str(stopCodonCount))

fileOutput = open("dataFiles" + sep + "stopCodonIndices.txt", "w")

fileOutput.write("The total number of stop codons in this sequence: " + str(stopCodonCount) + "\n")
for index in stopCodonList:
	fileOutput.write(str(index) + "\n")
fileOutput.close()

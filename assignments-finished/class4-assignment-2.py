# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################
# 1)
file = open('dataFiles/sequence-p53.fasta', 'r')
DNA = []
for line in file:
	DNA.append(line.strip('\n'))
DNA.pop(0)
DNASequence = "".join(DNA)
print(DNASequence)


# 2)
start_Codon = "ATG"
StartCodonFile = open("startCodonIndices.txt", 'w')
i = 0
c = 0
while i < len(DNASequence):
	i = DNASequence.find(start_Codon, i + 1)
	if i == -1: break
	c += 1
StartCodonFile.write('The total number of start codons is ' + str(c) + '.\n')


i = 0
c = 0
while i < len(DNASequence):
	i = DNASequence.find(start_Codon, i + 1)
	if i == -1: break
	c += 1
	StartCodonFile.write(str(i) + '.\n') 
	
StartCodonFile.close()

# 3)

StopCodons = ["TAG", "TGA", "TAA"]

AllStopCodons = []

StopCodonCount = 0
for StopCodon in StopCodons:
	i = 0
	while i < len(DNASequence) - 2:
		iCodon = DNASequence[i:i+3]
		if iCodon == StopCodon:
			AllStopCodons.append(i)	
			StopCodonCount += 1			
		i += 1

StopCodonFile = open("stopCodonIndices.txt", "w")

StopCodonFile.write("The total number of stop codons in this sequence: " + str(StopCodonCount) + "\n")

for codon in AllStopCodons:
	StopCodonFile.write(str(codon) + "\n")

StopCodonFile.close()




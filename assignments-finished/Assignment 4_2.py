
# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.

subsequenceofchromosome17= open('sequence-p53.fasta')
dna = ""
fileInput=subsequenceofchromosome17
for line in fileInput:
	dna += line[0:-1]
#####################################################################################################################

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
startcodon = "ATG"
file = open("startCodonIndices.txt", "w")
startcodontotal = 0
i = 0
startcodontotal=dna.count(startcodon)
file.write("Total number of start codons: "+str(startcodontotal)+"\n")
startcodonlisted = []
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == startcodon:
		file.write("startcodon, " +startcodon+ ", at index: "+str(i)+"\n")
	i += 1

#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
stopcodons = ["TAG", "TGA", "TAA"]
file = open("stopCodonIndices.txt", "w")
stopcodontotal = 0
i = 0
for stopcodon in stopcodons:
    stopcodontotal += dna.count(stopcodon)
file.write("Total number of stop codons: "+str(stopcodontotal)+"\n")
stopcodonlisted = []
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == stopcodon:
		file.write("stopcodon, " +stopcodon+ ", at index: "+str(i)+"\n")
	i += 1


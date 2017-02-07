# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################

fileInput = open("dataFiles/sequence-p53.fasta", "r")
dna=""
for line in fileInput:
	dna +=line[0:-1]
print dna

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

startCodon = "ATG"

startCodonCount = 0
i = 0
start_index=[]
fileOutput = open("startCodonIndices.txt", "w")

while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		start_index.append(i)
		# Increment the start codon count.
		#################################
		startCodonCount += 1 
	# Increment the index counter.
	##############################
	i += 1
fileOutput.write("There are a total of " + str(startCodonCount) + " start codons." + '\n')
for value in start_index:
	fileOutput.write(str(value) + '\n')

fileOutput.close()

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################

stopCodons = ["TAG", "TGA", "TAA"]

stopCodonCount = 0
stop_index=[]
fileOutput = open("stopCodonIndices.txt", "w")

for stopCodon in stopCodons: 
	i = 0
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopCodon:
			stop_index.append(i)
			# Increment the start codon count.
		    #################################
		    stopCodonCount += 1 
		# Increment the index counter.
		##############################
		i += 1
		
fileOutput.write("There are a total of " + str(stopCodonCount) + " stop codons." + '\n')
for value in stop_index:
	fileOutput.write(str(value) + '\n')

fileOutput.close()


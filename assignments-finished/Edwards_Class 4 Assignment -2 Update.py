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




#1
fileInput = open("dataFiles\sequence-p53.fasta", "r")
dna = ""
for line in fileInput:
	if line[0]== ">":
		continue
	dna += line[0:-1]
print(dna)
print(len(dna))


#2

startcodon = "ATG"

i = 0
startcodonCount = 0
for startCodon in startcodon:
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == startcodon:
			startcodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", str(startcodonCount))
StartCodonFile = open("JSE_startCodonIndices.txt", 'w')
StartCodonFile.write('The total number of start codons is ' + str(startcodonCount) + '.\n')

startcodon = "ATG"
i =0
startcodonCount = 0
for startCodon in startcodon:
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == startcodon:
			startcodonCount += 1
			print("Found start codon", iCodon, "at index", i) 
		i += 1
		StartCodonFile.write('Start ATG Codon at ' + str(i) + '.\n')
		
		
#3

stopcodon = ['TAG', 'TGA', 'TAA']

i = 0
stopcodonCount = 0
for stopCodon in stopcodon:
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopcodon:
			stopcodonCount += 1
		i += 1
print("The total number of stop codons found in the DNA sequence is:", str(stopcodonCount))
StopCodonFile = open("JSE_stopCodonIndices.txt", 'w')
StopCodonFile.write('The total number of stop codons is ' + str(stopcodonCount) + '.\n')


stopcodon = ['TAG', 'TGA', 'TAA']

i =0
stopcodonCount = 0
for stopCodon in stopcodon:
	while i < len(dna) - 2:
		iCodon = dna[i:i+3]
		if iCodon == stopcodon:
			startcodonCount += 1
			print("Found stop codon", iCodon, "at index", i) 
		i += 1
		StopCodonFile.write('Stop Codon at ' + str(i) + '.\n')
		
StopCodonFile.close()

#says there is zero. 

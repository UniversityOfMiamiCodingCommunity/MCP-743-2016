# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################
fasta = open('dataFiles/sequence-p53.fasta')

list_of_lines = []

for line in fasta:
	list_of_lines.append(line.rstrip('\n'))

list_of_lines = list_of_lines[1:-1]

sequence = ''

for line in list_of_lines:
	sequence += line

print(sequence)

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

startCodon = 'ATG'

file = open("startCodonIndices.txt", 'w')

index = 0
count = 0
while index < len(sequence):
	index = sequence.find(startCodon, index)
	if index == -1:
		break
	count += 1
	index += 1
file.write('The total number of start codons is ')
file.write(str(count))
file.write('.\n')

index = 0
while index < len(sequence):
	index = sequence.find(startCodon, index)
	if index == -1:
		break
	file.write('There was a start codon found at position ')
	file.write(str(index))
	file.write('.\n')
	index += 1

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 

stopCodons = ["TAG", "TGA", "TAA"]

file2 = open("stopCodonIndices.txt", 'w')

for stopCodon in stopCodons:
	index = 0
	count = 0
	while index < len(sequence):
		index = sequence.find(stopCodon, index)
		if index == -1:
			break
		count += 1
		index += 1
file2.write('The total number of stop codons is ')
file2.write(str(count))
file2.write('.\n')

index = 0
for stopCodon in stopCodons:
	while index < len(sequence):
		index = sequence.find(stopCodon, index)
		if index == -1:
			break
		file2.write('There was a ')
		file2.write(stopCodon)
		file2.write(' stop codon found at position ')
		file2.write(str(index))
		file2.write('.\n')
		index += 1




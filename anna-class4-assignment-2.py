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

index = 0
while index < len(weirdAssDna):
	index = weirdAssDna.find(startCodon, index)
	if index == -1:
		break
	print('There was a start codon found at position', index)
	index += 1


# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 


# string = []
# sequence = open('dataFiles/sequence-p53.fasta')
# for line in sequence:
# 	string.append(line.rstrip('\n'))
# string = string[1:-1]
# sequence = ', '.join(str(x) for x in string)
# print(sequence)
# sequence = ''
# for line in string:
# 	sequence += line
# print(sequence)

# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################




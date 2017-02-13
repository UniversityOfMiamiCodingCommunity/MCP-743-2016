# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################



#~ with open ('dataFiles/sequence-p53.fasta') as file_object:
	#~ contents = file_object.read()
	#~ print (contents)
	
filename= 'dataFiles/sequence-p53.fasta'
with open(filename) as file_object:
	lines = file_object.readlines()

dna_string= ' '
for line in lines:
	dna_string += line.rstrip()
print(dna_string)
	
	
#~ # 2)
#~ # Find all possible start codons in parsed DNA sequence.
#~ # Write your results to file named startCodonIndices.txt.
#~ # The file should be formatted such that:
#~ # a) the first line reports the total number of startCodons
#~ # b) the additional lines report a single start codon index

#~ startcodon= "ATG" 
#~ startcodonCount= dna_string.count(startcodon)
#~ print ("The total number of start codons is:" + str(startcodonCount))
#~ startCodonList = []
#~ i = 0	
#~ while i < len(dna_string)-2:
	#~ Codon = dna_string[i:i + 3]
	#~ if Codon == startcodon:
		#~ print("Index: ", i)
		#~ startCodonList.append(i)
	#~ i += 1
#~ fileOutput = open('dataFiles/startCodonIndices.txt', "w")
#~ fileOutput.write("The total number of start codons in this sequence: " + str(startcodonCount) + "\n")
#~ for index in startCodonList:
	#~ fileOutput.write(str(index) + "\n")
#~ fileOutput.close()
#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################
stopCodons = ["TAG", "TGA", "TAA"]

file2 = open("stopCodonIndices.txt", 'w')

for stopCodon in stopCodons:
	i = 0
	stopCodonCount = 0
	while i < len(dna_string):
		i = dna_string.find(stopCodon, i)
		if i == -1:
			break
		stopCodonCount += 1
		i += 1
file2.write('The total number of stop codons is ')
file2.write(str(stopCodonCount))
file2.write('.\n')

for stopCodon in stopCodons:
	i = 0
	while i < len(dna_string):
		i = dna_string.find(stopCodon, i)
		if i == -1:
			break
		file2.write('There was a ')
		file2.write(stopCodon)
		file2.write(' stop codon found at position ')
		file2.write(str(i))
		file2.write('.\n')
		i += 1




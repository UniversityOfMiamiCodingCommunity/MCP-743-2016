# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################

fileinput = open("sequence-p53.fasta", "r")

p53file = []

for line in fileinput:
	p53file.append(line.strip('\n'))

p53file.pop(0)

newDNA = "".join(p53file)
print(newDNA)

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

startCodon = 'ATG'
startCodonOutput = open('StartCodonIndices.txt', 'w')

listStartCodons = []
i = 0
while i < len(newDNA) - 2:
	iCodon = newDNA[i:i+3]
	if iCodon == startCodon:
		print("Found start codon", iCodon, "at index", i)
		listStartCodons.append(i)
	i += 1

startnumber = len(listStartCodons)
startCodonOutput.write("The number of start codons is: " + str(startnumber) + '\n')

for ele in listStartCodons:
	startCodonOutput.write(str(ele)+"\n")

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################

stopCodon = ["TGA", "TAG", "TAA"]
file2 = open('StopCodonIndices.txt', 'w')

listStopCodons = []
for stop in stopCodon:
	f = 0
	while f < len(newDNA) - 2:
		mCodon = newDNA[f:f+3]
		if mCodon == stop:
			print("Found stop codon", mCodon, "at index", f)
			listStopCodons.append(f)
		f += 1

value = len(listStopCodons)
file2.write("The number of stop codons is: " + str(value) + '\n')

print(listStopCodons)
for ele in listStopCodons:
	file2.write(str(ele)+"\n")

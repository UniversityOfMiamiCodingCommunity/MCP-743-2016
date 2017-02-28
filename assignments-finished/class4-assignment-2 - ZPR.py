# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################

fileinput = open("sequence-p53.fasta", "r")

genomedna = []

for line in fileinput:
	genomedna.append(line.strip('\n'))

genomedna.pop(0)

newDNA = "".join(genomedna)
print(newDNA)



# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

startCodon = "ATG" # Variable named startCodon defined as "ATG"
startCodonFile = open("startCodonIndices.txt", 'w') # Made a new file called startCodonIndices in a .txt file that I can 'w' in.
i = 0 
c = 0 
while i < len(newDNA): 
	i = newDNA.find(startCodon, i + 1) 
	if i == -1: break 
	c += 1
startCodonFile.write('The total number of start codons is: ' + str(c) + '.\n') 


i = 0 
c = 0 
while i < len(newDNA) + 2: 
	i = newDNA.find(startCodon, i + 1)  
	if i == -1: break 
	i += 1 
	c += 1 
	startCodonFile.write(str(i) + '.\n') 
	
startCodonFile.close() 





# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################

stopCodon = ["TAA", "TGA", "TAG"]

allStopcodons = []

stopCodonCount = 0
for stopCodon in stopCodon:
	i = 0
	while i < len(newDNA) -2:
		iCodon = newDNA[i:i+3]
		if iCodon == stopCodon:
			allStopcodons.append(i)
			stopCodonCount += 1
		i += 1
		
stopCodonfile = open("stopCodonIndices.txt", 'w')

stopCodonfile.write("The total number of stop codons is: " + str(stopCodonCount) + "\n")

for codon in allStopcodons:
	stopCodonfile.write(str(codon) + "\n")


stopCodonfile.close()

	
	


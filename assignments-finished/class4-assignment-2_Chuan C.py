# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################
fileInput = open("sequence-p53.fasta") 
sequence={}
for line in fileInput:
	if line.startswith(">"):
		name=line[1:].rstrip("\n")
		sequence[name]=""
	else:
		sequence[name] = sequence[name]+line.rstrip("\n")
dna=sequence[name]
print("The p53 DNA sequence is:",dna)
print("The length of p53 DNA sequence is:",len(dna))

# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]

startCodonCount = 0
i = 0
startCodonIndices = open("C:/Users/Samuel/Documents/GitHub/MCP-743/startCodonIndices.txt","w")
startCodonCount = dna.count(startCodon)
startCodonIndices.write("The total number of start codons found in the p53 DNA sequence is: "+str(startCodonCount)+"\n")
while i < len(dna) - 2:
	iCodon = dna[i:i+3]
	if iCodon == startCodon:
		startCodonIndices.write("Found start codon "+ iCodon+ " at index "+str(i)+"\n") 
	i += 1
startCodonIndices.close()

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################
stopCodonIndices = open("C:/Users/Samuel/Documents/GitHub/MCP-743/stopCodonIndices.txt","w")
stopCodonCount = 0
for stopCodon in stopCodons:
	stopCodonCount = stopCodonCount+dna.count(stopCodon)
stopCodonIndices.write("The total number of stop codons found in the p53 DNA sequence is: "+str(stopCodonCount)+"\n")
for stopCodon in stopCodons:
	j = 0
	while j < len(dna) - 2:
		jCodon = dna[j:j+3]
		if jCodon == stopCodon:
			stopCodonIndices.write("Found stop codon "+ jCodon+ " at index "+str(j)+"\n") 
		j += 1
stopCodonIndices.close()

################################
#Most input is from Sunil Yadav#
################################

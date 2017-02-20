# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################
startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]
data=open('C:/Users/Nil Su/Documents/GitHub/MCP-743/dataFiles/sequence-p53.fasta')
sequence={}
for line in data:
	if line.startswith(">"):
		name=line[1:].rstrip('\n')
		sequence[name]=''
	else:
		sequence[name]=sequence[name]+line.rstrip('\n') #Creates a Dictionary with key(header) and value(dna sequence)
dna=sequence[name]										#Extracts the value a.k.a the dna sequence 
print("The DNA sequence is:", dna)
print("The length of the DNA sequence is: ",len(dna))
######################################################################################################
# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
i=0
new_file = open("C:/Users/Nil Su/Documents/GitHub/MCP-743/dataFiles/startCodonIndices.txt", "w")				#Using Absolute Path 
startCodonCount=dna.count(startCodon)
new_file.write("The total number of start codons found in the DNA sequence is: "+str(startCodonCount)+"\n")
while i<len(dna)-2:
	icodon=dna[i:i+3]
	if icodon==startCodon:
		new_file.write("A start codon, " +startCodon+ ", was found at index: "+str(i)+"\n")
	i +=1

#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
new_file1 = open("C:/Users/Nil Su/Documents/GitHub/MCP-743/dataFiles/stopCodonIndices.txt", "w")
counter=0
for stopCodon in stopCodons:
	counter=counter+dna.count(stopCodon)
new_file1.write("The total number of possible stop codons found in the DNA sequence is: "+str(counter)+"\n")
for stopCodon in stopCodons:
	k=0
	while k<len(dna)-2:
		kcodon=dna[k:k+3]
		if kcodon==stopCodon:
			new_file1.write("A stop codon, " +stopCodon+ ", was found at index: "+str(k)+"\n")
		k +=1
#################################################################################################







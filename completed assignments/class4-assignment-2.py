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
###############################################################################################

#Open p53 file and create lines of dna as string
fileInput = open("/Users/Chris/Documents/Chris/python/MCP-743/dataFiles/sequence-p53.fasta", "r")
dna = ""
for line in fileInput:
    dna += line[0:-1]
#print(dna) will print total dna sequence as string if uncomented

#finds number of start codons in p53 gene
startCodon = "ATG"
startCodonCount = dna.count(startCodon)

#Stores number of start codons in file
fileOutput_1 = open("/Users/Chris/Documents/Chris/python/MCP-743/dataFiles/startCodonIndices.txt", "w")
fileOutput_1.write('Number of start codons in p53 gene: ' + str(startCodonCount))

#Stores text that reads what code is acheiving
fileOutput_1.write('\nThe p53 start codon indexes are: ' + '\n')

#Finds all start codon indexs
i = 0
while i < len(dna):
    i = dna.find(startCodon, i)
    if i == -1:
        break
    fileOutput_1.write(str(i) + '\n') #stores all start codon indexes in file
    i += 1
fileOutput_1.close() 

#3 Finds Number of Stop Codons 
#######################
stopCodons = ["TAG", "TGA", "TAA"]
fileOutput_2 = open("/Users/Chris/Documents/Chris/python/MCP-743/dataFiles/stopCodonIndices.txt", "w")
    stopCodonCount = dna.count('TAG') + dna.count('TGA') + dna.count('TAA')
    fileOutput_2.write('The total number of stop codons is ' + str(stopCodonCount) + '\n')
   
#Finds Stop Codon TAG 
index = 0
while index < len(dna):
    index = dna.find('TAG', index)
    if index == -1:
        break
    fileOutput_2.write('stop_index TAG found at ' + str(index) + '\n')
    index += 1

#3 Finds Stop Codon TGA
stopCodons = ["TAG", "TGA", "TAA"]
index = 0
while index < len(dna):
    index = dna.find('TGA', index)
    if index == -1:
        break
    fileOutput_2.write('stop_index TGA found at '+ str(index) + '\n')
    index += 1

#3 Finds Stop Codon TAA
stopCodons = ["TAG", "TGA", "TAA"]
index = 0
while index < len(dna):
    index = dna.find('TAA', index)
    if index == -1:
        break
    fileOutput_2.write('stop_index TAA found at ' + str(index) + '\n')
    index += 1

fileOutput_2.close()
fileInput.close()
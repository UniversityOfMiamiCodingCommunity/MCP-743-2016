# Personal Project_Identifying putative phosphorylation consensus

# This specific project will focus on identifying the putative Orb6 phosphorylation consensus in Sts5 protein sequence.

# 1) 
# Open the Sts5 protein sequence file in fasta format.
#########################################################
fileInput = open("Pombe-sts5.fa") 
sequence = {}
for line in fileInput:
	if line.startswith(">"):
		name = line[1:].rstrip("\n")
		sequence[name] = ""
	else:
		sequence[name] = sequence[name]+line.rstrip("\n")
Sts5Protein = sequence[name]
print("The Fission yeast S. Pombe Sts5 protein sequence is:",Sts5Protein)
print("The length of Sts5 protein sequence is:",len(Sts5Protein))
	
# 2) 
# Find all possible Orb6 phosphorylation consensus sequence in parsed Sts5 protein sequence.
# Write results to file named Orb6Consensus.txt.
# The file should be formatted such that:
# a) the first line reports the total number of the putative Orb6 phosphorylation consensus. 
# b) the additional lines report a single Orb6 phosphorylation site index
############################################################################################
## Load a module using the import statement: module dealing with regular expression (re)
#import re
## Define the pattern I would like to search for
pattern = "H.[RKH]..[ST]"
## Use the regular search function
#re.search (pattern, Sts5Protein)
#St5Protein = sequence[name]
#if re.search(r"H.[RKH]..[ST]", Sts5Protein):
	#print("The Orb6 phosphorylation consensus in Sts5 protein is found")

patternCount = 0
i = 0
Orb6Consensus = open("C:/Users/Samuel/Documents/GitHub/MCP-743/assignments-finished/Personal Project_Fission yeast Sts5 protein/Orb6Consensus.txt", "w")
patternCount = Sts5Protein.count(pattern)
Orb6Consensus.write("The total number of Orb6 phosphorylation consensus found in the Sts5 protein sequence is: "+str(patternCount)+"\n")
while i < len(Sts5Protein) - 5:
	iPattern = Sts5Protein[i:i+6]
	if iPattern == pattern:
		Orb6Consensus.write("Found Orb6 consensus "+ iPattern+ " at index "+str(i+6)+"\n") 
	i += 1
Orb6Consensus.close()




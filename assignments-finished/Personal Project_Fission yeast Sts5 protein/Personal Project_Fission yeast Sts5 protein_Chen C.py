# Personal Project_Identifying putative phosphorylation consensus

# This specific project will focus on identifying the putative Orb6 phosphorylation consensus in Sts5 protein sequence.

# 1) Open the Sts5 protein sequence file in fasta format.
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
	
# 2) Find all possible Orb6 phosphorylation consensus sequence in parsed Sts5 protein sequence.
###############################################################################################
# Load a module using the import statement: module dealing with regular expression (re)
import re
# Define the pattern I would like to search for
pattern = "H.[RKH]..[ST]"
# testpattern = "HGHRRS"
Orb6Consensus = re.findall (pattern, Sts5Protein)
print(Orb6Consensus)





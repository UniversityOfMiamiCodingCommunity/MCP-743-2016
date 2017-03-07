fileInput = open("/Users/ugnzekon/GitHub/MCP-743/FinalProjectStuff/GRIN2A-aligned.fasta.txt", "r")
import re

######Program that extracts species name from fasta alignment file, 
######then calculates percentage similarity between the set of protein sequences


seq_info = []
aligned_sequences = []
species_name_list = []
for line in fileInput:
	species_name = []
	if line[0:3] == ">sp" or line[0:3] == ">tr":   	   #####lines starting with "">sp" and ">tr" have sequence info
		#print(line)
		sLine = line.split('OS=')
		#print(sLine)
		sLine2 = sLine[1].split(' GN=')                #### LINES NOT SPLIT ON TABS, not all OS values followed by GN= (PE=)
		species_name = sLine2[0]
		#print(sLine2)
		if " PE=" in sLine2[0]:
			sLine3 = sLine2[0].split(' PE=')
			species_name = sLine3[0]
		species_name_list.append(species_name)
		#print(species_name)
		seq_info.append(line)
	 	#print(seq_info)

	else:								     ##### all other lines will be sequences
		aligned_sequences.append(line)
		#print(aligned_sequences)

	# for aligned_sequence in aligned_sequences:
	# 	print(aligned_sequence)
	# 	print(len(line))      			     ###############each seq length is 4103

percentage = []
j = 0 
for sequence in aligned_sequences:
	i = 0
	for amino_acid in sequence:
		if amino_acid == '-':
			pass
			#b += 1
			#percent_dif = 100*(b/len(sequence))
			#print("Sequence differs by: " + str(percent_dif) + "%")
		else:
			i += 1
	percent_sim = 100*(i/len(sequence))
	percentage.append(percent_sim)
	#print(j, len(seq_info), len(aligned_sequences))
	print("Number of amino acids similar: ", i, "\n", 
		"Percent sequence similarity: ", percent_sim, "%", "\n", 
		seq_info[j])
			#print("Sequence similarity: " + str(percent_sim) + "%")
	j += 1
		


##make a dictionary that lists species, sequence match (key=species, val=seq%similarity)
##tupule??

combined = [(species_name_list[i], percentage[i]) for i in range(len(species_name_list))]

#print(combined) ###lists species name, percent similarity
			

fileInput.close()
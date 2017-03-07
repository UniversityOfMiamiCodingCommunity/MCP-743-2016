
fileInput = open("/Users/ugnzekon/GitHub/MCP-743/GRIN2A-aligned.fasta.txt", "r")
import re


for line in fileInput:
	seq_info = []
	aligned_sequences = []
	species_name = []
	if line[0:3] == ">sp":   			#####lines starting with "">sp" have sequence info
		seq_info.append(line)
		print(seq_info)


		os = re.search(' OS=(.+?) (.+?) ', line)  #### LINES NOT SPLIT ON TABS, not all OS values followed by GN= (PE=)
		if os:
			species_name.append(os)
		print(species_name)


	else:								##### all other lines will be sequences
		aligned_sequences.append(line)
		#print(aligned_sequences)

	# for aligned_sequence in aligned_sequences:
	# 	print(aligned_sequence)
	# 	print(len(line))      			###############each seq length is 4103


i = 0
j=0    #counts identity hits
for sequence in aligned_sequences:
	for amino_acid in sequence:
		if amino_acid == '-':
			j += 1
			#percent_dif = 100*(j/len(sequence))
			#print("Sequence differs by: " + str(percent_dif) + "%")
		else:
			i += 1
			percent_sim = 100*(i/len(sequence))
			print("Sequence similarity: " + str(percent_sim) + "%")
	j = 0
	i =0
		


##make a dictionary that lists species, sequence match (key=OS, val=seq)

fileInput.close()
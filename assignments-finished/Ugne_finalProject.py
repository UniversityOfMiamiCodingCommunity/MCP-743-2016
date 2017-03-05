
fileInput = open("/Users/ugnzekon/GitHub/MCP-743/GRIN2A-aligned.fasta.txt", "r")
import re


for line in fileInput:
	seq_info = []
	aligned_sequences = []
	species_name = []
	if line[0:3] == ">sp":   			#####lines starting with "">sp" have sequence info
		seq_info.append(line)
		print(seq_info)

		# os = re.search('OS=(.+?)', line)  #### LINES NOT SPLIT ON TABS, not all OS values followed by GN=
		# if os:
		# 	species_name.append(os)
		# print(species_name)
	else:								##### all other lines will be sequences
		aligned_sequences.append(line)
		#print(aligned_sequences)

# for sequence in aligned_sequences:
# 	if line[0] ==:
# 		#i+1



fileInput.close()
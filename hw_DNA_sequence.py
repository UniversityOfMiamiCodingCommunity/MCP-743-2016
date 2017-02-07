start_codon = "ATG"
stop_codons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"

# 1) Identify the index of each start codon in the DNA sequence provided  

#startCodonSearchResult = dna.find(start_codon)
#for start in start_codon:
#	if start in dna:
#		print("Found start codon:", start_codon , "at position", dna.find(start_codon))
#print("\n")	

#for start in start_codon:
#	if start in dna:
#		print("Found start codon:", start_codon, "at position", dna.find(start))
#print("\n")	
#####why are positions wrong? not finding them all?

#start_codon_count = 0
#for start in start_codon:
#	i = 0
#	while i < len(dna) -2:
#		iCodon = dna[i:i+3]
#		if iCodon == start_codon:
#			print("Found start codon", iCodon, "at index", i)
#			start_codon_count += 1
#		i += 1
#print("The total number of start codons found in the DNA sequence is:", start_codon_count)
#print("\n")
#why is it repeating?

start_codon_count = 0
while start_codon_count < len(dna):
    start_codon_count = dna.find('ATG', start_codon_count)
    if start_codon_count == -1:
        break
    print('Start codon found at ', start_codon_count)
    start_codon_count += 2
print("\n")

# 2) Get the index of the first start codon.
print("Index of the first start codon is:" , dna.find(start_codon))
print("\n")	

# 3) Identify the index of each stop codon.

#for stop_codon in stop_codons:
#	stopCodonSearchResult = dna.find(stop_codon)
#	print("Found stop codon:", stop_codon, " at position ", dna.find(stop_codon))
#print("\n")	
############why is it not finding everything?

stop_codon_count = 0
for stop_codon in stop_codons:
	i = 0
	while i < len(dna) -2:
		iCodon = dna[i:i+3]
		if iCodon == stop_codon:
			print("Found stop codon", iCodon, "at index", i)
			stop_codon_count += 1
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stop_codon_count)
print("\n")


# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# start_dna_orf = dna[20:]
# start_dna = dna.find('ATG')
# #print(ORF_dna)
# ORF_codon_count = 0
# ORF_dna = dna[start_dna:]
# codons = [ORF_dna[i:i+3] for i in range(0, len(ORF_dna),3)]
# print(codons)
# for stop_codon in stop_codons:
# 	i = 0
# 	while i < len(start_dna_orf) -2:
# 		orfCodon = start_dna_orf[i:i+3]
# 		if orfCodon == stop_codon:
# 			print("Found stop codon", orfCodon, "at index", i)
# 			ORF_codon_count += 1
# 		i += 1

minStopCodon, minStopCodonIndex = "", 10000000
for stop_codon in stop_codons:
	i = 0
	while i < len(dna) -2:
		iCodon = dna[i:i+3]
		if iCodon == stop_codon:
			StopCodonIndex = i
			if ((StopCodonIndex + 3) - 20) % 3 == 0:
				minStopCodon = iCodon
				minStopCodonIndex = StopCodonIndex
				print("Codon", codon, "found at index", i)
				break
			i += 1
print("The first in frame stop codon is", minStopCodon, "at index", minStopCodonIndex)

print("\n")

# 5) Count the number of G bases. 
base_a = "A"
base_t = "T"
base_c = "C"
base_g = "G"

G_count = 0
for base in base_g:
	i=0
	while i < len(dna) -2:
		iBase = dna[i:i+1]
		if iBase == base_g:
			#print("Found G at index" , i)
			G_count += 1
		i += 1
print("The total number of G's in this DNA seqence is:", G_count)
print("\n")

# 6) Identify each index that corresponds to an A base.  


A_count = 0
for base in base_a:
	i=0
	while i < len(dna) -2:
		iBase = dna[i:i+1]
		if iBase == base_a:
			print("Found A at index" , i)
			A_count += 1
		i += 1
#print("The total number of A's in this DNA seqence is:", A_count)
print("\n")

# 7) Identify the length of the DNA sequence.
print("The toal length of this DNA sequence is", len(dna), "bases.")
print("\n")
# 8) Split the DNA sequence into a list using the start codon
#dna_codons = ORF_dna.split([i:i+3])
#print(dna_codons)

start = dna.find(start_codon)

#take seq from first start codon
trimmed_sequence = dna[start:]

#split into triplets
codons = [trimmed_sequence[i:i+3] for i in range(0, len(trimmed_sequence),3)]
#print(len(codons))
#print(trimmed_sequence)
print(codons)


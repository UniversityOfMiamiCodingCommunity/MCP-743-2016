{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
# Assignment
# 1) Identify the index of each start codon in the DNA sequence provided below. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon.
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# 5) Count the number of G bases. 
# 6) Identify each index that corresponds to an A base.  
# 7) Identify the length of the DNA sequence. 
# 8) Split the DNA sequence into a list using the start codon. 
# Note: all of the answers to this assignment are directly or indirectly provided in the code above.
#########################################################################################################################


#1 Finds all Start Codons
#########################
print('Answer 1:')
startCodon = "ATG"
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
index = 0
while index < len(dna):
    index = dna.find(startCodon, index)
    if index == -1: #Two equal signs means you are doing a comparison 
        break
    print('start_index ATG found at ', index)
    index += 1


#2 Finds first start Codon
##########################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
startCodon = 'ATG'
print('\nAnswer 2: First start codon found at ', dna.find(startCodon))


#3 Finds Stop Codon TAG
#######################
print('\nAnswer 3:')
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
index = 0
while index < len(dna):
    index = dna.find('TAG', index)
    if index == -1:
        break
    print('stop_index TAG found at ', index)
    index += 1
#3 Finds Stop Codon TGA
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
index = 0
while index < len(dna):
    index = dna.find('TGA', index)
    if index == -1:
        break
    print('stop_index TGA found at ', index)
    index += 1
#3 Finds Stop Codon TAA
stopCodons = ["TAG", "TGA", "TAA"]
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
index = 0
while index < len(dna):
    index = dna.find('TAA', index)
    if index == -1:
        break
    print('stop_index TAA found at ', index)
    index += 1


#4 Finds Stop Codons in ORF after first start codon
###################################################
#parameters
print('\nAnswer 4: ')
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
startCodon = 'ATG'
stopCodons = ["TAG", "TGA", "TAA"]
ORF = []
stopCodon_ORF = []
startCodon_slice = []

#split dna into starting at first startcodon and ending at the end of the sequence
startCodon_slice = ['{}{}'.format(startCodon, s) for s in dna.split(startCodon) if s]
ORF = startCodon_slice[1:-1]
ORF_Full =''.join(ORF)
print('Open Reading Frame is ', ORF_Full)

#Finding the stop codons within the ORF
for stopCodon in stopCodons:
    i = 0
    while i < len(ORF_Full):
        iCodon = ORF_Full[i:i+3]
        if iCodon == stopCodon and (i+3) % 3 == 0:
            print('Found stop codon ' , iCodon, 'in ORF at ', i)
            break
        i += 1


    
#5 Counts Number of G in Sequence
#################################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
print('\nAnswer 5: Number of G in sequence is ', dna.count('G'))


#6 Finds all A bases
####################
print('\nAnswer 6: ')
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
index = 0
while index < len(dna):
    index = dna.find('A', index)
    if index == -1:
        break
    print ('A_Index found at ', index)
    index += 1


#7 Length of DNA Sequence
#########################
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
print('\nAnswer 7: Length of DNA is ', len(dna))


#8 Split DNA at Start Codons
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
startCodon = "ATG"
print('\nAnswer 8: DNA split at start codons ', dna.split(startCodon))


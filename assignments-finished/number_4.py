{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
dna = "GGACGTTTAAAAGGGAAAAAATGGAACCACCCGGGATAATGAAATTTTATGGGCCCCACCAGGACTAAGATAGCGTGAATGTAAATAAATAGCCC"
startCodon = 'ATG'
stopCodons = ["TAG", "TGA", "TAA"]

ORF = []
stopCodon_ORF = []
startCodon_slice = []

startCodon_slice = ['{}{}'.format(startCodon, s) for s in dna.split(startCodon) if s]
ORF = startCodon_slice[1:-1]
ORF_Full =''.join(ORF)
print(ORF_Full)
for stopCodon in stopCodons:
    i = 0
    while i < len(ORF_Full):
        iCodon = ORF_Full[i:i+3]
        if iCodon == stopCodon:
            print('Found stop codon ' , iCodon, 'in ORF at ', i)
            break
        i += 1


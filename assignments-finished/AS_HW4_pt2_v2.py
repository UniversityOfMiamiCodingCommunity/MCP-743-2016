# 1)
file = open('dataFiles/sequence-p53.fasta', 'r')
dna = []
for line in file:
	dna.append(line.strip('\n'))
dna.pop(0)
dnaseq = "".join(dna)
print(dnaseq)
  
  
# 2)
startcodon = "ATG"
startcodondoc = open("startcodon_hw4_pt2.txt", 'w')
i = 0
c = 0
while i < len(dnaseq) + 2:
	i = dnaseq.find(startcodon, i + 1)
	if i == -1: break
	i += 1
	c += 1
startcodondoc.write('# of start codons = ' + str(c) + '.\n')


i = 0
c = 0
while i < len(dnaseq) + 2:
	i = dnaseq.find(startcodon, i + 1)
	if i == -1: break
	i += 1
	c += 1
	startcodondoc.write(str(i) + '.\n') 
	
startcodondoc.close()

# 3)

stopcodons = ["TAG", "TGA", "TAA"]

stopcodonlst = []

stopcodon_ind = 0
for stopcodon in stopcodons:
	i = 0
	while i < len(dnaseq) - 2:
		codon_ind = dnaseq[i:i+3]
		if codon_ind == stopcodon:
			stopcodonlst.append(i)	
			stopcodon_ind += 1			
		i += 1

stopcodondoc = open("stopcodon_hw4_pt2.txt", "w")

stopcodondoc.write("# stop codons = " + str(stopcodon_ind) + "\n")

for codon in stopcodonlst:
	stopcodondoc.write(str(codon) + "\n")

stopcodondoc.close()
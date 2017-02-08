 # 1
dat = open('dataFiles/sequence-p53.fasta', 'r')
dna = []
for line in dat:
	dna.append(line.strip('\n'))
	dna.pop(0)
	dnaseq = "".join(dna)
	print(dnaseq)
 
 
 # 2)
startcodon = "ATG"
startcodondoc = open("startcodoni.txt", 'w')
i = 0
c = 0
while i < len(dnaseq) + 2:
	i = dnaseq.find(startcodon, i + 1)
	if i == -1: break
	i += 1
	c += 1
startcodondoc.write('The total number of start codons is ' + str(c) + '.\n')


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

lst_stopcodons = []

stopcodoncount = 0
for stopcodon in stopcodons:
	i = 0
	while i < len(dnaseq) - 2:
		iCodon = dnaseq[i:i+3]
		if iCodon == stopcodon:
			lst_stopcodons.append(i)	
			stopcodoncount += 1			
		i += 1

stopcodondoc = open("stopcodoni.txt", "w")

stopcodondoc.write("The total number of stop codons in this sequence: " + str(stopcodoncount) + "\n")

for codon in lst_stopcodons:
	stopcodondoc.write(str(codon) + "\n")
 
stopcodondoc.close()
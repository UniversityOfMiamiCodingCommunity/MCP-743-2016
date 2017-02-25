#S75619.1 precore region: precore, core [hepatitis B virus HBV, host=human, patient 1 isolate, Genomic, 90 nt]
#~ >AB981583.1 HBV genotype B DNA, complete genome, isolate: P2-121214
#~ #S81946.1 Hepatitis B virus envelope (env) gene, complete cds



#Find HBV core and envelop sequences in genome sequence
#Find Start and Stop Codons
#Total Lengths
#HBV Hepatocyte cell lines (class)
#Function?




fileInput = open("..\dataFiles\HBV.fasta", "r")
HBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	HBV += line[0:-1]
print(HBV)
print(len(HBV))
#3,215bp :)




startCodons = ["ATG"]
StartCodonFile = open("HBV_startCodonIndices.txt", 'w')
startcodonCount = 0
for startCodon in startCodons:
	i =0
	while i < len(HBV) - 2:
		iCodon = HBV[i:i+3]
		if iCodon == startCodon:
			startcodonCount += 1
			StartCodonFile.write('Start ATG Codon at ' + str(i) + '.\n')
		i += 1
print("The total number of start codons found in the DNA sequence is:", str(startcodonCount))
StartCodonFile.write('The total number of start codons is ' + str(startcodonCount) + '.\n')

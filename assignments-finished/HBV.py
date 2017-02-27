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
			print("Found start codon", iCodon, "at index", i)
		i += 1
print("The total number of start codons found in the DNA sequence is:", str(startcodonCount))
StartCodonFile.write('The total number of start codons is ' + str(startcodonCount) + '.\n')

StartCodonFile.close()



stopCodons = ['TAG', 'TGA', 'TAA']
StopCodonFile = open("HBV_stopCodonIndices.txt", 'w')
stopcodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(HBV) - 2:
		iCodon = HBV[i:i+3]
		if iCodon == stopCodon:
			stopcodonCount += 1
			print("Found stop codon", iCodon, "at index", i)
			StopCodonFile.write("Stop Codon at index " + str(i) + '.\n')
		i += 1
print("The total number of stop codons found in the DNA sequence is:", str(stopcodonCount))
StopCodonFile.write('The total number of stop codons is ' + str(stopcodonCount) + '.\n')

#In Frame

startCodon = "ATG"
stopCodons = ["TAG", "TGA", "TAA"]

#Found index of 1st start codon

startCodonIndex = HBV.find(startCodon)
print(startCodonIndex)

#Find indencies of all stop codons

i = startCodonIndex
firststopCodonIndex = 0
firststopCodon = ""
InFrameFile = open("HBV_InframeIndices.txt", 'w')
while i < len(HBV) - 2:
	iCodon = HBV[i:i+3]
	if iCodon in stopCodons:
		print(iCodon, i)
		firststopCodon = iCodon
		firststopCodonIndex = i
		break
	i += 1
print("The stop codon in frame with start codon is", firststopCodon, "at index", firststopCodonIndex)
InFrameFile.write("The stop codon in frame with start codon is "  + str(firststopCodon) + '.\n')
InFrameFile.write("at index " + str(firststopCodonIndex) + '.\n')

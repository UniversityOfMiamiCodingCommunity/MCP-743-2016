fileInput = open("..\dataFiles\sequence-eHBV.fasta", "r")
eHBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	eHBV += line[0:-1]
print(eHBV)
print(len(eHBV))

startCodons = ["ATG"]
StartCodonFile = open("eHBV_startCodonIndices.txt", 'w')
startcodonCount = 0
for startCodon in startCodons:
	i =0
	while i < len(eHBV) - 2:
		iCodon = eHBV[i:i+3]
		if iCodon == startCodon:
			startcodonCount += 1
			StartCodonFile.write('Start ATG Codon at ' + str(i) + '.\n')
			print("Found start codon", iCodon, "at index", i)
		i += 1
print("The total number of start codons found in the DNA sequence is:", str(startcodonCount))
StartCodonFile.write('The total number of start codons is ' + str(startcodonCount) + '.\n')

StartCodonFile.close()



stopCodons = ['TAG', 'TGA', 'TAA']
StopCodonFile = open("eHBV_stopCodonIndices.txt", 'w')
stopcodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(eHBV) - 2:
		iCodon = eHBV[i:i+3]
		if iCodon == stopCodon:
			stopcodonCount += 1
			print("Found stop codon", iCodon, "at index", i)
			StopCodonFile.write("Stop Codon at index " + str(i) + '.\n')
		i += 1
print("The total number of stop codons found in the DNA sequence is:", str(stopcodonCount))
StopCodonFile.write('The total number of stop codons is ' + str(stopcodonCount) + '.\n')

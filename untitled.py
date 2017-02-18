all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index


startcodon = "ATG"
StartCodonFile = open("JSEstartCodonIndices.txt", 'w')
i = 0
startcodonCount = 0
while i < len(p53) - 2:
	p53[i:i+3] == startcodon
	if i == -1: break
	print("Found start codon", p53[i:i+3], "at index", i)
	startcodonCount += 1
	i += 1
StartCodonFile.write('The total number of start codons is ' + str(startcodonCount) + '.\n')

i = 0
startcodonCount = 0
while i < len(p53) - 2:
	p53[i:i+3] == startcodon
	if i == -1: break
	print("Found start codon", p53[i:i+3], "at index", i)
	i += 1
	startcodonCount += 1
StartCodonFile.write('Start codon at ' + str(i) + '.\n') 
	
StartCodonFile.close()






# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
    


stop1codon = "TAG" 
StopCodon1File = open("JSEstopCodon1Indices.txt", 'w')

stopcodon1Count = 0
i = 0
while i < len(p53) - 2:
		iCodon = p53[i:i+3]
		if iCodon == stop1codon:
			print ("Found stop codon", iCodon, "at index", i)
		stopcodon1Count += 1
		i += 1
print ("The total number of stop codons found in the DNA sequence is", stopcodon1Count)
StopCodon1File.write('The total number of stop codons is ' + str(stopcodon1Count) + '.\n')


stopcodon1Count = 0
i = 0
while i < len(p53) - 2:
		iCodon = p53[i:i+3]
		if iCodon == stop1codon:
			print ("Found stop codon", iCodon, "at index", i)
		stopcodon1Count += 1
		i += 1
StopCodon1File.write('Stop codon at ' + str(i) + '.\n') 

StopCodon1File.close()



stop2codon = "TAA"
  


stopcodonCount = 0
i = 0
while i < len(p53) - 2:
		iCodon = p53[i:i+3]
		if iCodon == stop2codon:
			print ("Found stop codon", iCodon, "at index", i)
		stopcodonCount += 1
		i += 1
print ("The total number of stop codons found in the DNA sequence is", stopcodonCount)








stop3codon = "TGA"
stopcodonCount = 0
i = 0
while i < len(p53) - 2:
		iCodon = p53[i:i+3]
		if iCodon == stop3codon:
			print ("Found stop codon", iCodon, "at index", i)
		stopcodonCount += 1
		i += 1
print ("The total number of stop codons found in the DNA sequence is", stopcodonCount)

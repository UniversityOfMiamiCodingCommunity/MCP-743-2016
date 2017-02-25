#Evelope HBV in HBV Genome

fileInput = open("..\dataFiles\HBV.fasta", "r")
HBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	HBV += line[0:-1]
print(HBV)
print(len(HBV))



eHBV = "ATGGGAGGTTGGTCTTCCAAACC"
print(eHBV)
print(len(eHBV))

i = 0
for Seq in eHBV:
	while i < len(HBV)- 22:
		Core = HBV[i:i+23]
		if Core == eHBV:
			print("Found Envelope Sequence", Core, "in HBV Genome at index", i)
			EnvelopeFile = open("HBV_EnvelopeIndices.txt", 'w')
			EnvelopeFile.write('Found Envelope Sequence at index ' + str(i) + '.\n')
		i +=1

fileInput = open("..\dataFiles\sequence-eHBV.fasta", "r")
eHBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	eHBV += line[0:-1]
print(eHBV)
print(len(eHBV))

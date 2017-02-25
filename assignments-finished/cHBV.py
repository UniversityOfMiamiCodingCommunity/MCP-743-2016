fileInput = open("..\dataFiles\sequence-cHBV.fasta", "r")
cHBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	cHBV += line[0:-1]
print(cHBV)
print(len(cHBV))
#90bp :)

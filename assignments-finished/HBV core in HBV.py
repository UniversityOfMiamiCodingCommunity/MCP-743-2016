#Find HBV Core in HBV Genome

fileInput = open("..\dataFiles\HBV.fasta", "r")
HBV = ""
for line in fileInput:
	if line[0]== ">":
		continue
	HBV += line[0:-1]
print(HBV)
print(len(HBV))

#~ fileInput = open("..\dataFiles\sequence-cHBV.fasta", "r")
#~ cHBV = ""
#~ for line in fileInput:
	#~ if line[0]== ">":
		#~ continue
	#~ cHBV += line[0:-1]
#~ print(cHBV)
#~ print(len(cHBV))

cHBV = "ATGCAAC"
print(cHBV)

i = 0
for Seq in cHBV:
	while i < len(HBV)- 6:
		Core = HBV[i:i+7]
		if Core == cHBV:
			print("Found Core Sequence", Core, "in HBV Genome at index", i)
			CoreFile = open("HBV_CoreIndices.txt", 'w')
			CoreFile.write('Found Core Sequence at index ' + str(i) + '.\n')
		i +=1



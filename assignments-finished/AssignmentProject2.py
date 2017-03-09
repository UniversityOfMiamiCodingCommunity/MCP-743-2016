########################################################################
#	Opening the first file

from os import listdir

## Test the exact contents of the directory
#~ for x in listdir("."):
	#~ print(x)

fileInput = open("Final3.txt", "r")

## Check the file output
#~ contents = fileInput.read()
#~ print(contents)

########################################################################
#	Creating a class for the tropism assay

## Each assay can populate one instance of this class, and each document has data recorded from one assay
## Want to include date, viral batch id, monocyte donor id, envelope donor id, raw de novo values, and raw RNA sep values

class TropismAssay():
	def __init__(self, date, vBatch, mDonor, rawData):
		self.date = date
		self.vBatch = vBatch
		self.mDonor = mDonor
		self.rawData = rawData

########################################################################
#	Extracting data from the file

## (Note: number of samples varies but docs are always formatted with same four-line intro and five controls at the end)
## Want each line to be added to the list "lines"
## Want the chunks of data in each line to be considered as items in a list for easier access 

lines = []
i = 0
for line in fileInput:
	lines.append(line.split())   
	i += 1
#~ print(lines)

## Want to extract date, viral batch, and donor number from the document

for chunk in lines[1:2]:
	date_1 = chunk[3]
	virBatch = chunk[7]
	monDonor = chunk[2]
#~ print(date_1, virBatch, monDonor)

## Want to create a formatted list of envelope donors 

envDonors = []
for chunk in lines[4:]:
	chunk = str(chunk[0] + "-" + chunk [1])
	envDonors.append(chunk)
#~ print(envDonors)

## Want to create list of de novo data values

deNovo = []
for chunk in lines[4:]:
	deNovo.append(chunk[2])
#~ print(deNovo)

## Want to create list of RNASep data values

rnaSep = []
for chunk in lines[4:]:
	rnaSep.append(chunk[5])
#~ print(rnaSep)

########################################################################
#	Organizing extracted data uing class

## Want to create dictionary for data set

rawDataChunks = []
j = 0
for chunk in envDonors:
	chunk1 = envDonors[j]
	chunk2 = deNovo[j]
	chunk3 = rnaSep[j]
	newEntry = {'Envelope':chunk1,'De Novo Value':chunk2,'RNA Sep':chunk3}
	rawDataChunks.append(newEntry)
	j += 1
#~ print(rawDataChunks)

assay_1 = TropismAssay(date_1, virBatch, monDonor, rawDataChunks)
print("Date: " + assay_1.date + "		Viral Batch #: " + assay_1.vBatch + "		Monocyte Donor ID: " + assay_1.mDonor + "		Samples Tested: " + str(len(rawDataChunks))) 
print("\nEnvelope:				De Novo Value:			   RNA Sep: \n" )
for entry in assay_1.rawData: 
	print(entry['Envelope'] + "				" + entry['De Novo Value'] + "					" + entry['RNA Sep'])

########################################################################
#	Testing the code on a second file

### !!! I don't know if what I've done above is good enough. I parsed the first document to my satisfaction but some envelopes in this second one are named differently, so the same code doesn't work again. Given infinite time I would want to make this code more extrapolateable

fileInput2 = open("Final4.txt", "r")

lines2 = []

i = 0
for line in fileInput2:
	lines2.append(line.split())   
	i += 1
	
for chunk in lines2[1:2]:
	date_2 = chunk[3]
	virBatch2 = chunk[7]
	monDonor2 = chunk[2]

envDonors = []
for chunk in lines2[4:]:
	chunk = str(chunk[0] + "-" + chunk [1])
	envDonors.append(chunk)
	
deNovo = []
for chunk in lines2[4:]:
	deNovo.append(chunk[2])

rnaSep = []
for chunk in lines2[4:]:
	rnaSep.append(chunk[5])
	
rawDataChunks = []
j = 0
for chunk in envDonors:
	chunk1 = envDonors[j]
	chunk2 = deNovo[j]
	chunk3 = rnaSep[j]
	newEntry = {'Envelope':chunk1,'De Novo Value':chunk2,'RNA Sep':chunk3}
	rawDataChunks.append(newEntry)
	j += 1

assay_2 = TropismAssay(date_2, virBatch2, monDonor2, rawDataChunks)
#~ print("Date: " + assay_2.date + "		Viral Batch #: " + assay_2.vBatch + "		Monocyte Donor ID: " + assay_2.mDonor + "		Samples Tested: " + str(len(rawDataChunks))) 
#~ print("\nEnvelope:				De Novo Value:			   RNA Sep: \n" )
#~ for entry in assay_2.rawData: 
	#~ print(entry['Envelope'] + "				" + entry['De Novo Value'] + "					" + entry['RNA Sep'])

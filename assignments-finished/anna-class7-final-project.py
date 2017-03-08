# create a dictionary of cell lines and diagnostic status
fileDiagnosis = open("diagnosis.txt", "r")
diagnosisDictionary = {}

for line in fileDiagnosis:
	if line[0:2] == "N_":
		lineAsList = line.split()
		PDXLine = lineAsList[0]
		diagnosis = lineAsList[1]
		uniqueKey = (PDXLine, diagnosis)
		diagnosisDictionary.update({uniqueKey})
fileDiagnosis.close()

# create lists of newly/recurrent lines
fileDiagnosis = open("diagnosis.txt", "r")
Newly = []
Recurrent = []

for line in fileDiagnosis:
	if line[0:2] == "N_":
		lineAsList = line.split()
		PDXLine = lineAsList[0]
		diagnosis = lineAsList[1]
		if diagnosis == "Newly":
			Newly.append(PDXLine)
		elif diagnosis == "Recurrent":
			Recurrent.append(PDXLine)
		else: break
fileDiagnosis.close()

# write file for newly diagnosed lines
fileMicroarray = open("microarray.txt", "r")

firstLine = fileMicroarray.readline().split()
print(firstLine)
for cellLine in firstLine:
	if cellLine[0:2] == "N_":
		fileName = (cellLine + ".txt")
		file = open(fileName, "w")
		for line in fileMicroarray:
			i = firstLine.index(cellLine)
			file.write(line.split()[0] + "\t")
			file.write(line.split()[i] + "\n")
		file.close()


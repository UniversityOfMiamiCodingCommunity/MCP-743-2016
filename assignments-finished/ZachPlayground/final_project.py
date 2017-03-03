file = open("9kb.over.reads.fasta", "r")
fileoutput = open('modified_project.txt', 'w')
startCodon = "ATG"
stopCodons = ["TGA", "TAG", "TAA"]
import os
#################################################
#################################################
fastadeFacto = []
cleanestInput = []
nearFullLengthDictionary = {}
startCodonDict = {}
#################################################
#################################################

i = 0
for line in file:
	title = '>'
	if line[0:1] == title:
		fastadeFacto.append(line)
		i += 1
	else:
		stripped = line.strip('\n')
		fastadeFacto.append(stripped)

cleanInput = "".join(fastadeFacto)
cleanerInput = cleanInput.split('>')
garbage = cleanerInput.pop(0)

i = 0
for ele in cleanerInput:
	marker = '\n'
	if ele.find(marker):
		ele.split('\n')
		cleanestInput.append(ele.split('\n'))
	i+=1

forDictionary = tuple(cleanestInput)
i = 0
while i < len(forDictionary):
	nearFullLengthDictionary[forDictionary[0 + i][0]] = forDictionary[0 + i][1]
	i += 1

for key, value in nearFullLengthDictionary.items():
	j = 0
	startCodonList = []
	while j < len(value) - 2:
		iCodon = value[j:j+3]
		if iCodon == startCodon:
			startCodonList.append(j)
			hereWeGo = tuple(startCodonList)
			startCodonDict[key] = hereWeGo
		j += 1

for key, value in sorted(startCodonDict.items()):
    print(key, value)

# stopCodonList = []
# for stopCodon in stopCodons:
# 	i = 0
# 	for key, value in nearFullLengthDictionary.items():
# 		while i < len(value) - 2:
# 			iCodon = value[i:i+3]
# 			if iCodon == stopCodon:
# 				stopCodonIndex = i
# 				if ((i + 3) - 20) % 3 == 0:
# 					stopCodonList.append(i)
# 				# print("There is a stop codon that is in frame with the first start codon at index", i)
# 		i += 1


# i = 0
# for key, value in nearFullLengthDictionary.items():
# 	print("Sequence #:", key)
# 	j = 0
# 	while j < len(value):
# 		iCodon = value[j:j+3]
# 		if iCodon == startCodon:
# 			print(j)
# 		j += 1
# 	print('\n')
# 	i +=1

for key, value in nearFullLengthDictionary.items():
	j = 0
	startCodonList = []
	while j < len(value) - 2:
		iCodon = value[j:j+3]
		if iCodon == startCodon:
			startCodonList.append(j)
			hereWeGo = tuple(startCodonList)
			startCodonDict[key] = hereWeGo
		j += 1

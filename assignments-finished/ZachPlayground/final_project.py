#################################################
#################Defining Variables:#############
#################################################
import os
file = open("9kb.over.reads.fasta", "r")
fileoutput = open('modified_project.txt', 'w')
startCodon = "ATG"
stopCodons = ["TGA", "TAG", "TAA"]
fastadeFacto = []
cleanestInput = []
nearFullLengthDictionary = {}
startCodonDict = {}
stopCodonDict = {}
#################################################
#################FILE CLEAN-UP:##################
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
#################################################
#################Dictionary######################
#################################################
forDictionary = tuple(cleanestInput)
# print(forDictionary)
i = 0
while i < len(forDictionary):
	nearFullLengthDictionary[forDictionary[0 + i][0]] = forDictionary[0 + i][1]
	i += 1
#################################################
#################Open Reading Frames#############
#################################################
# for key, value in nearFullLengthDictionary.items():
# 	j = 0
# 	startCodonList = []
# 	while j < len(value) - 2:
# 		iCodon = value[j:j+3]
# 		if iCodon == startCodon:
# 			startCodonList.append(j)
# 			hereWeGo = tuple(startCodonList)
# 			startCodonDict[key] = hereWeGo
# 		j += 1

# print(forDictionary[0][1].find(startCodon))

# stopCodonList = []
# for element in forDictionary:
# 	i = 0
# 	z = 0
# 	theBeginning = int(element[1][z].find(startCodon))
# 	for stopCodon in stopCodons:
# 		y = 0
# 		while y < len(element) - 2:
# 			mCodon = element[1][y:y+3]
# 			if mCodon == stopCodon:
# 				stopCodonIndex = y
# 				if ((stopCodonIndex + 3) - theBeginning) % 3 == 0:
# 					stopCodonList.append(stopCodonIndex)
# 					# print('A stop codon in frame with the first start codon was found at index', i)
# 			y += 1
# 		i += 1
# 		z += theBeginning

# stopCodonCount = 0
# stopCodonList = []
# for stopCodon in stopCodons:
# 	z = 0
# 	for element in forDictionary[z][1]:
# 		i = 0
# 		j = 0
# 		while i < len(element) - 2:
# 			name = element[0]
# 			iCodon = forDictionary[j][1][i:i+3]
# 			if iCodon == stopCodon:
# 				stopCodonList.extend((i, iCodon))
# 				# if ((i + 3) - 20) % 3 == 0: ###How do I make this number represent a variable list of items (start codon indices)
#  			# 		stopCodonList.append(i)
# 			i += 1
# 		j += 1
# 	z += 1

# i = 0
# sequence = forDictionary[i][1]
# while i < len(sequence)
# 	i += 1


i = 0
while i < len(forDictionary):
	key = forDictionary[i][0]
	mockList = []
	for basepair in forDictionary[i][1]:
		mockList.extend(basepair)
	mockString = "".join(mockList)
	# print('test1')
######################################	
######################################
	z = 0
	startCodonList = []
	while z < len(mockString) - 2:
		iCodon = mockString[z:z+3]
		if iCodon == startCodon:
			startCodonList.append(z)
		z += 1
		# print('test2')
######################################
######################################
	stopCodonList = []
	for stopCodon in stopCodons:
		x = 0
		j = 0
		while x < len(startCodonList) - 1:
			startCodonIndex = startCodonList[x]
			startFormula = int(startCodonIndex) + j
			iCodon = mockString[startFormula:startFormula + 3]
			# print ('test3')
			if iCodon == stopCodon:
				dataTransfer = startCodonIndex, (startCodonIndex+j)
				stopCodonList.append(dataTransfer)
				x += 1
				j = 0
			elif j > len(mockString):
				break
			else:
				j += 3
			print(x, j)
	x = 0
	fileoutput.write(str(key) + '\n' + str(stopCodonList) + '\n' + '\n' + '\n')
	i += 1



# print(nearFullLengthDictionary["m160813_184806_42269_c101085362550000001823239303091727_s1_p0/1424/ccs"])


# fileoutput.write(str(key) + '\n' + 'Start Codon (ATG):' + ':' + str(startCodonList[y]) + ' ' + 'Stop Codon' + str(stopCodon) + ':' + str(j) + '\n' + '\n')



# print(stopCodonDict)

# print(forDictionary[0][i])

# for key, value in nearFullLengthDictionary.items():
# 	for stopCodon in stopCodons:
# 		i = 0
# 		j = 0
# 		while i < len(value) - 2:
# 			mCodon = value[int(startCodonList[j])+1:i+3]
# 			if mCodon == stopCodon:
# 				stopCodonIndex = int(i)
# 				if ((stopCodonIndex + 3) - startCodonList[i]) % 3 == 0:
# 					stopCodonList.append(stopCodonIndex)
# 					a += 1
# 					break
# 			i += 1
# 		print(stopCodonList)

# # for key, value in sorted(startCodonDict.items()):
# #     print(key, value)

# # stopCodonList = []
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

# for key, value in nearFullLengthDictionary.items():
# 	j = 0
# 	startCodonList = []
# 	while j < len(value) - 2:
# 		iCodon = value[j:j+3]
# 		if iCodon == startCodon:
# 			startCodonList.append(j)
# 			hereWeGo = tuple(startCodonList)
# 			startCodonDict[key] = hereWeGo
# 		j += 1

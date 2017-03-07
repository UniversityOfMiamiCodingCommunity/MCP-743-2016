#################################################
#################Defining Variables:#############
#################################################
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
i = 0
while i < len(forDictionary):
	nearFullLengthDictionary[forDictionary[0 + i][0]] = forDictionary[0 + i][1]
	i += 1
#################################################
#################Translate Function##############
#################################################
def translate (key, seq):
	Isoleucine = ['I', 'ATT', 'ATC', 'ATA']
	Leucine = ['L', 'CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG']
	Valine = ['V', 'GTT', 'GTC', 'GTA', 'GTG']
	Phenylalanine = ['F', 'TTT', 'TTC']
	Methionine = ['M', 'ATG']
	Cysteine = ['C', 'TGT', 'TGC']
	Alanine = ['A', 'GCT', 'GCC', 'GCA', 'GCG']
	Glycine = ['G', 'GGT', 'GGC', 'GGA', 'GGG']
	Proline = ['P', 'CCT', 'CCC', 'CCA', 'CCG']
	Threonine = ['T', 'ACT', 'ACC', 'ACA', 'ACG']
	Serine = ['S', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
	Tyrosine = ['Y', 'TAT', 'TAC']
	Tryptophan = ['W', 'TGG']
	Glutamine = ['Q', 'CAA', 'CAG']
	Asparagine = ['N', 'AAT', 'AAC']
	Histidine = ['H', 'CAT', 'CAC']
	GlutamicAcid = ['E', 'GAA', 'GAG']
	AsparticAcid = ['D', 'GAT', 'GAC']
	Lysine = ['K', 'AAA', 'AAG']
	Arginine = ['R', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
	StopCodons = ['*', 'TAA', 'TAG', 'TGA']
	translatedSequence = []
	i = 0
	while i < len(seq) - 2:
		iCodon = seq[i:i+3]
		if iCodon in Isoleucine:
			translatedSequence.append("I")
			i += 3
		if iCodon in Leucine:
			translatedSequence.append("L")	
			i += 3		
		if iCodon in Valine:
			translatedSequence.append("V")	
			i += 3		
		if iCodon in Phenylalanine:
			translatedSequence.append("F")
			i += 3
		if iCodon in Methionine:
			translatedSequence.append("M")
			i += 3
		if iCodon in Cysteine:
			translatedSequence.append("C")
			i += 3
		if iCodon in Alanine:
			translatedSequence.append("A")
			i += 3
		if iCodon in Glycine:
			translatedSequence.append("G")
			i += 3
		if iCodon in Proline:
			translatedSequence.append("P")
			i += 3
		if iCodon in Threonine:
			translatedSequence.append("T")
			i += 3
		if iCodon in Serine:
			translatedSequence.append("S")
			i += 3
		if iCodon in Tyrosine:
			translatedSequence.append("Y")
			i += 3
		if iCodon in Tryptophan:
			translatedSequence.append("W")
			i += 3
		if iCodon in Glutamine:
			translatedSequence.append("Q")
			i += 3
		if iCodon in Asparagine:
			translatedSequence.append("N")
			i += 3			
		if iCodon in Histidine:
			translatedSequence.append("H")
			i += 3
		if iCodon in GlutamicAcid:
			translatedSequence.append("E")
			i += 3
		if iCodon in AsparticAcid:
			translatedSequence.append("D")
			i += 3
		if iCodon in Lysine:
			translatedSequence.append("K")
			i += 3
		if iCodon in Arginine:
			translatedSequence.append("R")
			i += 3
		if iCodon in StopCodons:
			translatedSequence.append("*")
			break
	fileDone = "".join(translatedSequence)
	fileNew = open('translated.txt', 'a')
	fileNew.write(str(key) + '\n' + str(fileDone) + '\n' + '\n')
#################################################
#################Transcribe######################
#################################################
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
	x = 0
	j = 0
	while x < len(startCodonList):
		startCodonIndex = startCodonList[x]
		startFormula = int(startCodonIndex) + j
		iCodon = mockString[startFormula:startFormula + 3]
		# print ('test3')
		if iCodon in stopCodons:
			dataTransfer = startCodonIndex, (startCodonIndex+j)
			stopCodonList.append(dataTransfer)
			x += 1
			j = 0
		elif j > len(mockString):
			break
		else:
			j += 3
		# print(x, j)
	x = 0
	# print(stopCodonList)
	# fileoutput.write(str(key) + '\n' + str(stopCodonList) + '\n' + '\n' + '\n')
	######################################
	######################################
	k = 0
	aCodonList = []
	while k < len(stopCodonList):
		aCodon = mockString[stopCodonList[k][0]:(stopCodonList[k][1]+3)]
		aCodonList.append(aCodon)
		fileoutput.write(str(key) + '\n' + str(aCodon) + '\n' + '\n' + '\n')
		k += 1
	# print(aCodonList)
	for ele in aCodonList:
		translate(key, ele)
	i += 1
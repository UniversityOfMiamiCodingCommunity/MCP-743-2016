file = open("9kb.over.reads.fasta", "r")
fileoutput = open('modified_project.txt', 'w')

fastadeFacto = []
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

cleanestInput = []
i = 0
for ele in cleanerInput:
	marker = '\n'
	if ele.find(marker):
		ele.split('\n')
		cleanestInput.append(ele.split('\n'))
	i+=1
	
forDictionary = tuple(cleanestInput)
nearFullLengthDictionary = {}

i = 0
while i < len(forDictionary):
	nearFullLengthDictionary[forDictionary[0 + i][0]] = forDictionary[0 + i][1]
	i += 1

keys = nearFullLengthDictionary.keys()
print(keys)

length = len(nearFullLengthDictionary)
print(length)
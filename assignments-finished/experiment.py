patientOneSequences = open("Class6_parsingAssignment_patient1readsOfInsert", "r")

nefPlasmidList = []

i = 0
for line in file:
	skip = line[0:1]
	if skip == '>':
		nefPlasmidList.append(line)
		i += 1

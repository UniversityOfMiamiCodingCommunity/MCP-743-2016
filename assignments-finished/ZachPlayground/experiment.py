patientOneSequences = open("Class6_parsingAssignment_patient1readsOfInsert.fasta", "r")

arbitrary = []

i = 0
for line in patientOneSequences:
	print(line)
	skip = line[0:1]
	if skip == '>':
		arbitrary.append(line)
		i += 1
print(i)
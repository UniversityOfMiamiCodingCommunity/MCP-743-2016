########################################################################################################################
# Assignment
# You have traveled to a new planet call Isom in the nearby Pharma solar system.
# You pull out the next next next next generation sequencer in your pocket and begin sequencing alien organisms. 
# Over the course of a day or two, you realize that life on this planet uses a radically different genetic code. 
# This code consists of 26 unique nucleobase you label from A-to-Z using the human english alphabet.
# You discover that, unlike life on earth, a codon on planet Isom consists of 6 nucleobases.
# You discover that, as with life on earth, there is only one start codon: "AYGOGO".
# You discover that, as with life on earth, there are three stop codons: "STOPME", "STOPIT", and "STOPGO"
# You have your obtained your first sequence:
########################################################################################################################
weirdAssDna = " XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"

# 1) Identify the index of each start codon in the DNA sequence. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon in the DNA sequence. 
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# Note: you must use at least one "for" and "while" loop in your approach.
# May the force be with you.
#########################################################################################################################

#Final Version :) ~Jazzy



# 1 and  2) Index of each start codon

startCodons = ["AYGOGO"]

startCodonCount = 0
i = 0
for startCodon in startCodons:
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == startCodon:
			print("Found start codon", iCodon, "at index", i) 
			startCodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", startCodonCount)

#startcodon at index 31
 


#3) Stop codons and indencies

stopCodons = ["STOPGO", "STOPIT", "STOPME"]

stopCodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopCodon:
			print("Found stop codon", iCodon, "at index", i) 
			stopCodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", stopCodonCount)

# STOPGO at 85, STOPIT at 139, STOPME at 127


#4 in frame

startCodon = "AYGOGO"
stopCodons = ["STOPGO", "STOPIT", "STOPME"]

#Found index of 1st start codon

startCodonIndex = weirdAssDna.find(startCodon)
print(startCodonIndex)

#Find indencies of all stop codons

i = startCodonIndex
firststopCodonIndex = 0
firststopCodon = ""
while i < len(weirdAssDna) - 5:
	iCodon = weirdAssDna[i: i + 6]
	if iCodon in stopCodons:
		print(iCodon, i)
		firststopCodon = iCodon
		firststopCodonIndex = i
		break
	i += 1
print("The stop codon in frame with start codon is", firststopCodon, "at index", firststopCodonIndex)

#




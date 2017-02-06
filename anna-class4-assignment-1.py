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
startCodon = "AYGOGO"
stopCodons = ["STOPME", "STOPIT", "STOPGO"]

# 1) Identify the index of each start codon in the DNA sequence. 
index = 0
while index < len(weirdAssDna):
	index = weirdAssDna.find(startCodon, index)
	if index == -1:
		break
	print('There was a start codon found at position', index)
	index += 1

# 2) Get the index of the first start codon.
startCodonIndex = weirdAssDna.find(startCodon)
print('The first stop codon is located at position', startCodonIndex)

# 3) Identify the index of each stop codon in the DNA sequence. 
for stopCodon in stopCodons:
	index = 0
	while index < len(weirdAssDna):
		index = weirdAssDna.find(stopCodon, index)
		if index == -1:
			break
		print('There was a', stopCodon, 'stop codon found at position', index)
		index += 1
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
stopCodonsFound = []
for stopCodon in stopCodons:
	index = 31
	while index < len(weirdAssDna):
		index = weirdAssDna.find(stopCodon, index)
		if index == -1:
			break
		stopCodonsFound.append(index)
		index += 6
print('The first in frame stop codon is found at location', min(stopCodonsFound))

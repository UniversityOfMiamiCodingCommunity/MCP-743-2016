########################################################################
# Assignment
# You have traveled to a new planet call Isom in the nearby Pharma solar system.
# You pull out the next next next next generation sequencer in your pocket and begin sequencing alien organisms. 
# Over the course of a day or two, you realize that life on this planet uses a radically different genetic code. 
# This code consists of 26 unique nucleobases you label from A-to-Z using the human english alphabet.
# You discover that, unlike life on earth, a codon on planet Isom consists of 6 nucleobases.
# You discover that, as with life on earth, there is only one start codon: "AYGOGO".
# You discover that, as with life on earth, there are three stop codons: "STOPME", "STOPIT", and "STOPGO"
# You have your obtained your first sequence:
# 1) Identify the index of each start codon in the DNA sequence. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon in the DNA sequence. 
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# Note: you must use at least one "for" and "while" loop in your approach.
# May the force be with you.
########################################################################

weirdAssDna = " XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"

########################################################################

#  1)

startCodon = "AYGOGO"

i = 0
while i < len(weirdAssDna) - 5:
	codon = weirdAssDna[i:i+6]
	if codon == startCodon:
		print(codon, i)
	i =+ i + 1

#  2)

i = 0
while i < len(weirdAssDna) - 5:
	codon = weirdAssDna[i:i+6]
	if codon == startCodon:
		print(i)
		break
	i =+ i + 1

#  3) + 4)

stopCodons = ["STOPME","STOPIT","STOPGO"] 
startIndex=weirdAssDna.find(startCodon)

for stopCodon in stopCodons:
	i = 0
	while i < len(weirdAssDna) - 5:
		codon = weirdAssDna[i:i+6]
		if codon == stopCodon:
			stopIndex = i
			if ((stopIndex + 6) - startIndex) % 6 == 0:
				firstStopCodon = codon
				firstStopCodonIndex = stopIndex
				print(codon, i)
		i = i + 1 
print("First in-frame stop codon: " + firstStopCodon, firstStopCodonIndex)

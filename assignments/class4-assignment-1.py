########################################################################################################################
# Assignment
# You discover that, as with life on earth, there is only one start codon: "AYGOGO".
# You have traveled to a new planet call Isom in the nearby Pharma solar system.
# You pull out the next next next next generation sequencer in your pocket and begin sequencing alien organisms. 
# Over the course of a day or two, you realize that life on this planet uses a radically different genetic code. 
# This code consists of 26 unique nucleobases you label from A-to-Z using the human english alphabet.
# You discover that, unlike life on earth, a codon on planet Isom consists of 6 nucleobases.
# You discover that, as with life on earth, there are three stop codons: "STOPME", "STOPIT", and "STOPGO"
# You have your obtained your first sequence:
########################################################################################################################
weirdAssDna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"

# 1) Identify the index of each start codon in the DNA sequence. 

startCodon = "AYGOGO"
stopCodon = ["STOPME", "STOPIT", "STOPGO"]

i = 0
while i < len(weirdAssDna) - 5:
	iCodon = weirdAssDna[i:i+6]
	if iCodon == startCodon:
		print("Found start codon", iCodon, "at index", i)
	i += 1

# 2) Get the index of the first start codon.

startCodon = "AYGOGO"
print(weirdAssDna.find(startCodon))

# 3) Identify the index of each stop codon in the DNA sequence. 

stopCodons = ["STOPME", "STOPIT", "STOPGO"]

stopCodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopCodon:
			print("Found stop codon", iCodon, "at index", i)
			stopCodonCount += 0
		i += 1

# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.

startCodonIndex = weirdAssDna.find(startCodon)

minStopCodon, minStopCodonIndex = "", 10000000 
for stopCodon in stopCodons:
	i = 0
	while i < len(weirdAssDna) - 5:
		mCodon = weirdAssDna[i:i+6]
		if mCodon == stopCodon:
			stopCodonIndex = i
			print(stopCodonIndex)
			if ((stopCodonIndex + 6) - startCodonIndex) % 6 == 0:
				if stopCodonIndex < minStopCodon:
					minStopCodon = mCodon
					minStopCodonIndex = stopCodonIndex
					print("In frame Stop Codon is:", mCodon, i)
		i += 1




# Note: you must use at least one "for" and "while" loop in your approach.
# May the force be with you.
#########################################################################################################################

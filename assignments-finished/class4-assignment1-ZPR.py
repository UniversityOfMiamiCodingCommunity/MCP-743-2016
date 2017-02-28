########################################################################################################################
# Assignment
# You have traveled to a new planet call Isom in the nearby Pharma solar system.
# You pull out the next next next next generation sequencer in your pocket and begin sequencing alien organisms. 
# Over the course of a day or two, you realize that life on this planet uses a radically different genetic code. 
# This code consists of 26 unique nucleobases you label from A-to-Z using the human english alphabet.
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
weirdAssDna = " XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
startCodon = ["AYGOGO"]
stopCodons = ["STOPME", "STOPIT", "STOPGO"]

# 1 
# Only found one stop codon.
startCodonCount = 0
for startCodon in startCodon:
	i = 0
	while i < len(weirdAssDna) - 6:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == startCodon:
			print("Found start codon,", iCodon, "at index", i)
			startCodonCount += 1
		i += 1
#######################################################################
print("\n")
#######################################################################

# 2
print("The index of the first start codon is:", weirdAssDna.index("AYGOGO"))
########################################################################
print("\n")
########################################################################

#3 
stopCodonCount = 0
for stopCodon in stopCodons:
	i = 0
	while i < len(weirdAssDna) - 6:
		nCodon = weirdAssDna[i:i+6]
		if nCodon == stopCodon:
			print("Found stop codon:", nCodon, "at index", i)
			stopCodonCount += 1
		i += 1
########################################################################
print("\n")
########################################################################
			
# 4
weirdAssDna = " XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
startCodon = ["AYGOGO"]
stopCodons = ['STOPME', 'STOPIT', 'STOPGO']

StopCodonsFound = []
for stopCodon in stopCodons:
	i = weirdAssDna.find(stopCodon)
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopCodon:
			if ((i-30) + 5) % 6 == 0:
				StopCodonsFound.append(i)
		i += 6
		
# print(min(StopCodonsFound))# This just prints the index, not the stop codon.

print("The first in frame stop codon is: " + str(weirdAssDna[85:91]) + " and is found at position " + str(min(StopCodonsFound)) + ".") 

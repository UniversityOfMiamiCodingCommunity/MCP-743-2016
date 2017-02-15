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
dna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"

# 1) Identify the index of each start codon in the DNA sequence. 
# 2) Get the index of the first start codon.
# 3) Identify the index of each stop codon in the DNA sequence. 
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# Note: you must use at least one "for" and "while" loop in your approach.
# May the force be with you.
#########################################################################################################################
start_codon = "AYGOGO"
stopcodons = ['STOPME', 'STOPIT', 'STOPGO']

# # 1)
i = 0
while True:
	i = dna.find(start_codon, i + 1)
	if i == -1: break
	print("Found start codon at index:", i)

# # 2)
start_codon1 = dna.find(start_codon)
print("Found first start codon at index:", start_codon1)

# 3)
for stopcodon in stopcodons:
	i = 0
	while i < len(dna) - 5:
		iCodon = dna[i:i+6]
		if iCodon == stopcodon:
			print("Found stop codon", iCodon, "at index", i) 
		i += 6
# 4)
StopCodonsFound = []
for stopcodon in stopcodons:
	i = dna.find(start_codon)
	while i < len(dna) - 5:
		iCodon = dna[i:i+6]
		if iCodon == stopcodon:
			if ((i-int(start_codon1)) + 6) % 6 == 0:
				StopCodonsFound.append(i)	
		i += 6

print("The first in frame stop codon is", dna[min(StopCodonsFound) : min(StopCodonsFound) + 6], "at location", min(StopCodonsFound))			




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

startcodon = "AYGOGO"

stopcodon = ["STOPME", "STOPIT", "STOPGO"]

#1) and 2) Index of each start codon


startcodonCount = 0
for startcodon in startcodon:
	i = 0
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == startcodon:
			print("Found start codon", iCodon, "at index", i) 
			startcodonCount += 1
		i += 1
print("The total number of start codons found in the DNA sequence is:", startcodonCount)

#1 startcodon at index 31; popped up 6 times though :/ 


#3) Stop codons

stopcodonCount = 0
for stopcodon in stopcodon:
	i = 0
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopcodon:
			print("Found start codon", iCodon, "at index", i) 
			stopcodonCount += 1
		i += 1
print("The total number of stop codons found in the DNA sequence is:", stopcodonCount)

# "STOPGO" at 85, "STOPME" at 127 and 'STOPIT" at 139


#4
for stopCodon in stopcodon:
	i = weirdAssDna(startCodon)
while i < len(weirdAssDna) - 5:
	iCodon = weirdAssDna[i:i+6]
	if iCodon == stopcodon:
		if ((i-19) + 2) % 3 == 0
print("Found stop codon", iCodon, "at index", i) 			
i += 1
print("Found in frame stop codon TAA at index 65")

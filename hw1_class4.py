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
start_codon = "AYGOGO"
stop_codons = ['STOPME', 'STOPIT', 'STOPGO']

# 1) Identify the index of each start codon in the DNA sequence. 
start_codon_count = 0
while start_codon_count < len(weirdAssDna):
	start_codon_count = weirdAssDna.find('AYGOGO', start_codon_count)
	if start_codon_count == -1:
		break
	print('Start codon found at ', start_codon_count)
	start_codon_count += 5
print("\n")


# 2) Get the index of the first start codon.
print("Index of the first start codon is:" , weirdAssDna.find(start_codon))
print("\n")	

# 3) Identify the index of each stop codon in the DNA sequence. 
stop_codon_count = 0
for stop_codon in stop_codons:
	i = 0
	while i < len(weirdAssDna) -5:
		in_codon = weirdAssDna[i:i+6]
		if in_codon == stop_codon:
			print("Stop codon ", in_codon, "found at index", i)
print("\n")			


# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
# Note: you must use at least one "for" and "while" loop in your approach.
# May the force be with you.
#########################################################################################################################
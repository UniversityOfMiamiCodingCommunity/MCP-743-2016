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

#1) Identify the index of each start codon in the DNA sequence.

startCodon = "AYGOGO"
stopCodons = ["STOPME","STOPIT","STOPGO"]

print 'Question 1'
i = 0
while i < len(weirdAssDna) - 5:
	iCodon = weirdAssDna[i:i+6]
	if iCodon == startCodon:
		print "Found start codon " + str(iCodon) + " at index " + str(i) 
	# Increment the index counter.
	##############################
	i += 1

#2) Identify the index of the first start codon.

firststart = weirdAssDna.find(startCodon)
print '\n'
print 'Question 2'
print 'The first start codon is found at index ' + str(firststart)

#3) Identify the index of each stop codon in the DNA sequence.

## Question 3 with 'while' loop:

print '\n'
print 'Question 3 with while loop:'
for stopCodon in stopCodons: 
	i = 0
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopCodon:
			print "Found stop codon " + str(iCodon) + " at index " + str(i) 
		# Increment the index counter.
		##############################
		i += 1
		
## Question 3 with 'for' loop:

print '\n'
print 'Question 3 with for loop:'
for stopCodon in stopCodons: 
	i = 0
	stop_pos = len(weirdAssDna) - 5
	for i in range(0,stop_pos):
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopCodon:
			print "Found stop codon " + str(iCodon) + " at index " + str(i) 
		# Increment the index counter.
		##############################
		i += 1

# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.

print '\n'
print 'Question 4'
ORF = weirdAssDna[firststart:]	
index=[]
subset_index=[]
for stopCodon in stopCodons:
	stopCodonSearchResult = ORF.find(stopCodon)
	index.append(stopCodonSearchResult)
for value in index:
	if value % 6 == 0:
		subset_index.append(value)
minimum = min(subset_index)
codon_label = ORF[minimum:minimum+6]
final_index = firststart + minimum	
print "The stop codon that is in frame with the first start codon is " + codon_label + ", located at index " + str(final_index)


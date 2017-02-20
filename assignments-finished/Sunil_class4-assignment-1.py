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
startCodon = "AYGOGO"
stopCodons = ["STOPME", "STOPIT", "STOPGO"]
weirdAssDna=weirdAssDna.lstrip()
# 1) Identify the index of each start codon in the DNA sequence.
i=0
while i<len(weirdAssDna)-5:
	icodon=weirdAssDna[i:i+6]
	if icodon==startCodon:
		print("A start codon, "+startCodon+ ", was found at index: "+str(i))
	i +=1 
# 2) Get the index of the first start codon.
firststartcodon=weirdAssDna.find(startCodon)
print("The index of the first start codon is: "+str(firststartcodon))
# 3) Identify the index of each stop codon in the DNA sequence. 
stopCodonCount = 0
for stopCodon in stopCodons:
	j = 0
	while j < len(weirdAssDna) - 5:
		jcodon = weirdAssDna[j:j+6]
		if jcodon == stopCodon:
			print("A stop codon: "+jcodon+" was found at index:" +str(j)) 
			stopCodonCount += 1
		j += 1
# 4) Identify the stop codon, and it's index that is in frame with the first start codon encountered in the DNA sequence.
for stopCodon in stopCodons:
	k=firststartcodon
	while k<len(weirdAssDna)-5:
		kcodon=weirdAssDna[k:k+6]
		if kcodon==stopCodon:
			print("A stop codon, "+kcodon+",in frame with the start codon was found at index: "+str(k))
		k +=6
# Note: you must use at least one "for" and "while" loop in your approach.
# May the force be with you.
#########################################################################################################################

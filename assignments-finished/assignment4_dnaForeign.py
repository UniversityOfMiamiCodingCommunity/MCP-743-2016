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

#1 Finds all start codons
#######################
print('Answer 1:')
startCodon = "AYGOGO"
weirdAssDna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"

index = 0
while index < len(weirdAssDna):
    index = weirdAssDna.find(startCodon, index)
    if index == -1: 
        break
    print('Start index AYGOGO found at ', index)
    index += 1


#2 Finds only first start codon
#############################
print('\nAnswer 2: First start codon found at ')
startCodon = "AYGOGO"
weirdAssDna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
print(weirdAssDna.find(startCodon))


#3 Finds all stop codons one at a time
######################################
print('\nAnswer 3: ')
weirdAssDna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
stopCodons = ["STOPME", "STOPIT", "STOPGO"]

i = 0
while i < len(weirdAssDna):
    i = weirdAssDna.find('STOPME', i) 
    if i == -1:
        break
    print('Stop index STOPME found at ', i)
    i += 1

i = 0
while i < len(weirdAssDna):
    i = weirdAssDna.find('STOPIT', i)
    if i == -1:
        break
    print('Stop index STOPIT found at ', i)
    i += 1

i = 0
while i < len(weirdAssDna):
    i = weirdAssDna.find('STOPGO', i)
    if i == -1:
        break
    print('Stop index STOPGO found at ', i)
    i += 1

#3 Finds every stop codon at once but only the first one of each
print('\nAnswer 3: More concise coding but less precise readout')
weirdAssDna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
stopCodons = ["STOPME", "STOPIT", "STOPGO"]
for stopCodon in stopCodons:
    print(weirdAssDna.find(stopCodon))


#4 Finds stopcodon in frame
###########################
#Setting parameters
print('\nAnswer 4: ')
weirdAssDna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
startCodon = 'AYGOGO'
stopCodons = ['STOPME', 'STOPIT', 'STOPGO']
startCodon_slice = []
ORF = []
ORF_Full = []

#Finding Open reading frame
startCodon_slice = ['{}{}'.format(startCodon, s) for s in weirdAssDna.split(startCodon) if s]
ORF = startCodon_slice[1:]
ORF_Full =''.join(ORF)
print('Open Reading frame is ', ORF_Full)
start_index = weirdAssDna.find(startCodon)

#Finding stop Codons within reading frame
for stopCodon in stopCodons:
    #this negates the while loop #print(ORF_Full.find(stopCodon) + start_index)
    i = 0
    while i < len(ORF_Full):
        iCodon = ORF_Full.find(stopCodon) 
        stop_index = ORF_Full[i:i+6]
        if i == iCodon: #This ensures codons are in frame if counting by 1 #and (i + 6) % 6 == 0:
            print ('Found stop index ', stop_index, 'in open reading frame at', i + start_index)   
            break
        i += 6



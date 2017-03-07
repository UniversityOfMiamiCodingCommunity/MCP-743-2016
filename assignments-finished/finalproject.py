#abca1 is a transpoter protein responsibile for cholesterol efflux
#reduced abca1-->reduced lipid droplet formation in DKD
#tnfalpha is a cell signaling protein reported to function very similarly to abca1
#since knockout of both has been reported to have nearly identical effects, I wanted to compare them. 
fileinput = open ("abca1.fasta", "r")
#print(fileinput)
# line in fileinput: 
	#print(line)
dna = ""
for line in fileinput:
	dna += line[0:-1]
print(dna)
print(len(dna))
fileinput2 = open ("tnfa.fasta","r")
dna2 =""
for line in fileinput2:
	dna2 += line[0:-1]
print(dna2)
print(len(dna2))
#difference in length  
import difflib
seq = difflib.SequenceMatcher()
seq.set_seqs(dna.lower(), dna2.lower())
d = seq.ratio()*100
print(d)
#sequencesimilarity
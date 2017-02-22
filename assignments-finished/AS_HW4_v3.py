dna = "XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISHEMRXDCFWRSTOPMEYWTSGBSTOPITYTGEBSOIMNEY"
startcodon = "AYGOGO"
stopcodons = ['STOPME' ,  'STOPGO' ,  'STOPIT']

#1
i = 0
while True:
	i = dna.find(startcodon, i + 1)
	if i == -1: break
	print("Start codon found at index:", i)

#2
firststartcodon_ind = dna.find(startcodon)
print("First start codon found at index:", firststartcodon_ind)

#3
sc1 ="STOPME"
result3a = dna.find(sc1)
print(result3a)
sc2 = "STOPIT"
result3b = dna.find(sc2)
print(result3b)
sc3 = "STOPGO"
result3c = dna.find(sc3)
print(result3c)

#4
dnanew = dna[firststartcodon_ind:]	
index=[]
subset_index=[]
for stopcodon in stopcodons:
	stopcodonrelindex = dnanew.find(stopcodon)
	index.append(stopcodonrelindex)
for num in index:
	if num % 6 == 0:
		subset_index.append(num)
low = min(subset_index)
codon = dnanew[low:low+6]
findex = firststartcodon_ind + low
print("The stop codon relative to the first start codon is " + codon + ", at index " + str(findex))



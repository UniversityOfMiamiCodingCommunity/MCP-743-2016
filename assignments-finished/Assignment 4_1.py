weirdAssDna="XUIOPDEHSUJQPQHDUMIEYDHNAPQLKGAYGOGODKSIGJIEHYSNOEKUJNPOQGTSFKSOJWNEIMSQYEBZXAUQGTBHSTOPGOBCDAFROKMYEVGSYJENUQTFARISH"
 #1
startCodon = "AYGOGO"
i = 0
while True: 
	i = weirdAssDna.find(startCodon, i + 1)
	if i == -1:break
	print("startCodon found at index:", i)
#2
startcodon = "AYGOGO"
result2 = weirdAssDna.find(startcodon)
print(result2)
#3
stopcodons = ["STOPME", "STOPIT", "STOPGO"]
for stopcodon in stopcodons: 
	i = 0
	while i < len(weirdAssDna) - 5:
		iCodon = weirdAssDna[i:i+6]
		if iCodon == stopcodon:
			print("Stopcodon", i, "index", i)
		i += 1
#4
stopcodon3 = "STOPGO"
i = 0
while True: 
	i = weirdAssDna.find(stopcodon3, i + 1)
	if i == -1:break
	print("stopcodon in same frame as startcodon at index", i)

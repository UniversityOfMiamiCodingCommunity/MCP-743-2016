class stats :
	def __init__(self, datastr) :
		self.mean = None
		self.mode = None
		self.median = None
		self.variance = None
		self.stdev = None
		self.datastr = datastr
	def statsres(self) :

		self.mean = sum(self.datastr) / len(self.datastr)

		counter = {}
		for n in self.datastr :
			subcounter = 0
			for k in self.datastr :
				if n == k:
					subcounter += 1
				else:
					subcounter += 0
				counter[n] = subcounter
		self.mode = max(counter, key = lambda i: counter[i])
		
		g = len(self.datastr)
		h = int(g/2)
		datastrSorted = sorted(self.datastr)
		if g/2 == int(g/2) :
			median = sum(datastrSorted[h-1 : h+1])/2
		else :
			median = datastrSorted[h]
		self.median = median

		sumSquares = 0
		for l in self.datastr:
			sumSquares = sumSquares + l**2
		variance = sumSquares/len(self.datastr) - self.median**2
		self.variance = variance

		self.stdev = variance**0.5

	def showResults(self):

		return "Mean value is:" + str(self.mean)

testInstance = stats([1,6,2,7,3,8,3,7,0,24,76,34,6,8,3])
testInstance.statsres()
result = testInstance.showResults()
print result

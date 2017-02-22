class stats :
	def __init__(self, datastr) :
		self.mean = None
		self.mode = None
		self.median = None
		self.variance = None
		self.stdev = None
		datastr = [1,6,2,7,3,8,3,7,0,24,76,34,6,8,3]
	def statsres(self, datastr) :

		self.mean = sum(datastr) / len(datastr)

		counter = {}
		for n in datastr :
			subcounter = 0
			for k in datastr :
				if n == k:
					subcounter += 1
				else:
					subcounter += 0
				counter[n] = subcounter
		self.mode = max(counter, key = lambda i: counter[i])
		
		g = len(datastr)
		h = int(g/2)
		datastrSorted = sorted(datastr)
		if g/2 == int(g/2) :
			median = sum(datastrSorted[h-1 : h+1])/2
		else :
			median = datastrSorted[h]
		self.median = median

		sumSquares = 0
		for l in datastr:
			sumSquares = sumSquares + l**2
		variance = sumSquares/len(datastr) - self.median**2
		self.variance = variance

		self.stdev = variance**0.5


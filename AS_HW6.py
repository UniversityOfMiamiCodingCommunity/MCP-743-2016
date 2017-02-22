def quadsolver(a, b, c) :
	if b**2 - 4 * a *c < 0 :
		print("Error, equation had imaginary roots")
	if b**2 - 4 * a *c >= 0 :
		x1 = (- b + ((b**2 - 4 * a *c)**0.5)) / (2 * a)
		x2 = (- b - ((b**2 - 4 * a *c)**0.5)) / (2 * a)
		print("The roots of the quadratic are ",x1,"and ",x2,".")
		return x1
		return x2

a = 4
b = 10
c = 1
quadsolver(a, b, c)


def slopecalc(P1, P2) :
	u1 = int(P1[1:2])
	u2 = int(P1[4:5])
	v1 = int(P2[1:2])
	v2 = int(P2[4:5])
	slop = ((v2 - v1)/(u2 - u1))
	print("The slope is ",slop,".")
	return slop
P1 = "(2, 3)"
P2 = "(4, 8)"
slopecalc(P1, P2)

class stats :
	def __init__(self) :
		self.mean = None
		self.mode = None
		self.median = None
		self.variance = None
		self.stdev = None

	def statsres(self) :

		if self.mean :
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

datastr = [1,6,2,7,3,8,3,7,0,24,76,34,6,8,3]
q = stats(datastr)
q.mean
#datastr = [1,6,2,7,3,8,3,7,0,24,76,34,6,8,3]
#output = stats(datastr)
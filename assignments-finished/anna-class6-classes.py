class Microarray:

	def __init__(self):

		# Class attributes that describe the object.
		# Key vocabulary term: class attribute
		############################################
		self.geneName = None
		self.tcgaMedian = None
		self.newlyDiagnosedMedian = None
		self.recurrentMedian = None

	# A class method, i.e. a function, that takes class attributes as arguments.
	# Key vocabulary term: class method or class function.
	############################################################################
	def printAttributes(self):

		if self.geneName:
			print("Gene Name:", self.geneName)
		if self.tcgaMedian:
			print("TCGA Median log2 FC:", self.tcgaMedian)
		if self.newlyDiagnosedMedian:
			print("Newly Diagnosed Median log2 FC:", self.newlyDiagnosedMedian)
		if self.recurrentMedian:
			print("Recurrent Median log2 FC", self.recurrentMedian)

gene1 = Microarray()
gene1.geneName = "ABCA8"
gene1.tcgaMedian = 2.1968
gene1.newlyDiagnosedMedian = 0.1446
gene1.recurrentMedian = 0.641467892
gene1.printAttributes()

gene2 = Microarray()
gene2.geneName = "ABCD2"
gene2.tcgaMedian = 1.903333333
gene2.newlyDiagnosedMedian = 0.0426
gene2.recurrentMedian = 1.2829
gene2.printAttributes()

gene3 = Microarray()
gene3.geneName = "AK3L1"
gene3.tcgaMedian = 0.5798
gene3.newlyDiagnosedMedian = -0.797
gene3.recurrentMedian = 0.0485
gene3.printAttributes()
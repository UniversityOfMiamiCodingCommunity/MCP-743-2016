class gene:

	def __int__(self):
		self.gene_symbol = None
		self.position = None
		self.sequence = None
		self.disease = None

	def printAttributes(self):
		if self.gene_symbol:
			print("Gene symbol: ", self.gene_symbol)
		if self.location:
			print("Location: ", self.location)
		if self.genomic_coordinates:
			print("Genomic coordinates: ", self.genomic_coordinates)
		if self.sequence:
			print("Sequence: ", self.sequence)
		if self.disease:
			print("Related disease:", self.disease)

first_gene = gene()
first_gene.gene_symbol = "BRCA1"
first_gene.location = "17q21.31"
first_gene.genomic_coordinates = "17:43,044,294-43,125,482"
first_gene.sequence = "[very long]"
first_gene.disease = "breast and ovarian cancer"
first_gene.printAttributes()
print("\n")

second_gene = gene()
second_gene.gene_symbol = "BRCA2"
second_gene.location = "13q12.3"
second_gene.genomic_coordinates = "13:32,315,479-32,399,671"
second_gene.sequence = "[very long]"
second_gene.disease = "breast and ovarian cancer"
second_gene.printAttributes()
print("\n")

third_gene = gene()
third_gene.gene_symbol = "HTT"
third_gene.location = "4p16.3"
third_gene.genomic_coordinates = "4:3,074,509-3,243,959"
third_gene.sequence = "[very long]"
third_gene.disease = "Huntington's disease"
third_gene.printAttributes()
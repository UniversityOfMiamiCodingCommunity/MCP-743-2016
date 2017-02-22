# Class for SNPs.
#################
class SNP:

	def __init__(self,rsid,gene,function,MAF):

		# Class attributes that describe the object.
		############################################
		self.rsid = rsid
		self.gene = gene
		self.function = function
		self.MAF = MAF

	# A class method, i.e. a function, that takes class attributes as arguments.
	# Key vocabulary term: class method or class function.
	############################################################################
		
	def major_allele_freq(self)
		major_freq = 1 - self.MAF
		print self.rsid + "is in " + self.gene.title() + "and has a minor allele frequency of " self.MAF "and a major allele frequency of " + major_freq

SNP1 = SNP()
# Populate the attributes of the class 
SNP1.rsid = 
SNP1.gene = 
SNP1.function = 
SNP1.MAF = 
SNP1.major_allele_freq()



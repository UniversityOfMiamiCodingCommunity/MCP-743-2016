# Class for SNPs.
#################
class SNP(object):

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
		
	def major_allele_freq(self):
		major_freq = 1 - self.MAF
		print self.rsid + " is in " + self.gene + " and has a minor allele frequency of " + str(self.MAF) + " and a major allele frequency of " + str(major_freq)

SNP1 = SNP('rs3007421','PLEKHG5','intronic',0.12)
SNP1.major_allele_freq()

SNP2 = SNP('rs9282641','CD86','UTR5',0.08)
SNP2.major_allele_freq()

SNP3 = SNP('rs3453643','TYK2','exonic',0.05)
SNP3.major_allele_freq()







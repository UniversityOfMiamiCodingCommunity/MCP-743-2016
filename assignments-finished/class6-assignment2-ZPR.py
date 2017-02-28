##############
# Date 2/20/17
##############
# Zach Rivas
##############


# A Class for Bacteria.
#######################
class Bacteria: 
 
	def __init__(self): 

		# Define attributes that describe the object, which in this case is a bacteria.
		###############################################################################
		self.lps = None 
		self.oantigen = None
		self.antibioticResistant = None
		self.toxin = None
		
	# Define a function for the bacteria
	####################################################################
	def printAttributes(self): 

		if self.lps:
			print("The LPS layer is:", self.lps)
		if self.oantigen:
			print("The O-antigen is:", self.oantigen)
		if self.antibioticResistant:
			print("The bacteria has antibiotic resististance to:", self.antibioticResistant)
		if self.toxin:
			print("The toxin produced is:", self.toxin)
			
# Created instance for Escherichia coli.
#########################################
Ecoli = Bacteria() 
Ecoli.lps = "Present" 
Ecoli.oantigen = "O:78" 
Ecoli.antibioticResistant = "Penicillin; Streptomycin"
Ecoli.toxin = "Endotoxins"
Ecoli.printAttributes()


###########
print("\n")
###########

# Created instance for Staphylococcus aureus
############################################
Saureus = Bacteria()
Saureus.lps = "Absent"
Saureus.oantigen = "None"
Saureus.antibioticResistant = "Methicillin"
Saureus.toxin = "Exotoxin"
Saureus.printAttributes()


###########
print("\n")
###########


# Created instance for Yersinia pseudotuberculosis
##################################################
Ypsuedotb = Bacteria()
Ypsuedotb.lps = "Present"
Ypsuedotb.oantigen = "O:8"
Ypsuedotb.antibioticResistant = "Ampicillin, Cephalothin, Erythromycin, Streptomycin, and Tetracycline"
Ypsuedotb.toxin = "Endotoxin"
Ypsuedotb.printAttributes()

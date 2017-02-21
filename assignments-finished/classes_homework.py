# smallMolecules is a class to store some basic information about a small molecule of interest. Within the class is a function that determines whether or not
# the small molcule's attributes meet Lipinski's rule.
#############################################################################################################################################################

class smallMolecules():
	"""General description of small molecules"""
	
	def __init__(self, name, MW, HBD, HBA, logP):
		"""Initialize attributes for the small molecule"""
		self.name = name
		self.MW = MW
		self.HBD = HBD
		self.HBA = HBA
		self.logP = logP
			
	def lipinski(self):
		
		# MW less than 300
		if self.MW < 300:
			print(self.name.title() + " " + "has a molecular weight that meets Lipinski's rule: " + str(self.MW))
		else:
			print(self.name.title() + " " + "has a molecular weight that DOES NOT meet Lipinski's rule: " + str(self.MW))
		
		# No more than 5 H-bond donors
		if self.HBD <= 5:
			print(self.name.title() + " " + "has a number of hydrogen bond donors that meets Lipinski's rule: " + str(self.HBD))
		else:
			print(self.name.title() + " " + "has a number of hydrogen bond donors that DOES NOT meet Lipinski's rule: " + str(self.HBD))
		
		# No more than 10 H-bond acceptors
		if self.HBA <= 10:
			print(self.name.title() + " " + "has a number of hydrogen bond acceptors that meets Lipinski's rule: " + str(self.HBA))
		else:
			print(self.name.title() + " " + "has a number of hydrogen bond acceptors that DOES NOT meet Lipinski's rule: " + str(self.HBA))
		
		# An octanol-water partition coefficient not greater than 5
		if self.logP <= 5:
			print(self.name.title() + " " + "has an octanol-water partition coefficient that meets Lipinski's rule: " + str(self.logP))
		else:
			print(self.name.title() + " " + "has an octanol-water partition coefficient that DOES NOT meet Lipinski's rule: " + str(self.logP))

			
smallMolecule_1 = smallMolecules('morphine', 285.14, 2, 2, 0.8)
smallMolecule_1.lipinski()

smallMolecule_2 = smallMolecules('acetaminophen', 151.06, 2, 2, 1.08)
smallMolecule_2.lipinski()

smallMolecule_3 = smallMolecules('nicotine', 162.12, 0, 2, 1.49)
smallMolecule_3.lipinski()



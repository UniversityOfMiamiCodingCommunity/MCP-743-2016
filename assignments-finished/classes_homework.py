# smallMolecules is a class to store some basic information about a small molecule of interest. Within the class is a function that determines whether or not the small molecule's attributes meet Lipinski's rule.
###################################################################################################################################################################################################################

class smallMolecules():
	"""General description of small molecules"""
	
	def __init__(self):
		"""Initialize attributes for the small molecule"""
		self.name = None
		self.MW = None
		self.HBD = None
		self.HBA = None
		self.logP = None

	def attributes(self):
		if self.name:
			print('Name: ', self.name.title())
		if self.MW:
			print('Molecular Weight: ', self.MW)
		if self.HBD:
			print('Number of hydrogen bond donors: ', self.HBD)
		if self.HBA:
			print('Number of hydrogen bond acceptors: ', self.HBA)
		if self.logP:
			print('Octanol-water partition coefficient: ', self.logP)

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

			
# Instance number one
#####################
smallMolecule_1 = smallMolecules()
smallMolecule_1.name = 'morphine'
smallMolecule_1.MW = 285.14
smallMolecule_1.HBD = 2
smallMolecule_1.HBA = 2
smallMolecule_1.logP = 0.8

smallMolecule_1.lipinski()
smallMolecule_1.attributes()

# Instance number two
#####################
smallMolecule_2 = smallMolecules()
smallMolecule_2.name = 'acetaminophen'
smallMolecule_2.MW = 151.06
smallMolecule_2.HBD = 2
smallMolecule_2.HBA = 2
smallMolecule_2.logP = 1.08

smallMolecule_2.lipinski()
smallMolecule_2.attributes()

# Instance number three
#######################
smallMolecule_3 = smallMolecules()
smallMolecule_3.name = 'nicotine'
smallMolecule_3.MW = 162.12
smallMolecule_3.HBD = 0
smallMolecule_3.HBA = 2
smallMolecule_3.logP = 1.49

smallMolecule_3.lipinski()
smallMolecule_3.attributes()


#Assignment - 6 - Classes


###--------------------> Test Example

#Simple Protein Example
#################################


class Protein:

	def __init__(self):
		self.primary = None
		self.secondary = None
		self.tertiary = None
		self.quaternary = None

	def printAttributes(self):

		if self.primary:
			print(self.primary, "-peptide chain")
		if self.secondary:
			print(self.secondary, "-alpha helix & beta sheet")
		if self.tertiary:
			print(self.tertiary, "-beta barrel")
		if self.quaternary:
			print(self.quaternary, "-multimeric")

FakeProtein = Protein()
FakeProtein.primary = "protein x"
FakeProtein.secondary = "protein x"
FakeProtein.tertiary = "protein x"
FakeProtein.quaternary = "protein x"
FakeProtein.printAttributes()

print("\n")


###-------------------------> Actual Assignment


class GPCRs:

	def __init__(self):
		self.receptorName = None
		self.GprotienClass = None
		self.Ligand = None
		self.TranscriptionalResult = None
		self.DiseaseInvolvedIn = None

	def printAttributes(self):
		if self.receptorName:
			print("Receptor Name Is:", self.receptorName)
		if self.GprotienClass:
			print("G-protein Class Is:", self.GprotienClass)
		if self.Ligand:
			print("Endogenous Ligand Is:", self.Ligand)
		if self.TranscriptionalResult:
			print("Transcriptional Result Is:", self.TranscriptionalResult)
		if self.DiseaseInvolvedIn:
			print("Involved In:", self.DiseaseInvolvedIn)


DopamineReceptor = GPCRs()
DopamineReceptor.receptorName = "DRD1"
DopamineReceptor.GprotienClass = "Class A"
DopamineReceptor.Ligand = "Dopamine"
DopamineReceptor.TranscriptionalResult = "c-fos production"
DopamineReceptor.DiseaseInvolvedIn = "ADHD, Schizophrenia, Hypertension"
DopamineReceptor.printAttributes()

print("\n")

CalcitoninReceptor = GPCRs()
CalcitoninReceptor.receptorName = "CALCR"
CalcitoninReceptor.GprotienClass = "Class B"
CalcitoninReceptor.Ligand = "Amylin & Calcitonin"
CalcitoninReceptor.TranscriptionalResult = "Activates Caclcium Homeostasis Genes"
CalcitoninReceptor.DiseaseInvolvedIn = "Metabolic Bone Disease"
CalcitoninReceptor.printAttributes()

print("\n")

OpiodReceptor = GPCRs()
OpiodReceptor.receptorName = "OPRD1"
OpiodReceptor.GprotienClass = "Class A"
OpiodReceptor.Ligand = "Dynorphin, Endomorphin, & Endorphin"
OpiodReceptor.TranscriptionalResult = "Disruption of Gene Expression By Inhibition of Arrestin, Dynamin, and GRK"
OpiodReceptor.DiseaseInvolvedIn = "Brain & Respitory Disorders"
OpiodReceptor.printAttributes()

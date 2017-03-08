# Use this code to see if the protein sequence of interest differs from the canonical Human NOS1 protein
# Can be used to compare different isoforms of the protein within humans or in different species


#Parse the file of interest into a single string for analysis 
fileInput = open("Human Brain NOS1 Protein.fasta", "r")#Define fileInput with whatever file you want to analyze 
Protein = []
for line in fileInput:
	Protein.append(line.strip('\n'))
Protein.pop(0)
ProteinSequence = "".join(Protein)
print(ProteinSequence)

 
#Define domains of interest- can be modified to look for other domains/sequences of interest 
PDZ = "SVRLFKRKVGGLGFLVKERVSKPPVIISDLIRGGAAEQSGLIQAGDIILAVNGRPLVDLSYDSALEVLRGIASETHVVLILRG"
FL = "ATILYATETGKSQAYAKTLCEIFKHAFDAKVMSMEEYDIVHLEHETLVLVVTSTFGNGDPPENGEKFGCALMEMRHPNSVQEERKSYKVRFNSVSSYSDSQKSSGDGPDLRDNFESAGPLANVRFSVFGLGSRAYPHFCAFGHAVDTLLEELGGERILKMREGDELCGQEEAFRTWAKKVF"     
FAD = "KRVSAARLLSRQNLQSPKSSRSTIFVRLHTNGSQELQYQPGDHLGVFPGNHEDLVNALIERLEDAPPVNQMVKVELLEERNTALGVISNWTDELRLPPCTIFQAFKYYLDITTPPTPLQLQQFASLATSEKEKQRLLVLSKGLQEYEEWKWGKNPTIVEVLEEFPSIQMPATLLLTQLSLLQPRYYSISSSPDMYPDEVHLTVAIVSYRTRDGEGPIHHGVCSSWLNRIQADELVPCFVRGAPSFHLP"
Calmodulin = "KRRAIGFKKLAEAVKFSAKLM"

print("\n")

#Search for protein domains within sequence and obtain their position in the sequence
if PDZ in ProteinSequence:
	print("PDZ domain present at location", ProteinSequence.find(PDZ))
else:
	print("PDZ domain not present.")
if FL in ProteinSequence:
	print("Flavodoxin-like domain present at location", ProteinSequence.find(FL))
else: 
	print("Flavodoxin-like domain not present.")
if FAD in ProteinSequence:
	print("FAD-binding domain present at location", ProteinSequence.find(FAD))
else:
	print("FAD-binding domain not present.")
if Calmodulin in ProteinSequence:
	print("Calmodulin Binding domain present at location", ProteinSequence.find(Calmodulin))
else:
	print("Calmodulin Binding domain not present.")


print("\n")


#Create a class to organize NOS1 protein variants and their properties 
class NOS:

	def __init__(self):
		self.proteinID = None
		self.PDZ = None
		self.FL = None
		self.FAD = None
		self.Calmodulin = None

	def printAttributes(self):
		if self.proteinID:
			print("The protein isoform is:", self.proteinID)
		if self.PDZ:
			print("Does protein have PDZ domain?", self.PDZ)
		if self.FL:
			print("Does protein have Flavodoxin-like domain?", self.FL)
		if self.FAD:
			print("Does protein have FAD-binding domain?", self.FAD)
		if self.Calmodulin:
			print("Does protein have Calmodulin binding domain?", self.Calmodulin)


#Create an instance for Human Brain NOS1 protein
HumanBrainNOS1 = NOS()
HumanBrainNOS1.proteinID = "Human Brain NOS1"
HumanBrainNOS1.PDZ = "Yes"
HumanBrainNOS1.FL = "Yes"
HumanBrainNOS1.FAD = "Yes"
HumanBrainNOS1.Calmodulin = "Yes"
HumanBrainNOS1.printAttributes()
print("\n")

#Create an instance for Human Brain NOS1 isoform 2
HumanIso2 = NOS()
HumanIso2.proteinID = "Human Brain NOS1 Isoform 2"
HumanIso2.PDZ = "Yes"
HumanIso2.FL = "Yes"
HumanIso2.FAD = "Yes"
HumanIso2.Calmodulin = "Yes"
HumanIso2.printAttributes()
print("\n")

#Create an instance for Human Brain NOS1 isoform 3
HumanIso3 = NOS()
HumanIso3.proteinID = "Human Brain NOS1 Isoform 3"
HumanIso3.PDZ = "No"
HumanIso3.FL = "Yes"
HumanIso3.FAD = "Yes"
HumanIso3.Calmodulin = "Yes"
HumanIso3.printAttributes()
print("\n")

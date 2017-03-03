fileinput = open("CexE.fasta", "r")

antiP2_dna = []

for line in fileinput:
	antiP2_dna.append(line.strip('\n'))
	
antiP2_dna.pop(0)

newAntiP2 = "".join(antiP2_dna)

print(newAntiP2)

############################################
print("\n")
############################################


fileinput = open("uniprot-CexE-ZPR.fasta", "r")

antiP2_protein = []

for line in fileinput:
	antiP2_protein.append(line.strip('\n'))
	
antiP2_protein.pop(0)

newAntiP2protein = "".join(antiP2_protein)

print(newAntiP2protein)
############################################
print("\n")
############################################
fileinput = open("uniprot-Dispersin.fasta", "r")

DispersinProtein = []

for line in fileinput:
	DispersinProtein.append(line.strip('\n'))
	
DispersinProtein.pop(0)

Dispersin = "".join(DispersinProtein)

print(Dispersin)

print("\n")

DispersinSignalProtein = "MKKIKFVIFSGILGISLNAFA"

print("The index of the signal protein in the EAEC E. coli gene, Dispersin, begins at position:", Dispersin.find(DispersinSignalProtein))

DispersinEffectorProtein = "GGSGWNADNVDPSQCIKLSGVQYTYNSGVPVCMQGLNEGKVRGVSVSGVFYYKDGTTSNFKGVVTPSTPVNTNQDINKTNKVGVQKYSALTEWVK"

print("The index of the effecotr protein in the EAEC E. coli gene Dispersin, begins at position:", Dispersin.find(DispersinEffectorProtein))





############################################
print("\n")
############################################
cexE_SignalProtein = "MKKYILGVILAMGSLSAIA"

print("\n")

print("The index of the signal protein in the ETEC E. coli gene, CexE, begins at position:", newAntiP2protein.find(cexE_SignalProtein))

cexE_EffectorProtein = "GGGNSERPPSVAAGECVTFNSKLGEIGGYSWKYSNDACNETVAKGYAIGVAMHRTVNYEGGYSIQSSGIVKPGSDFIMKGGKTYKGHKKVSAGGDTPYWYK"

print("\n")



print("The index of the effector protein in the ETEC E. coli gene, CexE, begins at position:", newAntiP2protein.find(cexE_EffectorProtein))


print("\n")
##########################


cexE_signalPeptidedna = "ATGAAAAAATATATATTAGGTGTTATTCTGGCTATGGGGTCTCTCTCCGCGATAGCT"

print("\n")

print("The index of the signal peptide in the ETEC E. coli gene, CexE, begins at position:", newAntiP2.find(cexE_signalPeptidedna))

print("\n")

effectorProtein = "GGAGGCGGTAATTCTGAACGACCGCCTTCCGTTGCAGCAGGGGAGTGTGTTACGTTCAACTCGAAATTAGGCGAGATTGGCGGATATAGCTGGAAATATTCTAATGACGCGTGTAATGAGACAGTTGCTAAAGGATATGCCATCGGTGTAGCCATGCATCGGACTGTAAATTATGAGGGGGGGTATTCCATACAATCAAGTGGAATTGTTAAACCAGGCTCTGATTTTATCATGAAGGGTGGAAAAACCTATAAAGGGCATAAAAAAGTATCTGCAGGTGGTGACACCCCTTATTGGTATAAATAA"

print("The index of the effector peptide in the ETEC strain of E. coli H10407, CexE, begins at position:", newAntiP2.find(effectorProtein))

# Parsed nucleotide sequence for positional info on E. coli, CexE gene.
#######################################################################
print("\n")
#######################################################################
fileinput = open("dispersin.fasta", "r")

disperinDna = []

for line in fileinput:
	disperinDna.append(line.strip('\n'))
	
disperinDna.pop(0)

new_disperinDna = "".join(disperinDna)

print(new_disperinDna)

dispersinSignalPeptide = "ATGAAAAAAATTAAGTTTGTTATCTTTTCTGGCATCTTGGGTATCAGCCTGAATGCCTTTGCG"

print("\n")

print("The index of the signal peptide in EAEC strain of E. coli, 042, CexE homolog, begins at position:", new_disperinDna.find(dispersinSignalPeptide))

effectorProtein2 = "GTTGGAACGCAGATAATGTGGACCCGTCCCAATGTATAAAACTGTCTGGAGTACAGTATACTTATAACAGCGGTGTCCCAGTATGTATGCAAGGCCTTAATGAAGGGAAAGTAAGGGGGGTGTCTGTCTCCGGGGTATTTTATTATAAGGACGGCACAACAAGCAACTTCAAAGGGGTTGTTACCCCCTCCACACCTGTAAATACGAACCAAGACATTAACAAGACAAATAAGGTTGGAGTCCAAAAATATAGTGCTCTAACCGAATGGGTTAAATAA"

print("\n")

print("The index of the effector peptide in the EAEC strain of E. coli, 042, CexE homolog, begins at position:", new_disperinDna.find(effectorProtein2))

#######################################################################
print("\n")
print("\n")
print("\n")
print("\n")
#######################################################################
#######################################################################
#######################################################################
# Building a class for the bacteria I'm working with in the lab I will 
# be building database with both more info and species and/or 
# strains as I continue through the lab.
#######################################################################
print("A Database For The Bacteria In The Munson Lab.")
print("\n")
#######################################################################
#######################################################################

class Bacteria_in_Munson_Lab:
	
	def __init__(self):
		
		self.genus = None
		self.species = None
		self.strain = None
		self.anti_P2_effector = None
		self.anti_P2_DNAsignalpeptide = None
		self.anti_P2_DNAeffector = None
		self.anti_P2_AA_signalPeptide = None
		self.anti_P2_AA_effectorPeptide = None
		self.cellularLocation = None
		self.freezerLocation = None
		
	def printAttributes(self):
		
		if self.genus:
			print("The genus is:", self.genus)
			print("The species is:", self.species)
			print("The strain is:", self.strain)
			print("Does this bacteria have an anti-P2-effector?", self.anti_P2_effector)
			print("The DNA sequence of the anti-P2 signal peptide is:", self.anti_P2_DNAsignalpeptide)
			print("The DNA sequence of the anti-P2 effector peptide is:", self.anti_P2_DNAeffector)
			print("The amino acid sequence of the anti-P2 signal peptide is:", self.anti_P2_AA_signalPeptide)
			print("The amino acid sequence of the anti-P2 effector peptide is:", self.anti_P2_AA_effectorPeptide)
			print("The cellular location of anti-P2 effector is:", self.cellularLocation)
			print("The location in the freezer for this bacteria is:", self.freezerLocation)
			
#######################################################################
bacteria = Bacteria_in_Munson_Lab()
bacteria.genus = "Escherichia"
bacteria.species = "coli"
bacteria.strain = "ETEC, H10407"
bacteria.anti_P2_effector = "TRUE"
bacteria.anti_P2_DNAsignalpeptide = cexE_signalPeptidedna, "The index it starts in the .fasta file is:", newAntiP2.find(cexE_signalPeptidedna)
bacteria.anti_P2_DNAeffector = effectorProtein, "The index it starts in the .fasta file is:", newAntiP2.find(effectorProtein)
bacteria.anti_P2_AA_signalPeptide = cexE_SignalProtein, "The index it starts in the .fasta file:", newAntiP2protein.find(cexE_SignalProtein) 
bacteria.anti_P2_AA_effectorPeptide = cexE_EffectorProtein, "The index it starts in the .fasta file:", newAntiP2protein.find(cexE_EffectorProtein)
bacteria.cellularLocation = "Periplasm"
bacteria.freezerLocation = "AG02"
bacteria.printAttributes()

#######################################################################
print("\n")
#######################################################################

######################################################################
bacteria = Bacteria_in_Munson_Lab()
bacteria.genus = "Escherichia"
bacteria.species = "coli"
bacteria.strain = "EAEC, 042"
bacteria.anti_P2_effector = "POTENTIALLY"
bacteria.anti_P2_DNAsignalpeptide = dispersinSignalPeptide, "The index it starts at in the .fasta file is:", new_disperinDna.find(dispersinSignalPeptide)
bacteria.anti_P2_DNAeffector = effectorProtein2, "The index it starts at in the .fasta file is:", new_disperinDna.find(effectorProtein2)
bacteria.anti_P2_AA_signalPeptide = DispersinSignalProtein, "The index it starts at in the .fasta file is:", Dispersin.find(DispersinSignalProtein)
bacteria.anti_P2_AA_effectorPeptide = DispersinEffectorProtein, "The index it starts at in the .fasta file is:", Dispersin.find(DispersinEffectorProtein)
bacteria.cellularLocation = "Outer membrane"
bacteria.freezerLocation = "BC05"
bacteria.printAttributes()


		
		


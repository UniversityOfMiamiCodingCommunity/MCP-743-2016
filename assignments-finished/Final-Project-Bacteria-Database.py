#######################################################
# The GenBank DNA for CexE, an anti-P2 effector protein
#######################################################
fileinput = open("CexE.fasta", "r")

cexE = []

for line in fileinput:
	cexE.append(line.strip('\n'))
	
cexE.pop(0)

cexE_DNA = "".join(cexE)

print("The .fasta file for CexE DNA:", cexE_DNA)


#######################################################
cexE_signalPeptideDNA = "ATGAAAAAATATATATTAGGTGTTATTCTGGCTATGGGGTCTCTCTCCGCGATAGCT" 
# Obtained the signal DNA sequence from GenBank

print("The index of the signal peptide in the ETEC E. coli gene, CexE, begins at position:", cexE_DNA.find(cexE_signalPeptideDNA)) 

cexE_effectorDNA = "GGAGGCGGTAATTCTGAACGACCGCCTTCCGTTGCAGCAGGGGAGTGTGTTACGTTCAACTCGAAATTAGGCGAGATTGGCGGATATAGCTGGAAATATTCTAATGACGCGTGTAATGAGACAGTTGCTAAAGGATATGCCATCGGTGTAGCCATGCATCGGACTGTAAATTATGAGGGGGGGTATTCCATACAATCAAGTGGAATTGTTAAACCAGGCTCTGATTTTATCATGAAGGGTGGAAAAACCTATAAAGGGCATAAAAAAGTATCTGCAGGTGGTGACACCCCTTATTGGTATAAATAA"
# Obtained the effector DNA sequence form GenBank

print("The index of the effector peptide in the ETEC strain of E. coli H10407, CexE, begins at position:", cexE_DNA.find(cexE_effectorDNA))

############################################
print("\n")
############################################

############################################
# The Uniprot Data for CexE
#############################################
fileinput = open("uniprot-CexE-ZPR.fasta", "r")

cexE_prot = []

for line in fileinput:
	cexE_prot.append(line.strip('\n'))
	
cexE_prot.pop(0)

cexE_protein = "".join(cexE_prot)

print("The .fasta file for CexE amino acid sequence:", cexE_protein)


#####################################################################
cexE_SignalProtein = "MKKYILGVILAMGSLSAIA"
# Obtained the CexE signal protein amino acid string from UniProt

print("The index of the signal protein in the ETEC E. coli gene, CexE, begins at position:", cexE_protein.find(cexE_SignalProtein))

cexE_EffectorProtein = "GGGNSERPPSVAAGECVTFNSKLGEIGGYSWKYSNDACNETVAKGYAIGVAMHRTVNYEGGYSIQSSGIVKPGSDFIMKGGKTYKGHKKVSAGGDTPYWYK"
# Obtained the CexE effector protein amino acid string from UniProt

print("The index of the effector protein in the ETEC E. coli gene, CexE, begins at position:", cexE_protein.find(cexE_EffectorProtein))


############################################
print("\n")
############################################



###################################################################
# Potentially a CexE homolog found in a different strain of E. coli
# The GenBank for the CexE potential homolog, named Dispersin
###################################################################
fileinput = open("dispersin.fasta", "r")

disperin_dna = []

for line in fileinput:
	disperin_dna.append(line.strip('\n'))
	
disperin_dna.pop(0)

Dispersin_DNA = "".join(disperin_dna)

print("The .fasta file for Dispersin DNA:", Dispersin_DNA)
########################################################################

dispersinSignalDNA = "ATGAAAAAAATTAAGTTTGTTATCTTTTCTGGCATCTTGGGTATCAGCCTGAATGCCTTTGCG"
# Obtained the Dispersin signal DNA sequence from GenBank

print("The index of the signal peptide in EAEC strain of E. coli, 042, CexE homolog, begins at position:", Dispersin_DNA.find(dispersinSignalDNA))

dispersinEffectorDNA = "GTTGGAACGCAGATAATGTGGACCCGTCCCAATGTATAAAACTGTCTGGAGTACAGTATACTTATAACAGCGGTGTCCCAGTATGTATGCAAGGCCTTAATGAAGGGAAAGTAAGGGGGGTGTCTGTCTCCGGGGTATTTTATTATAAGGACGGCACAACAAGCAACTTCAAAGGGGTTGTTACCCCCTCCACACCTGTAAATACGAACCAAGACATTAACAAGACAAATAAGGTTGGAGTCCAAAAATATAGTGCTCTAACCGAATGGGTTAAATAA"
# Obtained the Dispersin signal DNA sequence from GenBank

print("The index of the effector peptide in the EAEC strain of E. coli, 042, CexE homolog, begins at position:", Dispersin_DNA.find(dispersinEffectorDNA))


############################################
print("\n")
############################################

############################################
# The Uniprot data for Dispersin
############################################
fileinput = open("uniprot-Dispersin.fasta", "r")

dispersin_prot = []

for line in fileinput:
	dispersin_prot.append(line.strip('\n'))
	
dispersin_prot.pop(0)

Dispersin_Protein = "".join(dispersin_prot)

print("The .fasta file for the Dispersin amino acid sequence:", Dispersin_Protein)
########################################################################

DispersinSignalProtein = "MKKIKFVIFSGILGISLNAFA"
# Obtained the Dispersin signal amino acid sequence from UniProt
 
print("The index of the signal protein in the EAEC E. coli gene, Dispersin, begins at position:", Dispersin_Protein.find(DispersinSignalProtein))

DispersinEffectorProtein = "GGSGWNADNVDPSQCIKLSGVQYTYNSGVPVCMQGLNEGKVRGVSVSGVFYYKDGTTSNFKGVVTPSTPVNTNQDINKTNKVGVQKYSALTEWVK"
# Obtained the Dispersin effector amino acid sequence from UniProt

print("The index of the effector protein in the EAEC E. coli gene Dispersin, begins at position:", Dispersin_Protein.find(DispersinEffectorProtein))

#######################################################################
#######################################################################
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
		self.anti_P2_DNAsignalpeptide_Index = None
		self.anti_P2_DNAeffector = None
		self.anti_P2_DNAeffector_Index = None
		self.anti_P2_AA_signalPeptide = None
		self.anti_P2_AA_signalPeptide_Index = None
		self.anti_P2_AA_effectorPeptide = None
		self.anti_P2_AA_effectorPeptide_Index = None
		self.cellularLocation = None
		self.freezerLocation = None
		
	def printAttributes(self):
		
		if self.genus:
			print("The genus is:", self.genus)
			print("The species is:", self.species)
			print("The strain is:", self.strain)
			print("Does this bacteria have an anti-P2-effector?", self.anti_P2_effector)
			print("The DNA sequence of the anti-P2 signal peptide is:", self.anti_P2_DNAsignalpeptide)
			print("The index where the signal sequence of the DNA begins at:", self.anti_P2_DNAsignalpeptide_Index)
			print("The DNA sequence of the anti-P2 effector peptide is:", self.anti_P2_DNAeffector)
			print("The index where the effector sequence of the DNA begins at:", self.anti_P2_DNAeffector_Index)
			print("The amino acid sequence of the anti-P2 signal peptide is:", self.anti_P2_AA_signalPeptide)
			print("The index where the signal sequence of the amino acids begins is at:", self.anti_P2_AA_signalPeptide_Index)
			print("The amino acid sequence of the anti-P2 effector peptide is:", self.anti_P2_AA_effectorPeptide)
			print("The index where the effector sequence of the amino acids begins is at:", self.anti_P2_AA_effectorPeptide_Index)
			print("The cellular location of anti-P2 effector is:", self.cellularLocation)
			print("The location in the freezer for this bacteria is:", self.freezerLocation)
			
#######################################################################
bacteria = Bacteria_in_Munson_Lab()
bacteria.genus = "Escherichia"
bacteria.species = "coli"
bacteria.strain = "ETEC, H10407"
bacteria.anti_P2_effector = "TRUE"
bacteria.anti_P2_DNAsignalpeptide = cexE_signalPeptideDNA
bacteria.anti_P2_DNAsignalpeptide_Index = cexE_DNA.find(cexE_signalPeptideDNA)
bacteria.anti_P2_DNAeffector = cexE_effectorDNA  
bacteria.anti_P2_DNAeffector_Index = cexE_DNA.find(cexE_effectorDNA)
bacteria.anti_P2_AA_signalPeptide = cexE_SignalProtein
bacteria.anti_P2_AA_signalPeptide_Index = cexE_protein.find(cexE_SignalProtein)
bacteria.anti_P2_AA_effectorPeptide = cexE_EffectorProtein 
bacteria.anti_P2_AA_effectorPeptide_Index = cexE_protein.find(cexE_EffectorProtein)
bacteria.cellularLocation = "Periplasm"
bacteria.freezerLocation = "AG02"
bacteria.printAttributes()

#######################################################################
print("\n")
#######################################################################

######################################################################s 
bacteria = Bacteria_in_Munson_Lab()
bacteria.genus = "Escherichia"
bacteria.species = "coli"
bacteria.strain = "EAEC, 042"
bacteria.anti_P2_effector = "UNKNOWN"
bacteria.anti_P2_DNAsignalpeptide = dispersinSignalDNA
bacteria.anti_P2_DNAsignalpeptide_Index = Dispersin_DNA.find(dispersinSignalDNA)
bacteria.anti_P2_DNAeffector = dispersinEffectorDNA 
bacteria.anti_P2_DNAeffector_Index = Dispersin_DNA.find(dispersinEffectorDNA)
bacteria.anti_P2_AA_signalPeptide = DispersinSignalProtein 
bacteria.anti_P2_AA_signalPeptide_Index = Dispersin_Protein.find(DispersinSignalProtein)
bacteria.anti_P2_AA_effectorPeptide = DispersinEffectorProtein
bacteria.anti_P2_AA_effectorPeptide_Index = Dispersin_Protein.find(DispersinEffectorProtein)
bacteria.cellularLocation = "Outer membrane"
bacteria.freezerLocation = "BC05"
bacteria.printAttributes()


		
		


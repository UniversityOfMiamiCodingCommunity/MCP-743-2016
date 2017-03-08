#CD36


#Parsing Large Scale Gene Sets (9,404 genes)
fileInput = open("/Users/SamuelDelOlio/GitHub/MCP-743/assignments-finished/uniprot-CD36.txt", "r")
for line in fileInput:
	result = line.split("\t")
	print(" Uniprot Entry Number:", result[0], "\n",
		"Entry Name/Gene:", result[1], "\n",
		"Status:", result[2], "\n",
		"Protein Names:", result[3], "\n",
		"Gene Name(s):", result[4], "\n",
		"Organism:", result[5], "\n", 
		"Amino Acid Length:", result[6], "\n",
		"Peptide Sequence:", result[7])
fileInput.close()


#Searching all 9,404 genes for a Thrombospondin binding sequence motif (CSVTCG)
fileInput = open("/Users/SamuelDelOlio/GitHub/MCP-743/assignments-finished/uniprot-CD36.txt", "r")
for line in fileInput:
	CSVTCGcount = line.count("CSVTCG")
	splitLine = line.split("\t")
	if CSVTCGcount:
		print("There are", CSVTCGcount, "CSVTCG motifs in Uniprot Entry Number:", splitLine[0], "\n",
		"\t", "Entry Name/Gene:", splitLine[1], "\n",
		"\t", "Protein Name:", splitLine[3], "\n",
		"\t", "Gene Name(s):", splitLine[4], "\n",
		"\t", "Organism:", splitLine[5], "\n")
fileInput.close()

#Make a Class For Any Uniprot Amino Acid/Protein File in This Format
class uniprotGenes:

	def __init__(self):
		self.UniprotEntryNumber = None
		self.EntryNameGene = None
		self.Status = None
		self.ProteinNames = None
		self.GeneNames = None
		self.Organism = None
		self.AminoAcidLength = None
		self.PeptideSequence = None
		self.hasSequence = 0

	def printAttributes(self):
		if self.UniprotEntryNumber:
			print("Uniprot Entry Number is:", self.UniprotEntryNumber)
		if self.EntryNameGene:
			print("Entry Name/Gene is:", self.EntryNameGene)
		if self.Status:
			print("Status is:", self.Status)
		if self.ProteinNames:
			print("Protein Names are:", self.ProteinNames)
		if self.GeneNames:
			print("Gene Names are:", self.GeneNames)
		if self.Organism:
			print("The Organism is:", self.Organism)
		if self.AminoAcidLength:
			print("The number of Amino Acids is:", self.AminoAcidLength)
		if self.PeptideSequence:
			print("The Primary Peptide Sequence is:", self.PeptideSequence)

	def findSequence(self, querySequence):
		if self.PeptideSequence.find(querySequence) != -1:
			self.hasSequence = 1


# Loop over the lines in the file.
##################################
fileInput = open("/Users/SamuelDelOlio/GitHub/MCP-743/assignments-finished/uniprot-CD36.txt", "r")
i = 0
listOfInstances = []
for line in fileInput:
	if i:
		# Create a uniprotGenes instance for each file line that is an entry.
		result = line.split("\t")
		uniprotFile = uniprotGenes()
		uniprotFile.UniprotEntryNumber = result[0]
		uniprotFile.EntryNameGene = result[1]
		uniprotFile.Status = result[2]
		uniprotFile.ProteinNames = result[3]
		uniprotFile.GeneNames = result[4]
		uniprotFile.Organism = result[5]
		uniprotFile.AminoAcidLength = result[6]
		uniprotFile.PeptideSequence = result[7]
		listOfInstances.append(uniprotFile)
		# uniprotFile.printAttributes()
	else:
		i += 1

# Set the class instances that have this sequence.
querySequence = "CSVTCG"
for x in listOfInstances:
	x.findSequence(querySequence)

# Show me the subset of class instances that contain the sequence.
hits, misses = 0, 0 
for x in listOfInstances:
	if x.hasSequence:
		hits += 1
		x.printAttributes()
	else:
		misses += 1

print("The above", hits, "genes contain the motif,", "\n", "and", misses, "genes do not.")


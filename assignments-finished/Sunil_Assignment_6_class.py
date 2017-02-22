class Eukaryota:

	def __init__(self):

		self.Phylum = None
		self.Class = None
		self.Order = None
		self.Family = None

	def printAttributes(self):

		if self.Phylum:
			print("Phylum of the Eukaryote:", self.Phylum)
		if self.Class:
			print("Class of the Eukaryote:", self.Class)
		if self.Order:
			print("order of the Eukaryote:", self.Order)
		if self.Family:
			print("Family of the Eukaryote:", self.Family)

# Create an instance of an Eukaryota class.
##################################################
lion = Eukaryota()
lion.Phylum = "Chordata"
lion.Class = "Mammalia"
lion.Order = "Carnivora"
lion.Family = "Felidae"
lion.printAttributes()
########################################################
print("\n\n")
#######################################################
# Create an instance of an Eukaryota class for another organism in the domain: Eukaryota
#######################################################
paramecium = Eukaryota()
paramecium.Phylum = "Ciliophora"
paramecium.Class = "Oligohymenophorea"
paramecium.Order = "Peniculida"
paramecium.Family = "Parameciidae"
paramecium.printAttributes()
########################################################
print("\n\n")
#######################################################
# Create an instance of an Eukaryota class for another organism in the domain: Eukaryota
#######################################################
human = Eukaryota()
human.Phylum = "Chordata"
human.Class = "Mammalia"
human.Order = "Primates"
human.Family = "Hominidae"
human.printAttributes()
#Class Heptocyte Cell Lines

class Cells:

	def __init__(self):
		self.Line = None
		self.name = None
		self.mythology = None
		self.color = None
		self.function = None
	def printAttributes(self):

		if self.position:
			print(self.position, "planet from Sun")
		if self.name:
			print("Name of planet: ", self.name)
		if self.mythology:
			print("God/Goddess of Planet: ", self.mythology)
		if self.color:
			print("Color of Planet: ", self.color)
		if self.function:
			print("Force is: ", self.function)
			
#~ SolarSystem = Planets()
# Populate the attributes of the class 
#~ SolarSystem.position = "2nd"
#~ SolarSystem.name = "Venus"
#~ SolarSystem.mythology = "Vesper, Lucifer, and Aphrodite- Star, Light, and Beauty"
#~ SolarSystem.color = "Yellow-Orange"
#~ SolarSystem.function = Venus
#~ SolarSystem.printAttributes()


#~ OtherPlanet = Planets()
#~ OtherPlanet.position = "8th"
#~ OtherPlanet.name = "Neptune"
#~ OtherPlanet.mythology = "Poseidon of the Sea"
#~ OtherPlanet.color = "Blue"
#~ OtherPlanet.function = Neptune
#~ OtherPlanet.printAttributes()

#~ LastPlanet = Planets()
#~ LastPlanet.position = "5th"
#~ LastPlanet.name = "Mars"
#~ LastPlanet.mythology = "Ares of War"
#~ LastPlanet.color = "Red"
#~ LastPlanet.function = Mars
#~ LastPlanet.printAttributes()


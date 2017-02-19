#Class

m1 = 100 * (10**10)
m2 = 1.989 * ( 10**30)
M = m1 * m2
r = (108.0 * (10 **9)) **2
G = 6.674 * (10 ** -11)
F = G * (M/r)
print( "Force: ", F, "Newtons")


def F (M, r, G): 
	F = G * (M/r) 
	print("Force result from function", F, "Newtons") 
	return F 

#Mass and distances from sun can change with each one :/
#~ PlanetMassdict = { }
#~ PlanetMassdict [1] = 9.68 * (10**54) #Venus
#~ PlanetMassdict [2] = 2.04 * (10**56) #Neptune
#~ PlanetMassdict [3] = 1.27 8 (10**54) #Mars

#~ PlanetDistancedict = { }
#~ PlanetDistancedict [1] =
#~ PlanetDistancedict [2] =
#~ PlanetDistancedict [3] =


class Planets:

	def __init__(self):
		self.position = None
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
			
SolarSystem = Planets()
#~ # Populate the attributes of the class 
SolarSystem.position = "2nd"
SolarSystem.name = "Venus"
SolarSystem.mythology = "Vesper Lucifer, and Aphrodite- Star, Light, and Beauty"
SolarSystem.color = "Yellow-Orange"
SolarSystem.function = F
SolarSystem.printAttributes()


OtherPlanet = Planets()
OtherPlanet.position = "8th"
OtherPlanet.name = "Neptune"
OtherPlanet.mythology = "Poseidon of the Sea"
OtherPlanet.color = "Blue"
OtherPlanet.function = F
OtherPlanet.printAttributes()

LastPlanet = Planets()
LastPlanet.position = "5th"
LastPlanet.name = "Mars"
LastPlanet.mythology = "Ares of War"
LastPlanet.color = "Red"
LastPlanet.function = F
LastPlanet.printAttributes()

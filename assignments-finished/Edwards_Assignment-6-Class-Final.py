#Class Assignment

# use: F = m * a instead, much easier lol
#~ m = [(9.68 * (10**54)), (2.04 * (10**56)), (1.27 * (10**54))]
a = 9.80665 #m/s**2
#~ F = m * a
#~ print( "Force: ", F, "Newtons")


M1 = 9.68 * (10**54) #Venus
M2 = 2.04 * (10**56) #Neptune
M3 = 1.27 * (10**54) #Mars



def VForce(M1, a):
	F = M1 * a
	print("VForce is ", F, "Newtons")
	return F
Venus = VForce(M1, a)
print(Venus)


def NForce(M2, a):
	F = M2 * a
	print("NForce is ", F, "Newtons")
	return F
Neptune = NForce(M2, a)
print(Neptune)

def MForce(M3, a):
	F = M3 * a
	print("MForce is ", F, "Newtons")
	return F
Mars = MForce(M3, a)
print(Mars)


#~ def Force(M, a): 
	#~ F = m * a
	#~ print("Force result from function", F, "Newtons") 
	#~ return F 
#~ Try1 = Force(M, r, G)
#~ print(Try1)
#~ m1 = 200 * (10**10)
#~ try2 = Force(M, r, G)
#~ print(try2)
#~ raise SystemExit

#Mass is different with each one :/
#~ PlanetMassdict = { }
#~ PlanetMassdict [1] = 9.68 * (10**54) #Venus
#~ PlanetMassdict [2] = 2.04 * (10**56) #Neptune
#~ PlanetMassdict [3] = 1.27 * (10**54) #Mars

#doesn't always have to = NONE for inititation 

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
SolarSystem.mythology = "Vesper, Lucifer, and Aphrodite- Star, Light, and Beauty"
SolarSystem.color = "Yellow-Orange"
SolarSystem.function = Venus
SolarSystem.printAttributes()


OtherPlanet = Planets()
OtherPlanet.position = "8th"
OtherPlanet.name = "Neptune"
OtherPlanet.mythology = "Poseidon of the Sea"
OtherPlanet.color = "Blue"
OtherPlanet.function = Neptune
OtherPlanet.printAttributes()

LastPlanet = Planets()
LastPlanet.position = "5th"
LastPlanet.name = "Mars"
LastPlanet.mythology = "Ares of War"
LastPlanet.color = "Red"
LastPlanet.function = Mars
LastPlanet.printAttributes()

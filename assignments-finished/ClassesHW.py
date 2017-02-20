# A class for muscle fiber types
########################################
class Muscle:

	def __init__(self):
		self.contractionVelocity = None
		self.biochemistry = None
		self.forceProduction = None
		self.fatigueResistance = None

	def printAttributes(self):
		if self.contractionVelocity:
			print("Contraction Velocity:", self.contractionVelocity)
		if self.biochemistry:
			print("Biochemical Property:", self.biochemistry)
		if self.forceProduction:
			print("Force Production:", self.forceProduction)
		if self.fatigueResistance:
			print("Fatigue Resistance", self.fatigueResistance)

#Create an instance for Type 1 muscle fibers
Type1 = Muscle()
Type1.contractionVelocity = "Slow"
Type1.biochemistry = "Oxidative"
Type1.forceProduction = "Low"
Type1.fatigueResistance = "High"
Type1.printAttributes()
print("\n")

#Create an instance for Type 2A muscle fibers
Type2A = Muscle()
Type2A.contractionVelocity = "Fast"
Type2A.biochemistry = "Oxidative Glycolytic"
Type2A.forceProduction = "High"
Type2A.fatigueResistance = "Intermediate"
Type2A.printAttributes()
print("\n")

#Create an instance for Type 2B muscle fibers
Type2B = Muscle()
Type2B.contractionVelocity = "Fast"
Type2B.biochemistry = "Glycolytic"
Type2B.forceProduction = "Very High"
Type2B.fatigueResistance = "Low"
Type2B.printAttributes()

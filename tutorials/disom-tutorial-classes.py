# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

# Classes (also known as objects)
# If you need help or need to explore something new regarding classes start here: https://docs.python.org/3/tutorial/classes.html
##################################################################################################################################


# This is how you make a class for cars.
##################################################################################################################################
class Car:

	# Class variables.
	# Note: class variables are shared by all instances.
	#####################################################
	usMpgGoal2050 = 50.0 # default us MPG goal by 2050.

	def __init__(self):

		# Instance variables.
		# Note: instance variables are unique to each instance.
		#######################################################
		self.year = None
		self.make = None
		self.model = None
		self.color = None
		self.gasMileage = 20.0 # default miles per gallon
		self.tankVolume = 10.0 # default tank volume in gallons
		self.fractionOfFuelRemaining = 1.0 # default to full tank 

	# A class method, i.e. a function, that takes class attributes as arguments.
	# Key vocabulary term: class method or class function.
	############################################################################
	def printAttributes(self):

		if self.year:
			print("Year built:", self.year)
		if self.make:
			print("Make of car:", self.make)
		if self.model:
			print("Model of car:", self.model)
		if self.color:
			print("Color of car", self.color)

	def distanceOnFullTank(self):

		return self.gasMileage*self.tankVolume

	def distanceOnCurrentTank(self, fractionOfTankRemaining):

		self.fractionOfFuelRemaining = fractionOfTankRemaining
		return self.gasMileage*self.tankVolume*self.fractionOfFuelRemaining

	def calculateFractionUsGoal(self):

		# Note: Uses the class variable self.usMpgGoal2050, 
		# and the instance method self.distanceOnFullTank().
		####################################################
		return self.distanceOnFullTank()/self.usMpgGoal2050


# This is how you use the Cars class in your code. 
##################################################

# Create an instance (i.e. a copy) of a Car class.
##################################################
dansCar = Car()
# Populate the attributes of the class 
dansCar.year = 2002
dansCar.make = "Honda"
dansCar.model = "Civic"
dansCar.color = "Silver"
dansCar.gasMileage = 29.0
dansCar.tankVolume = 11.0
dansCar.printAttributes()
# Report fuel characteristics.
##############################
maxTravelDistance = dansCar.distanceOnFullTank()
fractionOfTankRemaining = dansCar.distanceOnCurrentTank(0.5)
fractionOfUsMpgGoal = dansCar.calculateFractionUsGoal()
print("Distance on full tank:", maxTravelDistance, "miles.")
print("Distance on current tank:", fractionOfTankRemaining, "miles.")
print("Fraction of US MPG 2050 goal:", fractionOfUsMpgGoal)


# Create an instance of a Car class for my other car...
#######################################################
dansOtherCar = Car()
dansOtherCar.year = 2017
dansOtherCar.make = "Lamborghini"
dansOtherCar.model = "Centenario"
dansOtherCar.color = "Black"
dansOtherCar.gasMileage = 10.0
dansOtherCar.tankVolume = 10.0
dansOtherCar.printAttributes()
<<<<<<< HEAD


# This is how you make a class for statistics.
##################################################################################################################################
# class Stats:

# 	def __init__(self, dataList):

		# Class attributes that describe the object.
		# Key vocabulary term: class attribute
		############################################
=======
# Report fuel characteristics.
##############################
maxTravelDistance = dansOtherCar.distanceOnFullTank()
fractionOfTankRemaining = dansOtherCar.distanceOnCurrentTank(0.5)
fractionOfUsMpgGoal = dansCar.calculateFractionUsGoal()
print("Distance on full tank:", maxTravelDistance, "miles.")
print("Distance on current tank:", fractionOfTankRemaining, "miles.")
print("Fraction of US MPG 2050 goal:", fractionOfUsMpgGoal)
>>>>>>> master


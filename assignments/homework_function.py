###############################
#Classes and Functions
###############################

#1 Create a function from equations

def Newtons_Second_Law(m,a):
	"""Newtons Second Law"""
	Force= m*a
	print ("the force of an object with mass %d kg and acceleration %d m/s^2 is %d." %(m, a, Force))

Newtons_Second_Law(6,20)

def heat_transfer(m, C, T):
	"""Used to calculate amount of heat (q) in a substance"""
	Q= m*C*T
	#m= mass of substance in kg
	#C= specific heat of substance
	#T= change in temperature in Kelvin (K)
	print ("The heat of this substance is:", Q)
	
heat_transfer(10,2,15)



#2 Create a class 

class Anemias():
	"""Classification of different anemias"""
	def __init__(self, size, retic_count):
		self.size= size
		self.retic_count= retic_count
	
	def type(self):
		"""is the anemia microcytic or macrocytic?"""
		if  self.size < 80:
			print ("this type of anemia is microcytic")
		elif self.size > 80:
			print ("This type of anemia is macrocytic")
		else:
			print ("this type if anemia is normocytic")
	def erythropoesis(self):
		"""is the anemia characterized by reduced/increased rbc production?"""
		if self.retic_count > 1.5:
			print ("This anemuia has increased erythropoesis")
		elif self.retic_count < 0.5:
			print ("This anemia has decreased erythropoesis")
		else:
			print ("This anemia appears to have normal eryhthropoesis")

patient1_anemia= Anemias(85, 1.0)

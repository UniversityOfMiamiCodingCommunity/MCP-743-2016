###############################
#Classes and Functions
###############################

#1 Create a function from equations

def Newtons_Second_Law(m,a):
	"""Newtons Second Law"""
	Force= m*a
	print ("the force of an object with mass %d kg and acceleration %d m/s^2 is %d Newtons." %(m, a, Force))

Newtons_Second_Law(6,20)

def heat_transfer(m, C, T):
	"""Used to calculate amount of heat (q) in a substance"""
	Q= m*C*T
	#m= mass of substance in kg
	#C= specific heat of substance
	#T= change in temperature in Kelvin (K)
	print ("The heat of this substance is:", Q, "joules")
	
heat_transfer(10,2,15)



#2 Create a class 

class Anemias():
	"""Classification of different anemias"""
	def __init__(self, MCV, retic_count):
		self.MCV= MCV
		self.retic_count= retic_count
	
	def type(self):
		"""is the anemia microcytic or macrocytic?"""
		if  self.MCV < 80:
			return ("This type of anemia is microcytic")
		elif self.MCV > 100:
			return ("This type of anemia is macrocytic")
		else:
			return ("This type if anemia is normocytic")


	def erythropoesis(self):
		"""is the anemia characterized by reduced/increased rbc production?"""
		if self.retic_count > 1.5:
			return ("This anemia has increased erythropoesis")
		elif self.retic_count < 0.5:
			return ("This anemia has decreased erythropoesis")
		else:
			return ("This anemia appears to have normal eryhthropoesis")

patient1_anemia= Anemias(85, 1.0)
patient2_anemia= Anemias(70, 2.0)
patient3_anemia= Anemias(100, 0.3)

print (patient1_anemia.type()) 
print (patient1_anemia.erythropoesis())
 
print (patient2_anemia.type()) 
print (patient2_anemia.erythropoesis())

print (patient3_anemia.type()) 
print (patient3_anemia.erythropoesis())



age = 22
if age >= 18:
	print("You can vote!") 

age = 17
if age >= 18:
	print ("You can vote")
else:
		print ("You cannot vote")
		
age = 22
if age < 4:
	Print("Free admission")
elif age < 18:
	print("Admission is $10")
else: 
	print("Admission is $20")
	
age = 67
if age < 4:
	price = 0
elif age < 18:
	price = 10
elif age > 65:
	price = 5
else: 
	price = 20
print("Your admission cost is $" + str(price) + ".")

toppings = ["pepperoni", "cheese", "sausage"]
if 'cheese' in toppings:
	print("Adding cheese")
if 'pepperoni' in toppings:
	print("Adding pepperoni")
if 'spinach' in toppings:
	print("adding Spinach")

toppings = ['pepperoni', 'cheese', 'sausage']
for toppings in toppings:
	if toppings == 'sausage':
		print("We are out of sausages riht now")
	else:
		print("Adding " + toppings + ".")
		
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings: 
	if requested_topping in available_toppings:       
		 print("Adding " + requested_topping + ".") 
	else:       
	 print("Sorry, we don't have " + requested_topping + ".")        
print("\nFinished making your pizza!")


	


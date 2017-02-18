alien_0 = { }
alien_0 ['color'] = 'green' 
alien_0 ['points'] = 5

print(alien_0)

alien_1 = {'color': 'red', 'points': 10}
print(alien_1['color'])
print(alien_1['points'])

alien_1 = {'color': 'red'} 
print("The alien is " + alien_0['color'] + ".")

alien_1['color'] = 'yellow' 
print("The alien is now " + alien_1['color'] + ".")



alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 

print("Original x-position: " + str(alien_2['x_position'])) 
if alien_2['speed'] == 'slow':
	x_increment = 1 
elif alien_2['speed'] == 'medium':
		x_increment = 2
else:
			x_increment = 3
print("New x_position: " + str(alien_2['x_position']))


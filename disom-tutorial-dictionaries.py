# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

# Dictionary
# If you need help or need to explore something new regarding dictionary start here:
# Dictionary Methods: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
########################################################################################

# An example dictionary.
########################
exampleDict = {}
exampleDict[1] = 1
exampleDict["1"] = 2
print("Dict #1", exampleDict)

# Example of accidental overwrite: the most common accidental error.
####################################################################
exampleDict[1.0] = 3
print("Dict #2", exampleDict)

# A list can't be a key.
########################
# exampleDict = {}
# exampleDict[1] = 1
# exampleDict["1"] = 2
# exampleDict[[1, 2, 3, 4]] = 3
# print("Dict #3", exampleDict)

# A tuple can be a key.
########################
exampleDict[(1, 2, 3, 4)] = 4
print("Dict #4", exampleDict)

# If you want to use a list as a dictionary key, convert it to a tuple you the built-in Python function tuple().
################################################################################################################
exampleList = [1, 2, 3, 4]
exampleTuple = tuple(exampleList)
exampleDict[exampleTuple] = 4
print("Dict #5", exampleDict)

# A dictionary can be a key. 
############################
# tryDictAsKey = {1:1, 2:2, 3:3, 4:4}
# exampleDict[tryDictAsKey] = 4
# print("Dict #6", exampleDict)

# The dictionary method keys() is arguable the most useful of dictionary methods. 
# It returns a list, in random order, of the dictionaries keys.  
#################################################################################
exampleDictKeys = exampleDict.keys()
print("Dict keys:", exampleDictKeys)

# The dictionary method values() is also very useful. 
# It returns a list, in random order, of the dictionaries values. 
#################################################################################
exampleDictValues = exampleDict.values()
print("Dict values:", exampleDictValues)

# The dictionary method update() also allows an alternative way to add keys and values to a dictionary.
#######################################################################################################
exampleDict.update({"MCP-743": 5})
exampleDictKeys = exampleDict.keys() # Reset the list of keys to reflect the addition of a new key, value pair.

# You access the values within a dictionary using its keys.
# Here is an example of the most common usage. 
###########################################################
for exampleDictKey in exampleDictKeys:
	print ("Dict value for key", exampleDictKey, "is", exampleDict[exampleDictKey])

# My example was a bit contrived because key values are usually the same type and/or form.
# Here is an example using are PDB file excerpt. 
# We will create a unique key for each atom in the PDB file, and then use this key to save each file line in a dictionary. 
##########################################################################################################################
fileInput = open("class3-pdbExcerptShort.pdb", "r")
atomDictionary = {}
for line in fileInput:

	# Make sure the file line corresponds to an atom.
	#################################################
	if line[0:4] == "ATOM":

		lineAsList = line.split() # Split the line, which is a string, by spaces using the string split() method with no arguments.

		# Using the file line in list format, populate select attributes of the atom.
		#############################################################################
		atomNumber = int(lineAsList[1])
		atomName = lineAsList[2]
		atomResidueName = lineAsList[3]
		atomChain = lineAsList[4]
		atomResidueNumber = int(lineAsList[5])

	# Make a unique key to store the atom file line in a dictionary.
	################################################################
	uniqueKey = (atomNumber, atomName, atomResidueName, atomChain, atomResidueNumber)
	atomDictionary[uniqueKey] = line

# Use the dictionary keys() method to get the keys of the dictionary as a list.
###############################################################################
dictKeys = atomDictionary.keys()
dictKeys.sort() # Sort the list of keys alpha-numerically using the keys sort() method.
for dictKey in dictKeys:
	print(dictKey)

# Use the sorted keys of the dictionary, print the file lines.
##############################################################
for dictKey in dictKeys:
	print("key: ", dictKey, "value: ", atomDictionary[dictKey])





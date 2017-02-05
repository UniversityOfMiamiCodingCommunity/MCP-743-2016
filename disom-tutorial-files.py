# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

# The vast majority of the time, you will open a file using the Python built-in function open().
# However, as your programming advances, you may need more advanced tools occassionally. 
# These advanced tools, i.e. modules, can be found here: https://docs.python.org/3/library/filesys.html
# We will only use a few these modules in class, so don't let them over complicate your assignments.  
########################################################################################################

# Open the file named, class3-pdbExcerptShort.pdb, which happens to be in the same directory as this Python script.
# The first argument to open() is the path to the file (this is why I had you learn how to navigate in the terminal: to help you learn how to write filepaths)
# In this case, the file is in the same directory as our script, so we can just use the file name. 
# The second argument is the file mode: "r" for read mode, or "w" for write, or "a" for append.
##############################################################################################################################################################
# fileInput = open("class3-pdbExcerptShort.pdb", "r")

# # You can loop over the lines in a file, the same as you would loop over a list.
# ################################################################################
# for line in fileInput:
# 	print(line)

# # Close the file.
# #################
# fileInput.close()

# If a file is in a directory different from that of your Python script (i.e. this script), you have to include the relative path to the file in open()
# For example, the class3-pdbExcerptLong.pdb file is in the sub-directory class3-pdbExcerptLong...
#######################################################################################################################################################
# fileInput = open("class3-pdbExcerptLong/class3-pdbExcerptLong.pdb", "r")
# for line in fileInput:
# 	print(line)
# fileInput.close()

# # This file path would work too.
# ################################
# fileInput = open("./class3-pdbExcerptLong/class3-pdbExcerptLong.pdb", "r") # "./" means "this directory", and "../" means "up one directory"
# for line in fileInput:
# 	print(line)
# fileInput.close()

# # File path separators are different on Macs and PCs. 
# # One was to deal with this is to import the Python variable sep, that corresponds to the proper file path separator on the current OS being used. 
# # If you use sep, than your file paths will work on all computer OSs (i.e. your code will be truly cross platform).
# # The sep variable can be imported from the os module, which is part of the standard Python library.
# # This is how it is done, reworking the sample code above:
# ##################################################################################################################################################
from os import sep # we have imported sep and can now use it as a key word
fileInput = open("." + sep + "class3-pdbExcerptLong" + sep + "class3-pdbExcerptLong.pdb", "r") # Note: the backslashes have been replaced by sep in a concatenated string. 
for line in fileInput:
	print("using sep", line)
fileInput.close()

# # Now that we know how to get access to file contents, let me show you how you get the informatoin you want.
# # Say I only wanted the file lines that corresponded to atoms. 
# ############################################################################################################
# from os import sep # you only need to import this once, but I will keep importing it so you don't get confused
# fileInput = open("." + sep + "class3-pdbExcerptLong" + sep + "class3-pdbExcerptLong.pdb", "r")
# for line in fileInput:
# 	if line[0:4] == "ATOM":
# 		print("Atom line:", line)
# fileInput.close()

<<<<<<< HEAD
# # Now let's do the same thing with if/else control flow statements
# ############################################################################################################
# from os import sep # you only need to import this once, but I will keep importing it so you don't get confused
# fileInput = open("." + sep + "class3-pdbExcerptLong" + sep + "class3-pdbExcerptLong.pdb", "r")
# for line in fileInput:

# 	if "ATOM" in line:
# 		print("Found an atom line:", line)
# 	elif "HEADER" in line:
# 		print("Found a header line:", line)
# 	elif "TITLE" in line:
# 		print("Found a title line:", line)
# 	elif "SOURCE" in line:
# 		print("Found a source line:", line)
# 	elif "AUTHOR" in line:
# 		print("This is who get's credit", line) # Note: if you want to use an apostrophe in a string, you have to use double quotes on the outside of the string.
# fileInput.close()

# ######################################
# #
# # NOW YOU ARE ALL SERIOUSLY DANGEROUS!
# #
# ######################################
=======
# Now let's do the same thing with if/else control flow statements
############################################################################################################
from os import sep # you only need to import this once, but I will keep importing it so you don't get confused
fileInput = open("." + sep + "class3-pdbExcerptLong" + sep + "class3-pdbExcerptLong.pdb", "r")
atomFileLines = ""
for line in fileInput:

	if line[0:4] == "ATOM":
		print("Found an atom line:", line)
		atomFileLines += line
	elif "HEADER" in line:
		print("Found a header line:", line)
	elif "TITLE" in line:
		print("Found a title line:", line)
	elif "SOURCE" in line:
		print("Found a source line:", line)
	elif "AUTHOR" in line:
		print("This is who get's credit", line) # Note: if you want to use an apostrophe in a string, you have to use double quotes on the outside of the string.
fileInput.close()

# Now write a new file that contains only the file lines corresponding to atoms.
# To accomplish this, you use the built-in Python write() function. 
# However, you first need to create a new file using the built-in Python open() function.
##################################################################################################################
fileOutput = open("." + sep + "class3-pdbExcerptLong" + sep + "class3-pdbExcerptLong-justAtoms.pdb", "w") # Note: instead of read "r" mode we should use write "w" mode
for line in atomFileLines:
	fileOutput.write(line)
fileOutput.close()
<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes




from os import sep

#################
# Open each file.
#################

fileInput_1 = open("../" + sep + "dataFiles" + sep + "targets_and_families.txt", "r")

fileInput_2 = open("../" + sep + "dataFiles" + sep + "Pharmacologically_active.txt", "r")

fileInput_3 = open("../" + sep + "dataFiles" + sep + "drugbank_vocabulary.txt", encoding = "utf8")
#######################################################################################
# Create a dictionary storing each receptor name as a key and the HGNC ID as its value.
# fileInput_1 contains all receptors in DrugBank and the family type.
#######################################################################################

gpcrHGNCids = {}

for line in fileInput_1:
	lineSplit_1 = line.split('\t')
	
	if lineSplit_1[0] == "gpcr":
		gpcrHGNCids[lineSplit_1[9]] = (lineSplit_1[11])


#~ print(gpcrHGNCids)
#~ raise SystemExit

#####################################################################################################
# Create a dictionary storing each HGNC ID as a key with the approved pharmaceutical(s) as its value.
# fileInput_2 contains all receptors that have an approved drug listed as a DrugBank ID.
#####################################################################################################

pharmLibraryByHGNCid = {}
roughHGNC = []

for line in fileInput_2:
	line = line.strip()
	lineSplit_2 = line.split('\t')
	
	roughHGNC.append(lineSplit_2[10])
	
	pharmLibraryByHGNCid[lineSplit_2[10].strip('HGNC:')] = [lineSplit_2[12]]

pharmHGNCids = []
for s in roughHGNC:
	if s:
		pharmHGNCids.append(s.strip('HGNC:'))
		
#~ pharmHGNCids = [s.strip('HGNC:') for s in roughHGNC]

#~ print(roughHGNC)
#~ print(pharmHGNCids)
#~ print(pharmLibraryByHGNCid)
#~ raise SystemExit

##############################################################
# Create a dictionary of each DrugBank ID and the common name.
# fileInput_3 contains the common name for each DrugBank ID.
##############################################################

drugBankCommonNames = {}

for line in fileInput_3:
	lineSplit_3 = line.split('\t')
	drugBankCommonNames[lineSplit_3[0]] = (lineSplit_3[2])

#~ print(drugBankCommonNames)	
#~ raise SystemExit

########################################################################################################################
# Create a function that identifies the receptor of interest and provides the approved pharmaceutical(s) for the target.
########################################################################################################################


def findDruggedTargets(gpcrHGNCids, pharmLibraryByHGNCid):
	for targetID in gpcrHGNCids:
		#~ print(targetID)

		if targetID in pharmLibraryByHGNCid:
			drugString = ""
			
			for drug in pharmLibraryByHGNCid[targetID][0].split(';'):
				drug = drug.strip()
				drugString += drugBankCommonNames[drug] + ' '
				
			print(targetID, gpcrHGNCids[targetID], drugString)

		#~ with open("../" + sep + "dataFiles" + sep + "approved_drugs_for_gpcrs.txt", "a") as fileOutput:
			#~ print("HGNC ID: " + targetID, "\nReceptor Name: " + gpcrHGNCids[targetID], "\nApproved drugs: " + drugString + "\n", file = fileOutput)

findDruggedTargets(gpcrHGNCids, pharmLibraryByHGNCid)






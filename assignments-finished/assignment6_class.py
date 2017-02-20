#Create Class
##############
class CancerTumor:

    #Create Class Attributes
    ########################
    def __init__(self):
        self.name = None
        self.location = None
        self.type = None

    #Create Class Method
    #####################        
    def Attributes(self):
        if self.name:
            print("Name of cancer:", self.name)
        if self.location:
            print("Location of tumor:", self.location)
        if self.type:
            print("Type of tumor:", self.type)

# Create an instance of a Patient
#################################
Patient_1 = CancerTumor()
# Populate the attributes of the class 
Patient_1.name = "Castration Resistant"
Patient_1.location = "Prostate"
Patient_1.type = "Metastatic"

Patient_1.Attributes()

# Create an instance of a Second Patient
#########################################
Patient_2 = CancerTumor()

Patient_2.name = "Triple Negative"
Patient_2.location = "Breast"
Patient_2.type = "Metastatic"

Patient_2.Attributes()

#Create an instance for a Third patient
#######################################
Patient_3 = CancerTumor()

Patient_3.name = "Carcinoma"
Patient_3.location = "Skin Epthelial"
Patient_3.type = "Non-metastatic"

Patient_3.Attributes()

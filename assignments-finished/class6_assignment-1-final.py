class HIVDiagnosticAssay:
	def __init__(self, patientID, daysAfterExposure):
		self.patientID = patientID
		self.daysAfterExposure = daysAfterExposure

	def protocol(self):
		if self.daysAfterExposure >= 21:
			print(self.patientID, "should be diagnosed using a Gag-p24 ELISA.")
		elif self.daysAfterExposure <= 7:
			print(self.patientID, "cannot have their HIV status determined.")
		else:
			print(self.patientID, "should be diagnosed using viral load analysis.")


patient1 = HIVDiagnosticAssay('VA #04774', 3)
patient2 = HIVDiagnosticAssay('VA #04776', 14)
patient4 = HIVDiagnosticAssay('VA #04779', 25)

patient1.protocol()
patient2.protocol()
patient4.protocol()

















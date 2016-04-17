import os
import re
import numpy
import time

NameList = [0,0]
RegExList = [0,0]
NameList[0] = 'Patient Barcode'
RegExList[0] = 'bcr_patient_barcode.+>(.+)<'
NameList[1] = 'Gender'
RegExList[1] = 'gender preferred_name.+>(.+)<'


path = 'D:\Anaconda\Project Canse\Data\Clinical\XML'
FileNames = os.listdir(path)
DatArray = [[0]*len(FileNames) for xyz in range(len(NameList))]

for i in range(len(FileNames)):
	b = open(path + '\\' + FileNames[i])
	c = b.readlines()
	for lines in c:
		for j in range(len(RegExList)):
			if re.search(RegExList[j],lines):
				g = re.findall(RegExList[j],lines)
				DatArray[j][i] = g[0]

print DatArray
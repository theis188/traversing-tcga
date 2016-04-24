import os
import re
import numpy
import time
from scipy import stats
import matplotlib.pyplot as plt
import sklearn

NameList = [0,0,0,0,0,0]
RegExList = [0,0,0,0,0,0]
NameList[0] = 'Patient Barcode'
RegExList[0] = 'bcr_patient_barcode.+>(.+)<'
NameList[1] = 'Gender'
RegExList[1] = 'gender preferred_name.+>(.+)<'
NameList[2] = 'Year Diagnosed'
RegExList[2] = 'year_of_initial_pathologic_diagnosis.+>(.+)<'
NameList[3] = 'Blast Percent'
RegExList[3] = 'lab_procedure_blast_cell_outcome_percentage_value.+>(.+)<'
RegExList[4] = 'days_to_death.+>(.+)<'
NameList[4] = 'Days To Death'
NameList[5] = 'FLT3'
RegExList[5] = 'molecular_analysis_abnormality_testing_result.+>(FLT3.+)<'


path = 'D:\Anaconda\Project Canse\Data\Clinical\XML'
FileNames = os.listdir(path)
DatArray = [[0]*(len(FileNames)-200) for xyz in range(len(NameList))]

for i in range(200):#,len(FileNames)):
	b = open(path + '\\' + FileNames[i+200])
	c = b.readlines()
	for lines in c:
		for j in range(len(RegExList)):
			if re.search(RegExList[j],lines):
				g = re.findall(RegExList[j],lines)
				DatArray[j][i] = g[0]

#print DatArray

CleanedBlast=[];
CleanedDays=[];
Survived=[];
SurvBlast=[];

for i in range(len(DatArray[3])):
	if (int(DatArray[3][i]) != 0):
		if int(DatArray[4][i]) == 0:
			Survived.append(1)
		else:
			Survived.append(0)
		if (int(DatArray[4][i]) != 0):
			CleanedBlast.append(int(DatArray[3][i]))
			CleanedDays.append(int(DatArray[4][i]))

#print Survived, SurvBlast

slope, intercept, r_value, p_value, std_err = stats.linregress(CleanedBlast,CleanedDays)

print 'Slope = ', slope
print 'P-value = ', p_value

plt.scatter(CleanedBlast,CleanedDays)
plt.xlabel('Blast Percentage (%)')
plt.ylabel('Days Lived')
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([0,2000])

plt.show()
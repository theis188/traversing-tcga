import os
import re
import numpy
import time
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import linear_model
from Canse1funfun import getData 
from Canse1funfun import listChange
from Canse1funfun import listClean
import psycopg2

MainArray = getData()
DataArray = MainArray[0]
NameList = MainArray[1]

DeathArray = listChange(DataArray[len(DataArray)-1],0,1500)

CleanArrayOfArrays = []
p_vals=[]
pnamelist=[]
slopess=[]

print NameList
print 
for i in range(2,len(DataArray)-1):
	#CleanArray = listChange(DataArray[i],0,0)
	Arrays = listClean(DataArray[i],999,DataArray[len(DataArray)-1],0)
	CleanArray = Arrays[0]
	DeathArray = Arrays[1]
	CleanArrayOfArrays.append(CleanArray)
	print NameList[i],'\n',CleanArray
	slope, intercept, r_value, p_value, std_err = stats.linregress(CleanArray,DeathArray)
	print 'Slope = ', slope
	print 'P-value = ', p_value
	p_vals.append(p_value)
	pnamelist.append(NameList[i])
	slopess.append(slope)
	### INDIVIDUAL SCATTER PLOTS WITH PAUSE ###
	#plt.scatter(CleanArray,DeathArray)
	#plt.xlabel(NameList[i])
	#plt.ylabel('Days Lived')
	#axes = plt.gca()
	#axes.set_xlim([min(CleanArray),max(CleanArray)])
	#axes.set_ylim([0,max(DeathArray)])
	#plt.show()
	#a = raw_input("Press Enter to continue...")

print ' '*33 +'Feature'+' '*4+'P-Value'+' '*4+'Slope'
for i in range(len(p_vals)):
	print repr(pnamelist[i]).rjust(40), repr(round(p_vals[i],5)).rjust(10), repr(round(slopess[i],5)).rjust(10)

a = raw_input("Press Enter to continue...")

FinalArray = numpy.array([CleanArrayOfArrays[0]])

for i in range(len(DataArray)-4):
	FinalArray=numpy.append(FinalArray,[CleanArrayOfArrays[i]],axis=0)

FinalArray=numpy.transpose(FinalArray)
print 'FinalArray',FinalArray,FinalArray.shape,type(FinalArray)
Indices = [index for index,value in enumerate(DeathArray) if value > 1000]
FinalArray = numpy.delete(FinalArray,Indices,axis=0)
print 'FinalArrayRemoved',FinalArray,FinalArray.shape,type(FinalArray)
for i in reversed(range(len(Indices))):
	DeathArray.pop(Indices[i])

clf = linear_model.LinearRegression()
clf.fit(FinalArray,numpy.array(DeathArray))

Coeffs = clf.coef_
print Coeffs.shape
ypred = clf.predict(FinalArray)
print ypred

print 'r-squared value = ', clf.score(FinalArray,numpy.array(DeathArray))
a = raw_input("Press Enter to continue...")


#B1 = numpy.linalg.inv(numpy.dot(FinalArray,numpy.transpose(FinalArray))

print DeathArray

plt.scatter(DeathArray,ypred)
plt.plot([1,1500],[1,1500],'k-')
axes = plt.gca()
axes.set_xlim([0,max(DeathArray)])
axes.set_ylim([0,max(DeathArray)])
plt.xlabel('Actual Days Lived')
plt.ylabel('Prediction')
plt.show()
plt.clf()


print type(ypred)
print ypred
ypred[(ypred<0)]=5
print 
ypredsqrt = ypred**(1.1)

deathnparray = numpy.array(DeathArray).reshape((103,1))
ypredsqrt = ypredsqrt.reshape((103,1))

print 'ypredsqrt',type(ypredsqrt),ypredsqrt.shape,ypredsqrt
print 'deathnparray',type(deathnparray),deathnparray.shape,deathnparray

clf2 = linear_model.LinearRegression()
clf2.fit(ypredsqrt,deathnparray)
newypred = clf2.predict(ypredsqrt)
print newypred
print clf2.coef_,float(clf2.coef_)
print clf2.intercept_,float(clf2.intercept_)

plt.scatter(deathnparray,((ypred*1.5)-100))
xxx = range(1000)
yyy = map(lambda x: float(clf2.coef_)*(x**(1.1)) + float(clf2.intercept_),xxx)
#plt.plot(xxx,yyy,'k-')
plt.plot([1,1500],[1,1500],'k-')
axes = plt.gca()
axes.set_xlim([0,max(DeathArray)])
axes.set_ylim([0,max(DeathArray)])
plt.xlabel('Actual Days Lived')
plt.ylabel('Prediction')
plt.show()

print 'sumerror1 = ', numpy.sum(numpy.square(deathnparray-ypred))
print 'sumerror2 = ', numpy.sum(numpy.square(deathnparray-((ypred*1.5)-100)))
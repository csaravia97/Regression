import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from pprint import pprint

#Hash, Four Substrings, Population and Sample Size
hash = "5C65CAC1462BF67A92193794A2F5482A"
S1, S2, S3, S4 = hash[0:8], hash[8:16], hash[16:24], hash[24:32]
divisor = "7FFFFFFF"
n = 100
n1 = 10

#Converting Hash into values
intercept = int(S1,16)/int(divisor,16)
slope = int(S2,16)/int(divisor,16)
SEED = int(S3,16)
np.random.seed(SEED)
std = int(S4,16)/int(divisor,16)
err = np.random.normal(0, std, n)

#Population 
xs = np.random.rand(n)
ys = [intercept+slope*xs[i]+err[i] for i in range(n)]


#Sample
x= xs[::n1]
y= ys[::n1]



def G(x):
	return intercept+slope*x

#Returns the average
def Avg(x):
	sum = 0
	for i in range(n1):
		sum = sum+x[i]
	return sum/n1

#Returns the Sum of Squares
def SS(x,y,Avg_x,Avg_y):
	sum = 0
	for i in range(n1):
		sum=sum+((x[i]-Avg_x)*(y[i]-Avg_y))
	return sum
		

Avg_x = Avg(x)
Avg_y = Avg(y)
SXX = SS(x,x,Avg_x,Avg_x)
SYY = SS(y,y,Avg_y,Avg_y)
SXY = SS(x,y,Avg_x,Avg_y)
b1 = SXY/SXX
b0 = Avg_y - b1*Avg_x

#Sum of Squares
SS_TOT = SYY
SS_REG = (b1 ** 2) * SXX
SS_ERR = SS_TOT - SS_REG

#Degrees of Freedom
DF_MOD = 1
DF_ERR = n1 - 2
DF_TOT = n1 - 1

#Mean Squares
MS_REG = SS_REG
MS_ERR = SS_ERR / DF_ERR

#F-Ratio
F_Ratio = MS_REG / MS_ERR

s = MS_ERR**0.5
R_Square = SS_REG/SS_TOT

#Confidence Interval for the Slope
slope_UB = b1+(2.306*(s/(SXX**0.5)))
slope_LB = b1-(2.306*(s/(SXX**0.5)))

#T-value
t = b1/(s/(SXX**0.5))

#Confidence Interval for the Mean of Responses at x=.50
mean_UB= b0+b1*0.50+(2.306*s*(((1/n)+((x[1]-Avg_x)**2)/SXX)**0.5))
mean_LB= b0+b1*0.50-(2.306*s*(((1/n)+((x[1]-Avg_x)**2)/SXX)**0.5))

#Plots Poulation
matplotlib.rcParams['axes.unicode_minus'] = True
fig,ax = plt.subplots()
ax.plot(xs, ys, 'r*')
ax.plot(xs,G(xs), 'k-')
ax.set_title('Population & its regression model')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

#Plots Sample 
matplotlib.rcParams['axes.unicode_minus'] = True
fig,ax = plt.subplots()
ax.plot(x, y, 'r*')
ax.plot(x,G(x), 'k-')
ax.set_title('Sample & its regression model')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

#Box plot of the Predictors & Response 
bp= plt.boxplot(x, 0, patch_artist=True)

for box in bp['boxes']:
	#change outline color
	box.set(color = '#000000',linewidth = 2)
	#change fill color
	box.set( facecolor = '#00ADB3')
for median in bp['medians']:
	#change color of median line
	median.set(color= '#000000',linewidth =2)
ax.set_xticklabels(['Predictors', 'Response'])
plt.show()

bp= plt.boxplot(y, 0, patch_artist=True)

for box in bp['boxes']:
	#change outline color
	box.set(color = '#000000',linewidth = 2)
	#change fill color
	box.set( facecolor = '#00ADB3')
for median in bp['medians']:
	#change color of median line
	median.set(color= '#000000',linewidth =2)
ax.set_xticklabels(['Predictors', 'Response'])
plt.show()



print("-------------------------------------------------------------------------------------------------------------")
print("	  			 Hash, Line Equation, and Population Size  			  			     ")
print("-------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t Hash: ",hash,"\n")
print("\t\t\t\t Intercept (B0): ",intercept,"\n")
print("\t\t\t\t Slope (B1): ",slope,"\n")
print("\t\t\t\t Standard Deviation: ",std,"\n")
print("\t\t\t\t Population Size: ",n)
print("-------------------------------------------------------------------------------------------------------------")


print("-------------------------------------------------------------------------------------------------------------")
print("	  			    	     Predictors	 			  			     ")
print("-------------------------------------------------------------------------------------------------------------")
pprint(np.round(xs,decimals=3,out=None),indent=25, width = 110, compact= True)
print("-------------------------------------------------------------------------------------------------------------")


print("-------------------------------------------------------------------------------------------------------------")
print("	  			    	     Response 	 			  			     ")
print("-------------------------------------------------------------------------------------------------------------")
pprint(np.round(ys,decimals=3, out= None),indent = 15, width = 101, compact= True)
print("-------------------------------------------------------------------------------------------------------------")


print("-------------------------------------------------------------------------------------------------------------")
print("	  			    	     Sample Predictors 	 			  			     ")
print("-------------------------------------------------------------------------------------------------------------")
pprint(np.round(x,decimals=3, out= None),indent = 15, width = 101, compact= True)
print("\t\t\t\t\t Sample Size: ",n1, "\n")
print("\t\t\t\t\t Sample Minimum Value: ",np.round(np.min(x), decimals=3, out=None), "\n")
print("\t\t\t\t\t Sample Maximum Value: ",np.round(np.max(x), decimals=3, out=None), "\n")
print("\t\t\t\t\t Sample Standard Deviation: ",np.round(np.std(x), decimals=3, out=None), "\n")
print("\t\t\t\t\t Sample Mean: ",np.round(np.mean(x), decimals=3, out=None),"\n")
print("\t\t\t\t\t Sample Median",np.round(np.median(x), decimals=3, out=None),"\n")
print("-------------------------------------------------------------------------------------------------------------")


print("-------------------------------------------------------------------------------------------------------------")
print("	  			    	     Sample Response	 			  			     ")
print("-------------------------------------------------------------------------------------------------------------")
pprint(np.round(y,decimals=3, out= None),indent = 15, width = 101, compact= True)
print("\t\t\t\t\t Sample Size: ",n1, "\n")
print("\t\t\t\t\t Sample Minimum Value: ",np.round(np.min(y), decimals=3, out=None), "\n")
print("\t\t\t\t\t Sample Maximum Value: ",np.round(np.max(y), decimals=3, out=None), "\n")
print("\t\t\t\t\t Sample Standard Deviation: ",np.round(np.std(y), decimals=3, out=None), "\n")
print("\t\t\t\t\t Sample Mean: ",np.round(np.mean(y), decimals=3, out=None),"\n")
print("\t\t\t\t\t Sample Median",np.round(np.median(y), decimals=3, out=None),"\n")
print("-------------------------------------------------------------------------------------------------------------")


print("-------------------------------------------------------------------------------------------------------------")
print("	  |			   |	     ANOVA Table	 |			  |			    |")
print("----------|------------------------|-----------------------------|------------------------|-----------------|")
print("Source	  |	Sum of Squares	   |	  Degrees of Freedom	 |	Mean Squares	  |		F 	    |")
print("----------|------------------------|-----------------------------|------------------------|-----------------|")
print("Model 	  |	%s 	   |		  %s 		 |	%s 	  |	%s   |" % (SS_REG,DF_MOD,MS_REG,F_Ratio))
print("----------|------------------------|-----------------------------|------------------------|-----------------|")
print("Error 	  |	%s 	   |		  %s 		 |	%s 	  |			    |" % (SS_ERR,DF_ERR,MS_ERR))
print("----------|------------------------|-----------------------------|------------------------|-----------------|")
print("Total 	  |	%s 	   |		  %s 		 |		  	  |			    |" % (SS_TOT,DF_TOT))
print("----------+------------------------+-----------------------------+------------------------+-----------------+")


print("-------------------------------------------------------------------------------------------------------------")
print("	  		Slope, Confidence Intervals, F Test, T-value, and R-Square 	 			  			     ")
print("-------------------------------------------------------------------------------------------------------------")
print("\t \t \t Equation of the Regression Line: ", b0, "+", b1, "x \n")
print(" \t \t \t Confidence Interval for the Slope: ( ",np.round(slope_LB,decimals = 3, out = None), ",", np.round(slope_UB,decimals = 3, out = None), ")\n")
print(" \t \t Confidence Interval for the Mean of Responses for x = 0.50:(",np.round(mean_LB,decimals = 3, out = None), ",", np.round(mean_UB,decimals = 3, out = None),") \n")
print("\t \t \t \t \t T- value: ", np.round(t,decimals = 3, out = None), "\n")
print("\t \t \t \t \t F-Ratio: ", np.round(F_Ratio,decimals = 3, out = None), "\n")	
print("\t \t \t \t \t R-Square: ", np.round(R_Square,decimals = 4, out = None), "\n")
print("-------------------------------------------------------------------------------------------------------------")







import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from numpy import loadtxt

#Define x and y values from the data
data = loadtxt("dataplanckmks.txt").array
xData = data[:, 0]
yData = data[:, 1]



#Fitting function

def planckfunction(x, T):

    h = 6.626070150*10**(-34) #Js
    c = 299792458 #m/s
    k = 1.3806488*10**(-23) #J/K
    return (2*h*c**2)/((x**5)*(np.exp((h*c)/(x*k*T))-1)

#Plot experimental data points
plt.plot(xData, yData, '.', label='experimental-data')

#Perform the curve-fit

initialGuess= 5000

popt, pcov = curve_fit(planckfunction, xData, yData, initialGuess)
print(popt)

#X values for the fitted function

xFit = np.arrange(0.0, 5.0, 0.01
                  )
#Plot the fitted function
plt.plot(xFit, planckfunction(xFit, *popt), 'r', label='fit params')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

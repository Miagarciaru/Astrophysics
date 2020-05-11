import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import curve_fit
from numpy import loadtxt


#Define x and y values from the data
data = loadtxt("data-planckiana.txt")
xData = data[:, 0]
yData = data[:, 1]

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


#Define function

def planckfunction(x, T):

    h = 6.626070150*10**(-34) #Js
    c = 299792458 #m/s
    k = 1.3806488*10**(-23) #J/K
    return (2*h*c**2)/((x**5)*(np.exp((h*c)/(x*k*T))-1))

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


                       
plt.plot(xData, yData, 'bo', label='experimental-data')

#Perform the curve-fit

initialGuess= 5000

popt, pcov = curve_fit(planckfunction, xData, yData, initialGuess)
print(popt)

#X values for the fitted function

xFit = np.arange(0.0, 0.000006, 0.001)

#Plot the fitted function
plt.plot(xFit, planckfunction(xFit, *popt), 'r', label='fit params')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

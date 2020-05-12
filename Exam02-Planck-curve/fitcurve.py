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

    h = 6.626070150 #e-34Js
    c = 2.99792458 #e10m/s
    k = 1.3806488 #e-23J/K
    return (2*h*c**2)/((x**5)*(np.exp((h*c)/(x*k*T))-1))

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


plt.figure(figsize=(6,8))                       
plt.plot(xData, yData, '.', label='Experimental-data')

#Perform the curve-fit


popt, pcov = curve_fit(planckfunction, xData, yData*10)
print(popt)

#X values for the fitted function

xFit = np.arange(0.0, 5.2, 0.1)

#Plot the fitted function

plt.grid()
plt.title('Spectrum from Solar surface')
plt.xlabel('Wavelength $\lambda$ ($\mu$m)',fontsize=12)
plt.ylabel('Astrophysical Flux at the Solar surface ($10^{10}$ erg $cm^{-2}$ $s^{-1}$ $\mu$$m^{-1}$ $ster^{-1}$)',fontsize=12)
plt.plot(xFit, planckfunction(xFit, *popt)/10, 'r', label='Fitted curve')
plt.legend()
plt.show()

set term pngcairo size 1280, 960
set output 'Fit-Planck-Curve.png'
set key box
set xlabel 'Wavelength'
set ylabel 'Astrophysical flux at the solar surface'
set key width 1
set border 3
set tics nomirror
set border lw 2
R=6.95508*(10**10) #Radio del Sol
h=6.6261*(10**(-27)) #Constante de Planck en unidades cgs
Kb=1.380649*(10**(-16)) #Constante de Boltzmann en unidades cgs
c=2.99792458*(10**10) #velocidad de la luz en unidades cgs
r=1.49597870*(10**13) #Distancia del Sol a la Tierra en cgs
f(x)=((2*pi*h*(c**2))/(a**5))*(((R/r)**2)/(exp((h*c)/(Kb*T))-1))
fit f(x) "data-planckiana.txt" using 1:3 via a,T
plot "data-planckiana.txt" using 1:3, f(x) 

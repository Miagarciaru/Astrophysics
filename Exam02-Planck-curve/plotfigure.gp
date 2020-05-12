set term pngcairo size 1280, 960
set output 'Fit-Planck-Curve.png'
set key box
set xlabel 'Wavelength'
set ylabel 'Astrophysical flux at the solar surface'
set key width 1
set border 3
set tics nomirror
set border lw 2
h=6.6261 #Constante de Planck en unidades cgs
K=1.380649 #Constante de Boltzmann en unidades cgs
c=2.99792458 #velocidad de la luz en unidades cgs
f(x)=(2*h*(c**2))/((x**5)*(exp((h*c)/(x*K*T))-1))
fit f(x) "data-planckiana.txt" using 1:($2*10) via T
plot "data-planckiana.txt" using 1:2 , f(x)/10 

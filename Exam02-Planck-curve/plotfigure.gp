set term pngcairo size 1280, 960
set output 'Fit-Planck-Curve.png'
set title "Spectrum from Solar surface" font ',20'
set key box
set xlabel 'Wavelength {/Symbol l} ({/Symbol m}m)' font ',18'
set ylabel 'Astrophysical flux at the solar surface (10^{10} erg cm^{-2} s^{-1} {/Symbol m}m^{-1} ster^{-1})' font ',18'
set key width 1
set key font ',16'
set border 3
set tics nomirror
set grid
set border lw 2
h=6.6261 #Constante de Planck en unidades cgs
K=1.380649 #Constante de Boltzmann en unidades cgs
c=2.99792458 #velocidad de la luz en unidades cgs
f(x)=(2*h*(c**2))/((x**5)*(exp((h*c)/(x*K*T))-1))
fit f(x) "data-planckiana.txt" using 1:($2*10) via T
plot "data-planckiana.txt" using 1:2 title "Experimental data" lt 7 lc 7 w p, f(x)/10 title "Fitted Curve" 

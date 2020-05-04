set term pngcairo size 1280, 960
set output 'Fit-Planck-Curve.png'
set key box
set xlabel 'Wavelength'
set ylabel 'Astrophysical flux at the solar surface'
set key width 1
set border 3
set tics nomirror
set border lw 2
plot "data-planckiana.txt" using 1:3 w p 

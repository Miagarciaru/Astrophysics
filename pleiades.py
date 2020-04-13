"""
 Programa para realizar el diagrama color-magnitud a partir de datos de Gaia

 En la estructura del programa, primero se importan las librerías que van a ser 
 de utilidad para realizar el diagrama. Luego se realizan las funciones que nos
 permiten realizar la conversión entre magnitudes de Gaia y Johnson-Cousins.
 
 Importante:
 En la lectura de los archivos de la tabla VOT, hay columnas que pueden no estar
 para una estrella en particular (diapositiva 25). Esto puede generar WARNINGS.
 Para que no muestre los Warnings, se importa y usa la librería warnings.
 
 Estos datos serán tomados en cuenta más adelante, puesto que no se pueden 
 realizar operaciones con dichos valores no existentes (a estos valores se le 
 conoce también como nan: Not A Number).
 
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io.votable import parse_single_table
#import warnings   # ------ librería que esconde los warnings
#warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# definición de funciones

def Magnitude(V,d,E):
    M = V - 5*np.log10(d/10) - 3.2*E
    return M


# En las diapositivas se explica bien cómo funciona la siguiente función
def B_V(BP_RP): 
    GG = np.ones(2000)*BP_RP
    a = 0.0981
    b = 1.4290
    c = -0.0269
    d = 0.0061
    B_V = np.linspace(-2,4,2000)
    right = a + b*(B_V) + c*(B_V)**2 + d*(B_V)**3
    idx = np.argwhere(np.diff(np.sign(GG - right))).flatten()
    return B_V[idx][0]


def V(B_V,RP):
    a = 0.1245
    b = 1.0147
    c = 0.1329
    d = -0.0044
    V = RP + a + b*(B_V) + c*(B_V)**2 + d*(B_V)**3
    return V

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------



# Se lee la tabla con el nombre del archivo
data = parse_single_table("pleiades.vot").array
 
G = data['phot_g_mean_mag']    # Magnitud absoluta de Gaia
bp_rp = data['bp_rp']          # Indice de color de Gaia
temp = data['teff_val']        # Temperatura efectiva
rp = data['phot_rp_mean_mag']  # G_RP: Indice centrado en 797 nm 
d = 1000/data['parallax']      # Distancia en parsec (d=1/paralaje)
E = 0.030                      # Valor del reddening (tomado de WEBDA)


# Se crean ARRYAS vacíos con el fin de llenarlos de los datos de los índices
# de Johnson-Cousins
b_v = np.zeros(len(G))  # Acá se pondrá el índice de color       (B-V)
v   = np.zeros(len(G))  # Acá se pondrá el filtro en el visible  (V)
Mv  = np.zeros(len(G))  # Acá se pondrá la Magnitud absoluta     (Mv)


# Se hace un barrido sobre cada uno de los datos que contienen los arrays.
# Fíjense que a las funciones creadas, les ingresan números.
# El ciclo for corre desde 0 hasta el tamaño que tenga G.
for i in range(len(G)):
    """
        La siguiente función, "isinstance", garantiza que bp_rp sea un número,
        esto puesto que muchos datos son vacíos (ver diapositiva 25). Si no se 
        llegase a colocar el isinstance, no se podrían hacer las operaciones de 
        las funciones que creamos y retornaría un error. 

        Probarlo sin isinstance a ver cómo correría.

        En el siguiente if, se mira el tipo de variable es cada uno de los datos
        de bp_rp. Esto se hace barriendo cada uno de los datos con bp_rp[i] y 
        mirando si son floats (otro tipo de variable son enteros "int", cadenas
        "strings", etc.).
    """
    if isinstance(bp_rp[i],np.float32):  # Garantiza que bp_rp sea un número
        BP_RP = bp_rp[i]
        RP = rp[i]
        b_v[i] = B_V(BP_RP)         # Se ingresa cada número que está en bp_rp
        v[i]   = V(b_v[i],RP)              # Acá se va escribiendo el array v
        Mv[i]  = Magnitude(v[i],d[i],E=E)  # Acá se va escribiendo el array Mv
    else:
        b_v[i] = np.nan     # Si bp_rp no es un número, lo llena con NAN 
        v[i]   = np.nan
        Mv[i]  = np.nan
        print(i)



plt.plot(b_v-E,Mv,'.')     # Ojo, se hace (B-V)-E, índice de color intrínseco
plt.gca().invert_yaxis()
plt.grid()
plt.xlabel('Color Index (B-V)',fontsize=12)
plt.ylabel('Absolute Magnitude',fontsize=12)
plt.show()




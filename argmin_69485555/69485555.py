import numpy as np
import matplotlib.pyplot as plt
import math
from math import e

#para niquel

D= 0.4205 #profundidad de pozo
f = 2.7540 #distancia de equilibrio
a = 1.4199 #ancho de potencial
x = np.arange(-100,100,0.01) #Distancia interatómica / eje X
y = -D + D*(1-e**(-a*(x-f)))**2


# plt.xlabel('Distancia interatómica [$\AA$]')
# plt.ylabel('Energía [eV]')
# plt.plot(x, y, color = 'mediumturquoise')
# plt.xlim(2,5.5)
# plt.ylim(-0.5, 0.75)

print(np.argmin(y) * 0.01 + -100)
print(x[np.argmin(y)])
#plt.annotate('a$_{0}$', xy = (X, min(y)) ) HERE'S WHERE I'D NEED THE X COORDINATE!!

plt.show()
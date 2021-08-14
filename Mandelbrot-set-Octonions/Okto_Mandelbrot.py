######  Mandelbrot set #### OKTONIJONŲ aritmetika 21 užduotis  ###
# Oktonijonų aritmetikoje realizuoti iteracijas zn+1 = zn^2 + r, z0 = (0.1,0,0,0,0,0,0,0).
## Pavaizduoti spalvinę diagramą srityje (r1,r7) (taip pat srityje (r5,r8)),
### atspindinčią didėjančių kaimyninių iteracijų (kai patenkinta sąlyga |zn| <= |zn+1|), kiekį.

from Okto_aritmetika import okto_modulis, okto_daugyba, okto_suma
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

iteracijos = 255
begalybe = 1000.0
rezx = 100
rezy = 100
xmin = -0.5
xmax = 0.0
ymin = -1.0
ymax = -0.5
ilgis = xmax - xmin
aukstis = ymax - ymin
zingsnisx = ilgis/rezx      #pikselio (langelio) dydis x
zingsnisy = aukstis/rezy    #pikselio (langelio) dydis y

# žemiau pateikiama z0 reikšmė duota sąlygoje. Ji naudojama tik vieną kartą
z0 = n1, n2, n3, n4, n5, n6, n7, n8 = [0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
pav = np.zeros((rezx, rezy)) # paruošiama 'drobė' poaveikslėlio braižymui - list'ai su nuliais

def mandelbrot(r):
    z_senas = z0
    z_naujas =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    counter = 0
    n = 0
    while okto_modulis(z_senas) <= begalybe and n < iteracijos:
        z_naujas = okto_suma(okto_daugyba(z_senas), r)
        if okto_modulis(z_senas) <= okto_modulis(z_naujas):
            counter +=1
        z_senas =z_naujas
        n+=1
    if okto_modulis(z_senas) > begalybe:
        counter = 255 - n
    return counter

for i in range(0, rezx):
    x = xmin + i * zingsnisx
    for f in range(0, rezy):
        y = ymin + f * zingsnisy
        #r = [0.0, 0.0, 0.0, 0.0, x, 0.0, 0.0, y] # diagrama sroityje r5,r8
        r = [x, 0.0, 0.0, 0.0, 0.0, 0.0, y ,0.0 ] # diagrama srityje r1,r7
        man_set = mandelbrot(r)
        pav[f, i] = man_set

#paveikslėlio braižymas
fig, ax = plt.subplots()
ax.imshow(pav, interpolation='nearest', cmap=cm.jet,extent=[xmin, xmax, ymin, ymax])
#fig.savefig('r1r7_jett1000.png')
plt.show()
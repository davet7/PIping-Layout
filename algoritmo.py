from astar.search import AStar
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



    # mapa rectangular de cualquier valor

alto = 100 #int(input("Introduzca el alto del área de trabajo: "))
ancho = 100 #int(input("Introduzca el ancho del área de trabajo: "))

world = np.zeros((alto,ancho))
l = int(len(world))
print(l)

anchopr = 30 #int(input("Introduzca el Ancho Piperack: ")) 

largopr = 30 #int(input("Introduzca el Largo Piperack: "))

altopr = 10 #int(input("Introduzca el Alto Piperack: "))

seccionespr = 2 #int(input("Introduzca el número de secciones del Piperack: "))
seccionespr += 1



fp = int(((l - largopr)//2))  #3
print(fp)
sp = int(l - ((l - largopr)//2)) #7
print(sp)

lin_piperack = []

for i in range(fp):
  world[i][fp-1] = 5
  linea = (i,fp-1)
  lin_piperack.append(linea)
for j in range(sp,l,1):  
  world[j][fp-1] = 5
  linea = (j,fp-1)
  lin_piperack.append(linea)
for h in range(fp):
  world[h][sp] = 5
  linea = (h,sp)
  lin_piperack.append(linea)
for k in range(sp,l,1):
  world[k][sp] = 5
  linea = (k, sp)
  lin_piperack.append(linea)
for o in range(fp, sp+1, 1):
  world[fp-1][o] = 5
  linea = (fp-1, o)
  lin_piperack.append(linea)
for p in range(fp, sp+1, 1):
  world[sp][p] = 5
  linea = (sp,p)
  lin_piperack.append(linea)

print(lin_piperack)
xp = [x[1] for x in lin_piperack]
yp = [y[0] for y in lin_piperack]

plotPiperackX = [fp, fp, sp, sp, fp]
plotPiperackY = [fp, sp, sp, fp, fp]

plotPiperackL1 = [fp, fp, fp, fp, fp, sp, sp, sp, sp, sp]
plotPiperackL2 = [fp, fp, sp, sp, sp, sp, sp, sp, fp, fp]
plotPiperackZ =  [ 0,  altopr,  altopr,  0,  altopr,  altopr,  0,  altopr, altopr,  0]

corEX = []
corEY = []

plt.imshow(world)
def muestraPiperack(seccionespr,plotPiperackX, plotPiperackY,plotPiperackL1, plotPiperackL2,plotPiperackZ,altopr,corEX, corEY):
  fig = plt.figure(figsize = (100,30))
  ax = fig.add_subplot(111, projection='3d')

  for i in range(seccionespr):
    ax.plot(plotPiperackX, plotPiperackY,((altopr/seccionespr))*(i+1), linewidth=10, color='red')

  ax.plot(plotPiperackL1, plotPiperackL2,plotPiperackZ, linewidth=10,color='red')
  ax.scatter3D(0, 0, 0,s = 1 , marker = "o", color='red')
  ax.scatter3D(alto, ancho, 0,s = 1 , marker = "o", color='red')
  ax.scatter3D(corEX, corEY, 0,s = 800 , marker = "x", color='green')
 
  #ax.scatter3D(xp, yp, 2,s = 1000 , marker = "o", color='red')
  return plt.show()

muestraPiperack(seccionespr,plotPiperackX, plotPiperackY,plotPiperackL1, plotPiperackL2,plotPiperackZ,altopr,corEX, corEY)
"""
world = [
        [0,0,0,0,0,0],
        [1,1,0,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,1,0,0],
        [0,0,0,1,0,0],
        [0,0,0,1,0,0],
        ]

print(world)
"""


all_paths = []

#equipos

equipos = []
tagEquipos = []
corEX = []
corEY = []



ask = ''
while ask != "no":  #while submit new
  ask = input("¿Añadir un equipo?: ")
  if  ask != "no":
    nuevoEquipo = input("Ingrese nombre del equipo:\n")
    nuevoTag = input("Ingrese TAG de equipo:\n")
    nuevoCorEX = int(input("Ingrese coordenada en X:\n"))
    nuevoCorEY = int(input("Ingrese coordenada en Y:\n"))
    

    equipos.append(nuevoEquipo)
    tagEquipos.append(nuevoTag)
    corEX.append(nuevoCorEX)
    corEY.append(nuevoCorEY)
    
  
    print(equipos)
    print(tagEquipos)
    print(corEX)
    print(corEY)

    muestraPiperack(seccionespr,plotPiperackX, plotPiperackY,plotPiperackL1, plotPiperackL2,plotPiperackZ,altopr,corEX, corEY)

  
 
#generar una conexión

ask1 = ''
while ask1 != "no":  #while submit new
  ask = input("¿Añadir una conexión?: ")
  if  ask != "no":
    equipoInicial = int(input("Ingrese el número del equipo del equipo inicial: "))
    equipoFinal = int(input("Ingrese el número del equipo final: "))
    nivel = int(input("Ingrese el nivel en el piperack: "))

    sx = corEX[equipoInicial-1]
    sy = corEY[equipoInicial-1]
    gx = corEX[equipoFinal-1]
    gy = corEY[equipoFinal-1]

        # define a start and end goals (x, y) (vertical, horizontal)

    start = (sx, sy)
    goal = (gy, gx)
    """
    start = (5, 3)
    goal = (5, 25)
    """

        # search
    path = AStar(world).search(start, goal)
    print(path)


    xs = [x[1] for x in path]
    ys = [y[0] for y in path]

    print(len(xs))
    print(len(ys))

    plt.figure(1)
    plt.plot(xs, ys)
    plt.imshow(world)

    for z in range(len(xs)):
        world[ys[z]][xs[z]] = 1
        paths = (ys[z],xs[z])
        all_paths.append(paths)


    #guarda todos los valores de los paths
    
    
    xa= [x[1] for x in all_paths]
    ya = [y[0] for y in all_paths]



    #plt.figure(2)
    plt.imshow(world)
    fig2 = plt.figure(figsize = (100,30))
    ax = fig2.add_subplot(111, projection='3d')
    
    for i in range(seccionespr):
      ax.plot(plotPiperackX, plotPiperackY,((altopr/seccionespr))*(i+1), linewidth=10, color='red')
    ax.plot(plotPiperackL1, plotPiperackL2,plotPiperackZ, linewidth=10,color='red')
    ax.scatter3D(0, 0, 0,s = 100 , marker = "o", color='red')
    ax.scatter3D(alto, ancho, 0,s = 100 , marker = "o", color='red')
    #ax.scatter3D(xp, yp, 1,s = 1000 , marker = "o", color='red')
    ax.scatter3D(xa, ya, ((altopr/seccionespr)*nivel), s = 1000, color='blue')

    plt.show()














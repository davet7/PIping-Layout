from astar.search import AStar
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


    # Make a map (any size!)

alto = 300 #int(input("Introduzca el alto del área de trabajo: "))
ancho = 300 #int(input("Introduzca el ancho del área de trabajo: "))

world = np.zeros((alto,ancho))
l = int(len(world))
print(l)

anchopr = 30 #int(input("Introduzca el alto Piperack: ")) 

altopr = 40 #int(input("Ancho Piperack: "))

f = (l - altopr)//2
print(f)
fp = int(((l - altopr)//2))  #3
print(fp)
sp = l - ((l - altopr)//2) #7
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

plt.imshow(world)
fig = plt.figure(figsize = (100,30))
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(xp, yp, 2,s = 500 , marker = "o", color='red')
plt.show()

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

ask = "si"
all_paths = []


while ask == "si" or "SI" or "Si" or "sI":
  ask = input("¿Añadir una conexión?: ")

  sx = int(input("Inicio en X: "))
  sy = int(input("Inicio en y: "))
  gx = int(input("Final en y: "))
  gy = int(input("Final en X: "))

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
  ax.scatter3D(xp, yp, 2,s = 1000 , marker = "o", color='red')
  ax.scatter3D(xa, ya, 2, s = 1000, color='blue')

  plt.show()

else: 
 print("FIN DEL PROGRAMA")












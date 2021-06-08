import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#This will be a 2D version of the relaxation method

#First step is to initialize our 2D grid, 
xmax=141;
ymax=90;

#initializing x-values, y-values, and making a meshgrid (2D array of values)
delta = 1;
x = np.arange(0, xmax, delta)
y = np.arange(0, ymax, delta)
X, Y = np.meshgrid(x, y)
length = len(Y[0])
height = len(Y)
V=np.zeros((height, length))
E_x=np.zeros((height, length))
E_y=np.zeros((height, length))
Enew=np.zeros((height, length))
print(V.shape)
print(Y.shape)

#initialize the edges and some values here
B1 = V[0:10,10:length-10]= 100
B2 = V[height-10: ,10:length-10]= 10
B3 = V[10:height-10,0:10] = 0
B4 = V[10:height-10,length-10:] = 0
B5 = V[:10,50:91] = -50
B6 = V[height-30:,70:71] = 100
#Random Boundary Conditions for Problem 3
'''
B1 = V[0:10,10:length-10]= random.randrange(-100,100)
B2 = V[height-10: ,10:length-10]= random.randrange(-100,100)
B3 = V[10:height-10,0:10] = random.randrange(-100,100)
B4 = V[10:height-10,length-10:] = random.randrange(-100,100)
B5 = V[:10,50:91] = random.randrange(-100,100)
B6 = V[height-30:,70:71] = random.randrange(-100,100)
'''



V[:10,50:91] = -50
V[height-30:,70:71] = 100
#relaxation loop here
m = 0
while m<1000:
    Vprev = V
    #take average:
    Vprev = V
    for i in range(1,height-1): 
        for j in range(1, length-1): 
            V[i,j]=((Vprev[i-1,j] + Vprev[i+1,j]+ Vprev[i,j-1]+ Vprev[i,j+1])/ 4.0) 
    V[0:10,10:length-10]= B1
    V[height-10: ,10:length-10]= B2
    V[10:height-10,0:10] = B3
    V[10:height-10,length-10:] = B4
    V[:10,50:91] = B5
    V[height-30:,70:71] = B6
    print(m)
    m+=1


fig1 = plt.figure()
cp1 = plt.contourf(X, Y, V, 25)
plt.title('Voltage (V)')
plt.show()

for i in range(1, height -1):
    for j in range(1, length -1):
        E_y[i,j] = (V[i-1,j]+V[i+1,j])/2

fig2 = plt.figure()
cp2 = plt.contourf(X, Y, E_y, 25)
plt.title('Electric Field in the y direction')
plt.show()

for i in range(1, height -1):
    for j in range(1, length -1):
        E_x[i,j] = (V[i,j-1]+V[i,j+1])/2

fig3 = plt.figure()
cp3 = plt.contourf(X, Y, E_x, 25)
plt.title('Electric Field in the x direction')
plt.show()
'This feels wrong, but idk'
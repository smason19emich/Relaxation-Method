import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#initializing my figure
fig1 = plt.figure()

#some initial conditions
i=1
m=0
n=0

#My potential:setting up 100 points, going from 1 to 18
V=np.linspace(0,0, num=100)
#setting up 100 points, going from 0 to 100
xes  =np.linspace(0,100, num=100)
#100 random numbers
B = np.random.rand(100)*30

#lets initialize our potential boundaries here:
V[0] = 10
V[99] = 18
#other potential values will just be random:
V[1:98] = B[1:98]
while m<750:
    #take average:
    Vprev = V
    for i in range(1,99): 
        V[i]=((Vprev[i-1] + Vprev[i+1])/ 2.0) 
    m+=1
    n+=1
    if n==10:
        plt.plot(xes, V, 'r-', label='q2',color = (0.5+5e-4*m,.3+5e-4,.1+(.9/751)*m))
        n=0

plt.plot(xes, V, 'r-', label='q2', color='darkblue')             
plt.show() 


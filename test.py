import scipy.stats as sps
import random

a0=13.3799576394
b0=12.1360521616                      
N=1000                                  #nombre de simulation
K=[50, 200, 500, 1000]                  #nombre de famille
K=[320]*10

def f(x):
    return sps.beta.ppf(x,a0,b0)

L=0
for k in K:
    X5=[0]*k                            #initialisation
    Mk=0; Vk=0; Lk=0
    q=w=e=r=t=y=0
    for i in range(k):
        p=f(random.random())            #p de chaque famille
        #print p
        for j in range(5):
            if(random.random()<p):
                X5[i]+=1
        Mk+=X5[i]
        Lk=Lk+(X5[i]**2)
    for i in range(k):
        if (X5[i] == 0): q+=1
        if (X5[i] == 1): w+=1
        if (X5[i] == 2): e+=1
        if (X5[i] == 3): r+=1
        if (X5[i] == 4): t+=1
        if (X5[i] == 5): y+=1
    print q,w,e,r,t,y
    
    Mk=Mk*1.0/k
    Vk=Lk*1.0/k-Mk**2
    #print Mk, Vk
    a=(Mk*(5-Mk)-Vk)*Mk/(5*Vk-Mk*(5-Mk))
    b=(Mk*(5-Mk)-Vk)*(5-Mk)/(5*Vk-Mk*(5-Mk))
    print a,b

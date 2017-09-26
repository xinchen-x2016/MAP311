import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
import random

a0=13.3799576394; b0=12.1360521616      #calcule dans la question 2.4
N=1000                                  #nombre de simulation
K=[50, 200, 500, 1000]                  #nombre de famille

def f(u):
    return sps.beta.ppf(u,a0,b0)


for k in K:
    xk=yk=[]
    Ea2=Ea=Eb2=Eb=Eab=0
    for n in range(N):
        X5=[0]*k
        Mk=0; Vk=0
        for i in range(k):
            p=f(random.random())        # p de chaque famille
            for j in range(5):
                if(random.random()<p):
                    X5[i]+=1
            Mk+=X5[i]; Vk+=(X5[i]**2)
        Mk=Mk*1.0/k; Vk=1.0*Vk/k-Mk**2
        D=5*Vk-Mk*(5-Mk)
        if (D==0):D+=0.00000001
        a=(Mk*(5-Mk)-Vk)*Mk/D
        b=(Mk*(5-Mk)-Vk)*(5-Mk)/D
        xk.append(np.sqrt(k)*(a-a0))
        yk.append(np.sqrt(k)*(b-b0))
        Ea=Ea+a/k
        Eb=Eb+b/k
        Ea2=Ea2+a**2/k
        Eb2=Eb2+b**2/k
        Eab=Eab+a*b/k
    C=[[Ea2-Ea**2, Eab-Ea*Eb],[Eab-Ea*Eb, Eb2-Eb**2]]
    print C                            #estimation de theta
 

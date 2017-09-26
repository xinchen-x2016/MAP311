import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

Mk = (5*18+4*52+3*110+2*88+1*35)/320.0
Vk = (5*5*18+4*4*52+3*3*110+2*2*88+1*35)/320.0-Mk**2

print Mk,Vk

def ak(n):
    return ((Mk*(n-Mk)-Vk)*Mk)/(n*Vk-Mk*(n-Mk))
def bk(n):
    return (Mk*(n-Mk)-Vk)*(n-Mk)/(n*Vk-Mk*(n-Mk))

print ak(5),bk(5)

x = np.linspace(0,1,1000)
f_x=sps.beta.pdf(x,ak(5),ak(5))
plt.plot(x,f_x)
plt.title('Beta:a='+str(round(ak(5),3))+',b='+str(round(bk(5),3)))
plt.xlabel('x')
plt.ylabel('densite')

def f(x):
    return sps.beta.pdf(x,ak(5),bk(5))

p1=0
for i in range(500,999):
    p1 += f(x[i])*0.001

print p1
plt.show()


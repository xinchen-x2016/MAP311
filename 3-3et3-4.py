import numpy as np
import scipy.special as scs
import matplotlib.pyplot as plt

N=[5,50,500,5000]
a=13.37995764
b=12.13615216

def f(x,n):
    return x**(a+n-1)*(1-x)**(b-1)/scs.beta(a+n,b)

fig,ax=plt.subplots(nrows=2,ncols=2)
i=1
for n in N:
    plt.subplot(2,2,i)
    i+=1
    x=np.linspace(0,1,1000)
    f_x=f(x,n)
    p=0
    for j in range(500,999):
        p=p+0.001*f(x[j],n)
    plt.plot(x,f_x)
    plt.title('n='+str(n)+',  P(P>1/2)='+str(round(p,3)))

plt.show()

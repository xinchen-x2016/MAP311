import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
import random
from mpl_toolkits.mplot3d import Axes3D

a0=13.3799576394; b0=12.1360521616      #resultat de quetion2-4
N=1000                                  #nombre de simulation
k=50                                    #nombre de famille, k=50,200,500,1000

def f(u):
    return sps.beta.ppf(u,a0,b0)

def draw(fre):
	fig = plt.figure()
	ax1 = fig.add_subplot(111, projection='3d')
	xx = []
	yy = []

	for i in range(-200,200,5):
		for j in range(80):
			xx.append(i)

	for i in range(80):
		for j in range(-200,200,5):
			yy.append(j)
	
	zz = np.zeros((80 * 80))
	
	dx = np.zeros((80*80))+5
	dy = np.zeros((80*80))+5
	dz = np.zeros((80*80))

	for i in range(80):
		for j in range(80):
			dz[i*80+j] = fre[i][j]
			
	ax1.bar3d(xx, yy, zz, dx, dy, dz, color='#00ceaa')
	plt.show()

def count_frequency(file_):
	fin = open(file_,'r')
	fre=np.zeros((80,80)) # (-200,200,5) # avoir 80 * 80 bars
	for line in fin:
		line = line.strip("\n").split(" ")
		if -200 < float(line[0]) < 200 and -200 < float(line[1]) < 200 :
			x = (int(float(line[0])) + 200)/5
			y = (int(float(line[1])) + 200)/5
			fre[x][y] += 1
	fin.close()
	return fre

xk=[]
yk=[]
for n in range(N):                  #simulation 1000 fois, chaque k
    X5=[0]*k
    Mk=0; Vk=0
    for i in range(k):              
        p=f(random.random())        # p: probabilité d'avoir un garçon
        for j in range(5):          #chaque famille a 5 enfants
            if(random.random()<p):  
                X5[i]+=1            # le nombre de garçon dans une famille
        Mk+=X5[i]; Vk+=(X5[i]**2)
    Mk=Mk*1.0/k; Vk=1.0*Vk/k-Mk**2 
    D=5*Vk-Mk*(5-Mk)
    if D==0: 
        D+=0.0000001
    a=(Mk*(5-Mk)-Vk)*Mk/D
    b=(Mk*(5-Mk)-Vk)*(5-Mk)/D
    xk.append(np.sqrt(k)*(a-a0))   
    yk.append(np.sqrt(k)*(b-b0))

fout = open("points.txt",'w')
for i in range(N): #écrire les x-pointes et y-pointes dans un fichier .txt
    fout.write(str(xk[i])+" "+str(yk[i])+"\n")
fout.close()

frequency = count_frequency("points.txt")
draw(frequency)


import numpy as np
import matplotlib.pyplot as plt

R=3 #radius of generator circle
N=200 #resolution
NP=3 #number of periods

tau = np.linspace(0,NP*2*np.pi,N) #parametrization
x= R*(tau-np.sin(tau))
y =R*(1-np.cos(tau))

plt.figure(figsize=(10,2))
plt.plot(x/2/np.pi/R,y/R,c='r',linewidth=3)
plt.ylabel(r"$y/R$",fontsize=15)
plt.xlabel(r"$x/(2\pi R)$",fontsize=15)
plt.savefig('./'+'cyclo.pdf')
plt.tight_layout()
plt.show()


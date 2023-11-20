import numpy as np
import matplotlib.pyplot as plt

#################################################################################################
#simple cycloid  

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

################################################################################################
#cycloid with parametrization in tau 

R=3 #radius of generator circle
N=200 #resolution
NP=1 #number of periods

tau = np.linspace(0,NP*2*np.pi,N) #parametrization
x= R*(tau-np.sin(tau))
y =R*(1-np.cos(tau))

taumk = np.arange(0,NP*2*np.pi,0.25)
xmk = R*(taumk-np.sin(taumk))
ymk = R*(1-np.cos(taumk))

plt.figure(figsize=(10,2))
plt.plot(x/2/np.pi/R,y/R,c='r',linewidth=3)
plt.scatter(xmk/2/np.pi/R,ymk/R,marker='o',c='k',zorder=1000)
plt.ylabel(r"$y/R$",fontsize=15)
plt.xlabel(r"$x/(2\pi R)$",fontsize=15)
plt.savefig('./'+'cyclo_mk.pdf')
plt.tight_layout()
plt.show()

#################################################################################################
#trochoid 

R1=6 #radius of generator circle
R2=3 #radius of generator circle
N=200 #resolution
NP=3 #number of periods

tau = np.linspace(0,NP*2*np.pi,N) #parametrization
x= R1*tau-R2*np.sin(tau)
y =R1-R2*np.cos(tau)

plt.figure(figsize=(10,2))
plt.plot(x/2/np.pi/R1,y/R1,c='r',linewidth=3)
plt.ylabel(r"$y/R_1$",fontsize=15)
plt.xlabel(r"$x/(2\pi R_1)$",fontsize=15)
plt.ylim([0,2])
plt.savefig('./'+'trochoid.pdf')
plt.tight_layout()
plt.show()

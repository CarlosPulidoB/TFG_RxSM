import numpy as np
import matplotlib.pyplot as plt


puntos = np.loadtxt('comp.txt') #masa,alpha,x

hhH=puntos[1][:199]
kappa=puntos[0][:199]
crosssection = np.loadtxt('plano650.txt') #masa,alpha,x


#plt.contour(x,b4,crosssection)
plt.scatter(hhH/2, kappa ,c=crosssection*1000)
#plt.xlim(250,100) #limites del eje x
#plt.ylim(0,1000) #limites del eje y
plt.title(r"$\sigma$(e+e-$\rightarrow$ hhZ)    $\sqrt{s}$ =650 GeV    Nivel Árbol"   ) #el titulo

plt.xlabel(r"$\lambda$$_{hhH}$")
plt.ylabel(r"$\kappa$$_{\lambda}$")

plt.colorbar(label="σ(fb)")
plt.savefig('planokap650.pdf')
plt.show()





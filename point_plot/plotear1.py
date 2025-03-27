import numpy as np
import matplotlib.pyplot as plt


puntos = np.loadtxt('comp.txt') #masa,alpha,x

x=puntos[1][:199]
b4=puntos[0][:199]
mH = np.loadtxt('mH.txt') #masa,alpha,x


#plt.contour(x,b4,crosssection)
plt.scatter(x, b4 ,c=mH)
#plt.xlim(250,100) #limites del eje x
#plt.ylim(0,1000) #limites del eje y
plt.title(r"mH"   ) #el titulo

plt.xlabel(r"$x$")
plt.ylabel(r"$b4$")

plt.colorbar(label="mH[GeV]")
plt.savefig('my_Figure_xb4_mH.pdf')
plt.show()





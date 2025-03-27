import numpy as np


#datos = np.loadtxt('DATAndrea.txt') #masa,alpha,x
#b4=datos[1][:200]
#x=datos[0][:200]



datos = np.loadtxt('DATAndrea.txt') #masa,alpha,x
b4=datos[1][:199]
x=datos[0][:199]
vS=x
msm=125
mh=125**2
v=246
vSM=v
lam = 0.18

a1 = -32000/x
b3 =-660*np.sqrt(b4)

mhp = 2*lam*v**2
ms = b3*x + 2*b4*x**2 -a1*v*v/(4*x)

a2 = (-2*np.sqrt(2*ms*lam*v**2 -2*mh*lam*v**2 + mh**2 - mh*ms)/v-a1)/(2*x)


mhs = v*(a1 + 2*a2*x)/2

mh2 =np.sqrt( (mhp + ms + np.abs(mhp-ms)*np.sqrt(1+((2*mhs)/(mhp-ms))**2))/2)

alpha =np.arccos(np.cos(np.arcsin((2*mhs)/(mh2**2-msm**2))/2 ))



K2=a2/2
LS=b4/4
K1=lam




c=np.cos(alpha)
s=np.sin(alpha)

acops = np.loadtxt('DATOS_acoplamientos.txt') #masa,alpha,x
hhhloop=acops[0][:199]
hhHloop=acops[1][:199]


ZH11=np.cos(alpha)
ZH12=np.sin(alpha)


hhh = ((2*b3+24*vS*LS)*ZH12*ZH12*ZH12+6*vSM*K1*ZH11*ZH11*ZH11+6*vSM*K2*ZH12*ZH12*ZH11+(3*a1/2+6*vS*K2)*ZH11*ZH11*ZH12)/(6*246)
hhH = (((a1+4*K2*vS)*ZH11*ZH11*ZH11+4*vSM*(2*K2-3*K1)*ZH11*ZH11*ZH12-2*(a1+4*K2*vS-2*b3-24*LS*vS)*ZH11*ZH12*ZH12-4*K2*vSM*ZH12*ZH12*ZH12))/(4*246)


kappaloop=hhhloop/(6*246*0.129)


def width(m,chhH,si):
    y = -6.45071195e-30 * m**12 +  4.39279827e-26 * m**11 + -1.33136302e-22 * m**10 +  2.36717022e-19 * m**9
    y += -2.73960711e-16 * m**8 +  2.16447509e-13 * m**7 + -1.19070417e-10 * m**6 +  4.56744299e-08 * m**5
    y += -1.20458265e-05 * m**4 +  2.11754572e-03 * m**3 + -2.34207440e-01 * m**2 +  1.45769348e+01 * m
    y += -3.85622510e+02
    
    mh2 = 125.09**2
    mH2 = m**2
    width=(chhH**2)*np.sqrt(1-4*mh2/mH2)/(8*np.pi*m)
    
    e = y*si**2 + width
    
    return e

anchura= width(mh2,hhH,s)

hhHloop2=hhHloop/(2*246)

#datos = np.transpose(np.column_stack((alpha.ravel(), mh2.ravel(), anchura.ravel(), K1.ravel(), K2.ravel(), LS.ravel(), a1.ravel(), b3.ravel())))

#datos=np.array([anchura])

datos = np.transpose(np.column_stack((hhHloop2.ravel())))



# Guardar los datos en un archivo de texto
np.savetxt('hhHloop.txt', datos)

#print(alpha)
#print(mh2)
#print(anchura)
#print(K1)
#print(K2)
#print(LS)
#print(a1)
#print(b3)

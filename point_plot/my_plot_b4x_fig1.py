import numpy as np
import matplotlib.pyplot as plt

# calculo de puntos en nuestro modelo

# inputs: mH, x, b4, b3, a1, a2, alphah
for point in ['1']:
      if point=='1':
    
    #masa Higgs pesado (singlete)
        mh2=461.9
    
    #vev del singlete
        vS=46.3
    
    #b4
        rLS=0.89/4
    
    #ángulo de mezcla
        alphaH=0.180
    
    #a1
        ra1=-691.1
    
    
    #a2
        rK2=4.50/2
    
    #b3
        rb3=-622.6

      if point=='2':
        mh2=470.8
        vS=46.3
        rLS=0.45/4
        alphaH=0.177
        ra1=-691.1
        rK2=4.45/2
        rb3=-442.7
    
    
      if point=='3':
        mh2=469.4
        vS=47.4
        rLS=0
        alphaH=0.174
        ra1=-675.1
        rK2=4.11/2
        rb3=0
        
    
      if point=='4':
        mh2=530.9
        vS=41.9
        rLS=0
        alphaH=0.153
        ra1=-763.7
        rK2=5.23/2
        rb3=0
        
    
      if point=='5':
        mh2=571.5
        vS=37.5
        rLS=0.78/4
        alphaH=0.140
        ra1=-853.3
        rK2=6.65/2
        rb3=-582.9
        
      if point=='6':
        mh2=529.6
        vS=40.8
        rLS=0.45/4
        alphaH=0.153
        ra1=-784.3
        rK2=5.63/2
        rb3=-442.7
    
      if point=='7':
        mh2=642.5
        vS=34.2
        rLS=0.11/4
        alphaH=0.125
        ra1=-935.7
        rK2=7.85/2
        rb3=-218.9
        
      if point=='8':
        mh2=656.1
        vS=33.1
        rLS=0.78/4
        alphaH=0.122
        ra1=-966.8
        rK2=8.44/2
        rb3=-582.9
#por constrains del modelo (se ven en Alain), el b4 va de 0.1 a 1 y el x va de 33 GeV a 48 GeV
n1=10
n2=20
b4=np.linspace(0.1,1,n1)
x=np.linspace(33,48,n2)
# outputs: lambdahhH, kappa, width,
# aqui, por comodidad, rellamo ra2=rK2, aunque en madgrpah se llama rK2
ra2=rK2
v=246
lambdaa=0.18
a1=-3200/x
b3=660*np.sqrt(b4)
mhp=np.sqrt(b3*c+2*b4*x**2-a1*v*v/(4*x))
mhbar=np.sqrt(2*lambdaa*v**2)
mh=125
a2=1/(2*x)*(-2/v*np.sqrt(2*mhp**2*lambdaa*v**2-2*mh*lambdaa*v**2+mh**4-mh**2*mhbar**2)-a1)
mhbarhp=np.sqrt(v/2*(a1*2*a2*x))
#mh=np.sqrt(1/2.*(mhbar**2+mhp**2-()*np.sqrt(1+2*mhbarhp/(mhbar**2-mhp**2))))

mH=np.sqrt(1/2.*(mhbar**2+mhp**2+np.abs(mhbar**2-mhp**2)*np.sqrt(1+2*mhbarhp**2/(mhbar**2-mhp**2))))

alpha=1/2*np.arcsin(2*mhbarhp**2*(mH**2-mh**2))
lhhHRxSM=(1/(4*v))*((a2+2*a2*x)*np.cos(alpha)**2+4*v*(a3-3*lambdaa)*np.cos(alpha)**2*np.sin(alpha)-2*(a1+2*a2*x-2*b3-6*b4*x)*np.cos(alpha)*np.sin(alpha)**2-2*a2*v*np.sin(alpha)**3)
lhhhRxSM=1*v*((a1/4+a2*x/2)*np.cos(alpha)**2*np.sin(alpha)+a2*v*np.cos(alpha)*np.sin(alpha)**2+(b3/2+b4*x)*np.sin(alpha)**3+lambdaa*v*np.cos(alpha)**3)
lhhhSM=0.129
kappa=lhhhRxSM/lhhhSM
width_H_hh=lhhHRxSM**2*np.sqrt(1-4*mh**2/mH**2)/(8*np.pi*mH)
#widthSM_H=...       (suma a todas las desintegraciones de H->ii)
#width_H=width_H_hh+np.sin(alpha)**2*widthSM_H

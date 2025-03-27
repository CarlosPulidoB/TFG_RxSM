import numpy as np
import matplotlib.pyplot as plt

# Definir los rangos de x y b4
n1 = 10  # Número de puntos en b4
n2 = 14  # Número de puntos en x
b4_values = np.linspace(0, 1, n1)
x_values = np.linspace(33, 47.33, n2)

# Crear malla
X, B4 = np.meshgrid(x_values, b4_values)


# Inicializar matrices para almacenar resultados
M_H = np.zeros_like(X)
KAPPA = np.zeros_like(X)
WIDTH_H = np.zeros_like(X)
LhhH = np.zeros_like(X)
ALPHA = np.zeros_like(X)
M_HNOTUSED = np.zeros_like(X)

#XS = {}  # Dictionary to store arrays dynamically
#xs = {}
#for i in range(5, 10): 
#    xs[f"xs_{i}00"] = np.loadtxt('/MG5_aMC_v3_5_7/Run_MadGraph_plane/xs_plane_zh1h1_'+{i}+'00.txt') #masa,alpha,x
 #   XS[f"XS_{i}00"] = np.zeros_like(X)


# Calcular los parámetros en cada punto de la malla
for i in range(n1):
    for j in range(n2):
        x = X[i, j]
        b4 = B4[i, j]

        # Plano de trabajo
        v = 246
        mh = 125.09  # Higgs ligero
        a1 = - 32000/x
        b3 =  - 560*np.sqrt(b4)
        lam = 0.18

        ms_2 = b3*x+2*b4*x**2-a1*v**2/(4*x)
        mhp_2 = 2*lam*v**2
        a2 = (1/(2*x))*(-2/v*np.sqrt(2*ms_2*lam*v**2-2*mh**2*lam*v**2+mh**4-mh**2*ms_2) - a1)
        mhps_2 =v/2*(a1+2*a2*x)

        mH = np.sqrt(0.5*(mhp_2+ms_2+(np.abs(mhp_2-ms_2))*np.sqrt(1+(2*mhps_2/(mhp_2-ms_2))**2)))

        # Apply the cut on mH
        if not (458 <= mH): # <= 670):
            M_HNOTUSED[i,j] = mH
            M_H[i, j] = np.nan  # Set to NaN so it's ignored in plots
            KAPPA[i, j] = np.nan
            WIDTH_H[i, j] = np.nan
            LhhH[i, j] = np.nan
            ALPHA[i, j] = np.nan
            #XS[i,j]= np.nan
            continue  # Skip the rest of the calculations
        #esto es un forma de hacerlo, hay otras formas de implementar este cut
        
        M_H[i, j] = mH  # Guardamos mH en la malla
#       for i in range(5, 10):
#            XS[f"XS_{i}00"][i,j] = xs[f"xs_{i}00"][i,j]#almaceno los valores para gráfica de crosssection tras pasar el filtro


        # Cálculo de otros parámetros
        alpha = np.arccos(np.cos(0.5*np.arcsin(2*mhps_2/(mH**2-mh**2))))
        ALPHA[i, j] = alpha

        lhhH = (1/(4*v))*((a1+2*a2*x)*np.cos(alpha)**3+4*v*(a2-3*lam)*np.cos(alpha)**2*np.sin(alpha)-
                2*(a1+2*a2*x-2*b3-6*b4*x)*np.cos(alpha)*np.sin(alpha)**2-2*a2*v*np.sin(alpha)**3)

        lhhhRxSM = 1/v*((a1/4+a2*x/2)*np.cos(alpha)**2*np.sin(alpha)+
                        a2*v/2*np.cos(alpha)*np.sin(alpha)**2+
                        (b3/3+b4*x)*np.sin(alpha)**3+
                        lam*v*np.cos(alpha)**3)

        lhhhSM = 0.129
        kappa = lhhhRxSM / lhhhSM
        KAPPA[i, j] = kappa  # Guardamos kappa

        LhhH[i,j]= lhhH

        # Cálculo comentado hasta su finalización
        #width_H_hh = lhhH**2 * np.sqrt(1 - 4 * mh**2 / mH**2) / (8 * np.pi * mH)

        def width(m,chhH,si):
            #estos acoplos que escribo ahora no son los buenos, estos son para un loop, debo buscar los buenos(y ponerlos en función de la masa o algo así)
            y = -6.45071195e-30 * m**12 +  4.39279827e-26 * m**11 + -1.33136302e-22 * m**10 +  2.36717022e-19 * m**9
            y += -2.73960711e-16 * m**8 +  2.16447509e-13 * m**7 + -1.19070417e-10 * m**6 +  4.56744299e-08 * m**5
            y += -1.20458265e-05 * m**4 +  2.11754572e-03 * m**3 + -2.34207440e-01 * m**2 +  1.45769348e+01 * m
            y += -3.85622510e+02
    
            mh_2 = 125.09**2
            mH_2 = m**2
            width=(chhH**2)*np.sqrt(1-4*mh_2/mH_2)/(8*np.pi*m)
    
            e = y*si**2 + width
    
            return e
        
        width_H= width(mH,lhhH,np.sin(alpha))

        WIDTH_H[i, j] = width_H  # Guardamos width_H_hh


# Graficar mH 
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X, B4, c=M_H, cmap='viridis')
#scatter = plt.scatter(X, B4, c=M_HNOTUSED, cmap='Reds')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$m_H$ (GeV)')
plt.xlabel(r'$x$ (GeV)')
plt.ylabel(r'$b_4$')
plt.title(r'Valores de $m_H$ (GeV) en función de $x$ y $b_4$')
plt.savefig('my_Figure_xb4_mH.pdf')
plt.show()

# Graficar mH en función de kappa y lhhH
plt.figure(figsize=(8, 6))
scatter = plt.scatter( LhhH,KAPPA, c=M_H, cmap='viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$m_H$ (GeV)')
plt.xlabel(r'$\lambda_{hhH}$')
plt.ylabel(r'$\kappa_\lambda$')
plt.title(r'$m_H$ en función de $\kappa_\lambda$ y $lhhH$')
plt.savefig('my_Figure_lhhHkappa_mH.pdf')
plt.show()

# Graficar kappa
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X, B4, c=KAPPA, cmap='viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$\kappa_\lambda$')
plt.xlabel(r'$x$ (GeV)')
plt.ylabel(r'$b_4$')
plt.title(r'Valores de $\kappa$ en función de $x$ y $b_4$')
plt.savefig('my_Figure_xb4_kappa.pdf')
plt.show()

# Graficar lhhH
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X, B4, c=LhhH, cmap='viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$\lambda_{hhH}$')
plt.xlabel(r'$x$ (GeV)')
plt.ylabel(r'$b_4$')
plt.title(r'Valores de $lhhH$ en función de $x$ y $b_4$')
plt.savefig('my_Figure_xb4_lhhH.pdf')
plt.show()


# Graficar WIDTH_H en función de x y b4
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X, B4, c=WIDTH_H, cmap='viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$\Gamma_H$')
plt.xlabel(r'$x$ (GeV)')
plt.ylabel(r'$b_4$')
plt.title(r'$\Gamma(H \to hh)$ en función de $x$ y $b_4$')
plt.savefig('my_Figure_xb4_Gamma.pdf')
plt.show()

# Graficar alpha en función de x y b4
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X, B4, c=ALPHA, cmap='viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$\alpha$')
plt.xlabel(r'$x$ (GeV)')
plt.ylabel(r'$b_4$')
plt.title(r'$\alpha$ en función de $x$ y $b_4$')
plt.savefig('my_Figure_xb4_alpha.pdf')
plt.show()

# Graficar alpha en función de kappa y lhhH
plt.figure(figsize=(8, 6))
scatter = plt.scatter( LhhH,KAPPA, c=ALPHA, cmap='viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(r'$\alpha$')
plt.xlabel(r'$\lambda_{hhH}$')
plt.ylabel(r'$\kappa_\lambda$')
plt.title(r'$\alpha$ en función de $\kappa_\lambda$ y $lhhH$')
plt.savefig('my_Figure_lhhHkappa_alpha.pdf')
plt.show()
'''
for i in range(5, 10):
    # Graficar xs en función de x y b4
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X, B4, c=XS[f"XS_{i}00"], cmap='viridis')
    cbar = plt.colorbar(scatter)
    cbar.set_label(r'$\sigma(fb)$') #revisar si estas unidades están bien
    plt.xlabel(r'$x$ (GeV)')
    plt.ylabel(r'$b_4$')
    plt.title(r'Nivel árbol $\sigma(e^xe^-\rightarrow Zhh) \sqrt(s)='+{i}+'00 GeV$')
    plt.savefig('my_Figure_xb4_xs_zh1h1.pdf')
    plt.show()

    # Graficar xs en función de kappa y lhhH
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter( LhhH,KAPPA, c=XS[f"XS_{i}00"], cmap='viridis')
    cbar = plt.colorbar(scatter)
    cbar.set_label(r'$\sigma(fb)$') #revisar si estas unidades están bien
    plt.xlabel(r'$\lambda_{hhH}$')
    plt.ylabel(r'$\kappa_\lambda$')
    plt.title(r'Nivel árbol $\sigma(e^xe^-\rightarrow Zhh) \sqrt(s)='+{i}+'00 GeV')
    plt.savefig('my_Figure_lhhHkappa_xs_zh1h1.pdf')
    plt.show()
'''
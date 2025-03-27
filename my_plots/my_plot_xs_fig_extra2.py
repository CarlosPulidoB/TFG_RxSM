import numpy as np
import matplotlib.pyplot as plt



data1 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlh_2.txt")#, skiprows=1)
#es la segunda toma de datos, donde se ha calculado para los mismos puntos que la pol

# Extract X and Y columns
y1 = 1000*data1[:, 0]  # First column
x1 = 2*data1[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data2 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zh_2.txt")#, skiprows=1)
#es la segunda toma de datos, donde se ha calculado para los mismos puntos que la pol

# Extract X and Y columns
y2 = 1000*data2[:, 0]  # First column
x2 = 2*data2[:, 1]  # Second column

# Extract X and Y columns
y2 = 1000*data2[:, 0]  # First column
x2 = 2*data2[:, 1]  # Second column

data1p = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y1p = 1000*data1p[:, 0]  # First column
x1p = 2*data1p[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data2p = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y2p = 1000*data2p[:, 0]  # First column
x2p = 2*data2p[:, 1]  # Second column

aux2=y2p/y2
aux1=y1p/y1

# Set log scale on the y-axis
#plt.yscale('log')

# Set x-axis range
plt.xlim(0, 3000)
# Set y-axis range
plt.ylim(1, 3)

# Activar las marcas en la parte superior y derecha
plt.tick_params(top=True, right=True)  # Activa las marcas en la parte superior y derecha

## Plot the data
#plt.plot(x2, aux2, linestyle='-', color='b', label='zh')#marker='o' 
#plt.plot(x1, aux1, linestyle='-', color='r', label=r'$\nu\nu$h')#marker='o'
##plt.plot(x1p, y1p, linestyle='--', color='r', label=r'$\nu\nu$h (pol. 30%/-80%)')#marker='o'

# Plot the data as points instead of lines
plt.scatter(x2, aux2, color='b', label='zh', marker='o',s=10)  
plt.scatter(x1, aux1, color='r', label=r'$\nu\nu$h', marker='o',s=10)  

##### Las SM están medidas con polarización de los beam:
#   30.0	= polbeam1 ! beam polarization for beam 1
#   -80.0	= polbeam2 ! beam polarization for beam 2

# Labels and title
plt.title(r'Cross Section $\sigma_{pol}$/$\sigma_{unpol}$ vs $\sqrt{s}$')
plt.xlabel(r'$\sqrt{s}$ (GeV)')
plt.ylabel(r'$\sigma_{pol}$/$\sigma_{unpol}$')

#plt.legend(frameon=False)
plt.legend()  # Moves legend outside on the right


# Show the plot
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Load data (adjust delimiter if needed: space, comma, or tab)
data1 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh_onlyW.txt")#, skiprows=1)

# Extract X and Y columns
y1 = 1000*data1[:, 0]  # First column #multiplicado por 1000 por unidades, para que quede en fb
x1 = 2*data1[:, 1]  # Second column #multiplicado por 2 porque esa columna es el beam, y la sqrt(s) aquí es el doble de eso

# Load data (adjust delimiter if needed: space, comma, or tab)
data2 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh_onlyZ.txt")#, skiprows=1)

# Extract X and Y columns
y2 = 1000*data2[:, 0]  # First column
x2 = 2*data2[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data2e = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vevehh_onlyZ.txt")#, skiprows=1)

# Extract X and Y columns
y2e = 1000*data2e[:, 0]  # First column
x2e = 2*data2e[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data3 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh.txt")#, skiprows=1)

# Extract X and Y columns
y3 = 1000*data3[:, 0]  # First column
x3 = 2*data3[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data3e = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vevehh.txt")#, skiprows=1)

# Extract X and Y columns
y3e = 1000*data3e[:, 0]  # First column
x3e = 2*data3e[:, 1]  # Second column


# Set log scale on the y-axis
plt.yscale('log')

# Set x-axis range
plt.xlim(0, 3000)
# Set y-axis range
plt.ylim(5*10**(-6), 1*10**0)

# Plot the data
plt.plot(x1, y1, linestyle='--', color='b', label=r'$\nu_e\nu_e$hh (only W)')#marker='o' 
plt.plot(x2, y2, linestyle='-', color='g', label=r'$\nu\nu$hh (only Z)')#marker='o'
plt.plot(x2e, y2e, linestyle='--', color='m', label=r'$\nu_e\nu_e$hh (only Z)')#marker='o'
plt.plot(x3, y3, linestyle='-', color='r', label=r'$\nu\nu$hh')#marker='o'
plt.plot(x3e, y3e, linestyle='--', color='k', label=r'$\nu_e\nu_e$hh')#marker='o'


 

# Labels and title
plt.title(r'Cross Section $\sigma$ (fb) vs $\sqrt{s}$ (GeV)')
plt.xlabel(r'$\sqrt{s}$ (GeV)')
plt.ylabel(r'Cross Section $\sigma$ (fb)')

plt.legend()

# Show the plot
plt.show()
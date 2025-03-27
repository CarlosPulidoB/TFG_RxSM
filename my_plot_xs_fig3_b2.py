import numpy as np
import matplotlib.pyplot as plt

#como fig2, pero RxSM in alignment limit (angulo de mezcla=0)

#hvlvl

# Load data (adjust delimiter if needed: space, comma, or tab)
data_a = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_zh1h1_RxSM.txt")#, skiprows=1)

# Extract X and Y columns
y_a = 1000*data_a[:, 0]  # First column #multiplicado por 1000 por unidades, para que quede en fb
x_a = 2*data_a[:, 1]  # Second column #multiplicado por 2 porque esa columna es el beam, y la sqrt(s) aquí es el doble de eso


#vlvlhh


# Load data (adjust delimiter if needed: space, comma, or tab)
data3 = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1h1_RxSM.txt")#, skiprows=1)

# Extract X and Y columns
y3 = 1000*data3[:, 0]  # First column
x3 = 2*data3[:, 1]  # Second column


#hz

# Load data (adjust delimiter if needed: space, comma, or tab)
data4e = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_zh1_RxSM.txt")#, skiprows=1)

# Extract X and Y columns
y4e = 1000*data4e[:, 0]  # First column
x4e = 2*data4e[:, 1]  # Second column


#hvlvl


# Load data (adjust delimiter if needed: space, comma, or tab)
data5e_2 = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1_RxSM.txt")#, skiprows=1)

# Extract X and Y columns
y5e_2 = 1000*data5e_2[:, 0]  # First column
x5e_2 = 2*data5e_2[:, 1]  # Second column



# Set log scale on the y-axis
plt.yscale('log')

# Set x-axis range
plt.xlim(0, 3000)
# Set y-axis range
plt.ylim(5*10**(-5), 5*10**3)

# Plot the data
plt.plot(x_a, y_a, linestyle='--', color='orange', label=r'zhh (RxSM)')#marker='o'

plt.plot(x4e, y4e, linestyle='--', color='g', label=r'zh (RxSM)')#marker='o'

plt.plot(x5e_2, y5e_2, linestyle='--', color='b', label=r'$\nu\nu$h (RxSM)')#marker='o'

plt.plot(x3, y3, linestyle='--', color='r', label=r'$\nu\nu$hh (RxSM)')#marker='o'





 

# Labels and title
plt.title(r'RxSM Cross Section $\sigma$ [fb] vs $\sqrt{s}$ [GeV]')
plt.xlabel(r'$\sqrt{s}$ [GeV]')
plt.ylabel(r'Cross Section $\sigma$ [fb]')

#plt.legend(frameon=False)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Moves legend outside on the right
plt.tight_layout()  # Prevents the figure from cutting off the legend

# Show the plot
plt.show()
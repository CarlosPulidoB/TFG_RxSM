import numpy as np
import matplotlib.pyplot as plt

#como fig2, pero RxSM in alignment limit (angulo de mezcla=0)



# Load data (adjust delimiter if needed: space, comma, or tab)
data1 = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1h1_RxSM.txt")#, skiprows=1)

# Extract X and Y columns
y1 = 1000*data1[:, 0]  # First column
x1 = 2*data1[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data1SM = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh.txt")#, skiprows=1)

# Extract X and Y columns
y1SM = 1000*data1SM[:, 0]  # First column
x1SM = 2*data1SM[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data1e = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1h1_RxSM_align_onlyZ.txt")#, skiprows=1)

# Extract X and Y columns
y1e = 1000*data1e[:, 0]  # First column
x1e = 2*data1e[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data1eSM = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh_onlyZ.txt")#, skiprows=1)

# Extract X and Y columns
y1eSM = 1000*data1eSM[:, 0]  # First column
x1eSM = 2*data1eSM[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data2e = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1h1_RxSM_align_onlyW.txt")#, skiprows=1)

# Extract X and Y columns
y2e = 1000*data2e[:, 0]  # First column
x2e = 2*data2e[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data2eSM = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh_onlyW.txt")#, skiprows=1)

# Extract X and Y columns
y2eSM = 1000*data2eSM[:, 0]  # First column
x2eSM = 2*data2eSM[:, 1]  # Second column




# Set log scale on the y-axis
plt.yscale('log')

# Set x-axis range
plt.xlim(600, 3000)
# Set y-axis range
plt.ylim(5*10**(-3), 5*10**3)

# Plot the data
plt.plot(x1SM, y1SM, linestyle='-', color='g', label=r'$\nu\nu$hh (SM)')#marker='o'
plt.plot(x1, y1, linestyle='--', color='b', label=r'$\nu\nu$hh (align. lim.)')#marker='o' 
plt.plot(x1eSM, y1eSM, linestyle='-', color='y', label=r'$\nu\nu$hh (only Z) (SM)')#marker='o'
plt.plot(x1e, y1e, linestyle='--', color='m', label=r'$\nu\nu$hh (only Z) (align. lim.)')#marker='o'
plt.plot(x2eSM, y2eSM, linestyle='-', color='y', label=r'$\nu\nu$hh (only W) (SM)')#marker='o'
plt.plot(x2e, y2e, linestyle='--', color='b', label=r'$\nu\nu$hh (only W) (align. lim.)')#marker='o'

### lo tengo con alignment. Voy a mirarlo así primero para ver que va bien, pero despues me quedo
### con esta figura quitando los alignments

 
# Labels and title
plt.title(r'RxSM Cross Section $\sigma$ [fb] vs $\sqrt{s}$ [GeV] $\nu\nu$hh in alignment limit')
plt.xlabel(r'$\sqrt{s}$ [GeV]')
plt.ylabel(r'Cross Section $\sigma$ [fb]')

#plt.legend(frameon=False)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Moves legend outside on the right
plt.tight_layout()  # Prevents the figure from cutting off the legend

# Show the plot
plt.show()
import numpy as np
import matplotlib.pyplot as plt

#como fig2, pero RxSM in alignment limit (angulo de mezcla=0)

#hvlvl

# Load data (adjust delimiter if needed: space, comma, or tab)
#data_b = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_zh1h1_RxSM_align.txt")#, skiprows=1)

# Extract X and Y columns
#y_b = 1000*data_b[:, 0]  # First column
#x_b = 2*data_b[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data_c = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zhh.txt")#, skiprows=1)

# Extract X and Y columns
y_c = 1000*data_c[:, 0]  # First column
x_c = 2*data_c[:, 1]  # Second column

#vlvlhh


# Load data (adjust delimiter if needed: space, comma, or tab)
#data3_al = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1h1_RxSM_align.txt")#, skiprows=1)

# Extract X and Y columns
#y3_al = 1000*data3_al[:, 0]  # First column
#x3_al = 2*data3_al[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data3SM = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh.txt")#, skiprows=1)

# Extract X and Y columns
y3SM = 1000*data3SM[:, 0]  # First column
x3SM = 2*data3SM[:, 1]  # Second column


#hz


# Load data (adjust delimiter if needed: space, comma, or tab)
data4e_2 = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_zh1_RxSM_align.txt")#, skiprows=1)

# Extract X and Y columns
y4e_2 = 1000*data4e_2[:, 0]  # First column
x4e_2 = 2*data4e_2[:, 1]  # Second column


# Load data (adjust delimiter if needed: space, comma, or tab)
data4eSM = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zh_2.txt")#, skiprows=1)

# Extract X and Y columns
y4eSM = 1000*data4eSM[:, 0]  # First column
x4eSM = 2*data4eSM[:, 1]  # Second column

#hvlvl

# Load data (adjust delimiter if needed: space, comma, or tab)
data5e = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1_RxSM_align.txt")#, skiprows=1)

# Extract X and Y columns
y5e = 1000*data5e[:, 0]  # First column
x5e = 2*data5e[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data5ez = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1_onlyZ_RxSM_align.txt")#, skiprows=1)

# Extract X and Y columns
y5ez = 1000*data5ez[:, 0]  # First column
x5ez = 2*data5ez[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data5ew = np.loadtxt("my_xs_rs_ee_txt/xs_RxSM_txt/xs_rs_ee_vlvlh1_onlyW_RxSM_align.txt")#, skiprows=1)

# Extract X and Y columns
y5ew = 1000*data5ew[:, 0]  # First column
x5ew = 2*data5ew[:, 1]  # Second column


# Load data (adjust delimiter if needed: space, comma, or tab)
data5eSM = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlh_2.txt")#, skiprows=1)

# Extract X and Y columns
y5eSM = 1000*data5eSM[:, 0]  # First column
x5eSM = 2*data5eSM[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data5eSMz = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlh_onlyZ.txt")#, skiprows=1)

# Extract X and Y columns
y5eSMz = 1000*data5eSMz[:, 0]  # First column
x5eSMz = 2*data5eSMz[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data5eSMw = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlh_onlyW.txt")#, skiprows=1)

# Extract X and Y columns
y5eSMw = 1000*data5eSMw[:, 0]  # First column
x5eSMw= 2*data5eSMw[:, 1]  # Second column


# Set log scale on the y-axis
plt.yscale('log')

# Set x-axis range
plt.xlim(0, 3000)
# Set y-axis range
plt.ylim(5*10**(-5), 5*10**3)

# Plot the data
#plt.plot(x_c, y_c, linestyle='--', color='y', label=r'zhh (SM)')#marker='o'
#plt.plot(x_b, y_b, linestyle='--', color='g', label=r'zhh (align. lim.)')# align. limit

plt.plot(x4eSM, y4eSM, linestyle='-', color='y', label=r'zh (SM)')#marker='o'
plt.plot(x4e_2, y4e_2, linestyle='--', color='k', label=r'zh (align. lim.)')# align. limit

plt.plot(x5eSM, y5eSM, linestyle='-', color='y', label=r'$\nu\nu$h (SM)')#marker='o'
plt.plot(x5e, y5e, linestyle='--', color='purple', label=r'$\nu\nu$h (align. lim.)')# align. limit

plt.plot(x5eSMz, y5eSMz, linestyle='-', color='y', label=r'$\nu\nu$h (only Z) (SM)')#marker='o'
plt.plot(x5ez, y5ez, linestyle='--', color='r', label=r'$\nu\nu$h (only Z) (align. lim.)')# align. limit

plt.plot(x5eSMw, y5eSMw, linestyle='-', color='y', label=r'$\nu\nu$h (only W) (SM)')#marker='o'
plt.plot(x5ew, y5ew, linestyle='--', color='b', label=r'$\nu\nu$h (ony W) (align. lim.)')# align. limit

#plt.plot(x3SM, y3SM, linestyle='-', color='y', label=r'$\nu\nu$hh (SM)')#marker='o'
#plt.plot(x3_al, y3_al, linestyle='--', color='b', label=r'$\nu\nu$hh (align. lim.)')#marker='o'





 

# Labels and title
plt.title(r'RxSM Cross Section $\sigma$ [fb] vs $\sqrt{s}$ [GeV] in alingment limit')
plt.xlabel(r'$\sqrt{s}$ [GeV]')
plt.ylabel(r'Cross Section $\sigma$ [fb]')

plt.legend() #frameon=False
#plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Moves legend outside on the right
plt.tight_layout()  # Prevents the figure from cutting off the legend

# Show the plot
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Load data (adjust delimiter if needed: space, comma, or tab)
data = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zhh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y = 1000*data[:, 0]  # First column
x = 2*data[:, 1]  # Second column


# Load data (adjust delimiter if needed: space, comma, or tab)
data2e = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vevehh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y2e = 1000*data2e[:, 0]  # First column
x2e = 2*data2e[:, 1]  # Second column

data3e = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_veveh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y3e = 1000*data3e[:, 0]  # First column
x3e = 2*data3e[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data4 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y4 = 1000*data4[:, 0]  # First column
x4 = 2*data4[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data5 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_eeh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y5 = 1000*data5[:, 0]  # First column
x5 = 2*data5[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data6 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_eehh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y6 = 1000*data6[:, 0]  # First column
x6 = 2*data6[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data7 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_tth_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y7 = 1000*data7[:, 0]  # First column
x7 = 2*data7[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data8 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_tthh_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
y8 = 1000*data8[:, 0]  # First column
x8 = 2*data8[:, 1]  # Second column


# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM = np.loadtxt("my_xs_txt/xs_ee_SM_pol30:-80/ee_zhh_xs_SM_pol30:-80.txt")#, skiprows=1)
dataSM = np.loadtxt("xs_ee_SM_pol30:-80/ee_cross_section_SM_pol30:-80.txt")#, skiprows=1)
xSM = 2*np.linspace(0,600,200)  # Second column

# Extract X and Y columns
ySM1 = dataSM[0, :]  #zhh
ySM2 = dataSM[1, :]  #zhh
ySM3 = dataSM[2, :]  #zhh
ySM4 = dataSM[3, :]  #zhh
ySM5 = dataSM[4, :]  #zhh
ySM6 = dataSM[5, :]  #zhh
ySM7 = dataSM[6, :]  #zhh
ySM8 = dataSM[7, :]  #zhh

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM2 = np.loadtxt("xs_ee_SM_pol30:-80/ee_vlvlhh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM2 = dataSM2  # First column

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM4 = np.loadtxt("xs_ee_SM_pol30:-80/ee_vlvlh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM4 = dataSM4  # First column

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM3 = np.loadtxt("xs_ee_SM_pol30:-80/ee_zh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM3 = dataSM3  # First column

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM5 = np.loadtxt("xs_ee_SM_pol30:-80/ee_eeh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM5 = dataSM5  # First column

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM6 = np.loadtxt("xs_ee_SM_pol30:-80/ee_eehh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM6 = dataSM6  # First column

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM7 = np.loadtxt("xs_ee_SM_pol30:-80/ee_tth_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM7 = dataSM7  # First column

# Load data (adjust delimiter if needed: space, comma, or tab)
#dataSM8 = np.loadtxt("xs_ee_SM_pol30:-80/ee_tthh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
#ySM8 = dataSM8  # First column


# Set log scale on the y-axis
plt.yscale('log')

# Set x-axis range
#plt.xlim(0, 3000)
# Set y-axis range
#plt.ylim(10**(-5), 10**3)

# Set x-axis range
plt.xlim(0, 1200)
# Set y-axis range
plt.ylim(5.0*10**-5, 1.5*10**3)

# Plot the data
plt.plot(x, y, linestyle='-', color='b', label='zhh')#marker='o' 
plt.plot(x2e, y2e, linestyle='-', color='r', label=r'$\nu_e\nu_e$hh')#marker='o'
plt.plot(x3e, y3e, linestyle='-', color='g', label=r'$\nu_e\nu_e$h')#marker='o'
plt.plot(x4, y4, linestyle='-', color='k', label=r'zh')#marker='o' 
plt.plot(x5, y5, linestyle='-', color='purple', label=r'eeh')#marker='o' 
plt.plot(x6, y6, linestyle='-', color='brown', label=r'eehh')#marker='o' 
plt.plot(x7, y7, linestyle='-', color='m', label=r'tth')#marker='o' 
plt.plot(x8, y8, linestyle='-', color='c', label=r'tthh')#marker='o' 

# Plot the data SM
#pongo SM en el anterior ya que pongo las lineas iguales i así el SM engloba a todo
plt.plot(xSM, ySM1, linestyle='--', color='y', label=r'SM')
plt.plot(xSM, ySM2, linestyle='--', color='y')
plt.plot(xSM, ySM3, linestyle='--', color='y')
plt.plot(xSM, ySM4, linestyle='--', color='y')
plt.plot(xSM, ySM5, linestyle='--', color='y')
plt.plot(xSM, ySM6, linestyle='--', color='y')
plt.plot(xSM, ySM7, linestyle='--', color='y')
plt.plot(xSM, ySM8, linestyle='--', color='y')

##### Las SM están medidas con polarización de los beam:
#   30.0	= polbeam1 ! beam polarization for beam 1
#   -80.0	= polbeam2 ! beam polarization for beam 2

# Labels and title
plt.title(r'Cross Section $\sigma$ vs $\sqrt{s}$ (polarization 30%/-80%)')
plt.xlabel(r'$\sqrt{s}$ (GeV)')
plt.ylabel(r'Cross Section $\sigma$ (fb)')

#plt.legend(frameon=False)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Moves legend outside on the right
plt.tight_layout()  # Prevents the figure from cutting off the legend


# Show the plot
plt.show()
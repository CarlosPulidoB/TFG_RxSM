import numpy as np
import matplotlib.pyplot as plt

# Load data (adjust delimiter if needed: space, comma, or tab)
data = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zhh.txt")#, skiprows=1)

# Extract X and Y columns
y = 1000*data[:, 0]  # First column
x = 2*data[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data2 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlhh.txt")#, skiprows=1)

# Extract X and Y columns
y2 = 1000*data2[:, 0]  # First column
x2 = 2*data2[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data3 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_vlvlh.txt")#, skiprows=1)

# Extract X and Y columns
y3 = 1000*data3[:, 0]  # First column
x3 = 2*data3[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data4 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_zh.txt")#, skiprows=1)

# Extract X and Y columns
y4 = 1000*data4[:, 0]  # First column
x4 = 2*data4[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
data5 = np.loadtxt("my_xs_rs_ee_txt/xs_SM_txt/xs_ee_tth_modified.txt")#, skiprows=1)

# Extract X and Y columns
y5 = 1000*data5[:, 0]  # First column
x5 = 2*data5[:, 1]  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
dataSM = np.loadtxt("xs_ee_SM_pol30:-80/zhh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
ySM = dataSM  # First column
xSM = 2*np.linspace(0,600,200)  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
dataSM2 = np.loadtxt("xs_ee_SM_pol30:-80/vlvlhh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
ySM2 = dataSM2  # First column
xSM2 = 2*np.linspace(0,600,200)  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
dataSM3 = np.loadtxt("xs_ee_SM_pol30:-80/vlvlh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
ySM3 = dataSM3  # First column
xSM3 = 2*np.linspace(0,600,200)  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
dataSM4 = np.loadtxt("xs_ee_SM_pol30:-80/zh_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
ySM4 = dataSM4  # First column
xSM4 = 2*np.linspace(0,600,200)  # Second column

# Load data (adjust delimiter if needed: space, comma, or tab)
dataSM5 = np.loadtxt("xs_ee_SM_pol30:-80/tth_cross_section_SM_pol30:-80.txt")#, skiprows=1)

# Extract X and Y columns
ySM5 = dataSM5  # First column
xSM5 = 2*np.linspace(0,600,200)  # Second column


# Set log scale on the y-axis
plt.yscale('log')

# Set x-axis range
#plt.xlim(0, 3000)
# Set y-axis range
#plt.ylim(10**(-5), 10**3)

# Set x-axis range
plt.xlim(0, 1200)
# Set y-axis range
plt.ylim(0.005, 1.5*10**3)

# Plot the data
plt.plot(x4, y4, linestyle='-', color='k', label=r'zh')#marker='o' 
plt.plot(x, y, linestyle='-', color='b', label='zhh')#marker='o' 
plt.plot(x3, y3, linestyle='-', color='g', label=r'$\nu\nu$h')#marker='o'
plt.plot(x2, y2, linestyle='-', color='r', label=r'$\nu\nu$hh')#marker='o'
plt.plot(x5, y5, linestyle='-', color='orange', label='tth')#marker='o'

# Plot the data
plt.plot(xSM, ySM4, linestyle='--', color='y', label=r'zh')#marker='o' 
plt.plot(xSM, ySM, linestyle='--', color='y', label='zhh')#marker='o' 
plt.plot(xSM, ySM3, linestyle='--', color='y', label=r'$\nu\nu$h')#marker='o'
plt.plot(xSM, ySM2, linestyle='--', color='y', label=r'$\nu\nu$hh')#marker='o'
plt.plot(xSM, ySM5, linestyle='--', color='y', label='tth')#marker='o'

##### Las SM están medidas con polarización de los beam:
#   30.0	= polbeam1 ! beam polarization for beam 1
#   -80.0	= polbeam2 ! beam polarization for beam 2

# Labels and title
plt.title(r'Cross Section $\sigma$ (fb) vs $\sqrt{s}$ (GeV)')
plt.xlabel(r'$\sqrt{s}$ (GeV)')
plt.ylabel(r'Cross Section $\sigma$ (fb)')

plt.legend()

# Show the plot
plt.show()
from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from t2data import *
from mpl_toolkits.mplot3d import Axes3D

liquid_density_kgPm3=1000
water_molecular_weight=0.018
kpaPpa=1.e-3
R_value=8.3145
mPmm=1.e-3
dayPs=1./(3600*24)
T_kelven=273.15

# --- post-process the output ---------------------------
lst = t2listing(dat.title+'.listing')


connection_direction         = np.array([blk.direction for blk in dat.grid.connectionlist])
# element_volume_m3            = np.array([blk.volume for blk in dat.grid.blocklist[:-nblks_z-nblks_z+4]])
# element_coordinate           = np.array([j.centre for j in dat.grid.blocklist[:-nblks_z-nblks_z+4]])      
element_coordinate           = np.array([j.centre for j in dat.grid.blocklist])                                                                        
element_value_x              = element_coordinate[:,0]
element_value_y              = element_coordinate[:,1]
element_value_z              = element_coordinate[:,2]

# gas_saturation               = np.array([lst.history(('e',lst.element.row_name[i],'SG'))[1] for i in range(lst.element.num_rows)])
liq_saturation               = np.array([lst.history(('e',lst.element.row_name[i],'SL'))[1] for i in range(lst.element.num_rows)])
# salt_saturation              = np.array([lst.history(('e',lst.element.row_name[i],'SS'))[1] for i in range(lst.element.num_rows)])
# gas_pressure_pa              = np.array([lst.history(('e',lst.element.row_name[i],'P'))[1] for i in range(lst.element.num_rows)])
# capillary_pressure_pa        = np.array([lst.history(('e',lst.element.row_name[i],'PCAP'))[1] for i in range(lst.element.num_rows)])
# temperature_degree           = np.array([lst.history(('e',lst.element.row_name[i],'T'))[1] for i in range(lst.element.num_rows)])
salt_mass_fraction_in_liquid = np.array([lst.history(('e',lst.element.row_name[i],'XNACL'))[1] for i in range(lst.element.num_rows)])
# K_red                        = np.array([lst.history(('e',lst.element.row_name[i],'K-RED'))[1] for i in range(lst.element.num_rows)])
# liq_density_kgPm3            = np.array([lst.history(('e',lst.element.row_name[i],'DL'))[1] for i in range(lst.element.num_rows)])
 
# liquid_flow_kgPs             = -1*np.array([lst.history(('c',lst.connection.row_name[i],'FLO(LIQ.)'))[1] for i in range(lst.connection.num_rows)])
# liquid_flow_mmPday           = liquid_flow_kgPs/dat.grid.connectionlist[0].area/liquid_density_kgPm3/mPmm/dayPs
# liquid_flow_mmPday_x         = liquid_flow_mmPday[connection_direction==1]
# liquid_flow_mmPday_z         = liquid_flow_mmPday[connection_direction==3]
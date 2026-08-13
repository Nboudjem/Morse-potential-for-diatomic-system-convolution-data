# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:03:57 2019

@author: nboudjem ## PES HBr molecule

"""

import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt


h = 1
h_bar=1
w_0 = 79.41
delta = 1.5
m_H  = 1.00794
m_Br = 79.904
u = (m_H * m_Br)/(m_Br+m_H)
x = h_bar/(u*w_0)
a_0 = np.sqrt(x)
F_fo = 9
r_0 = 1.41

u_f=3236.5

u_f_1=3231+3.762 # 3234.72
u_f_2=3230.54+3.762 # 3234.302 
u_f_3=3230.77+3.762 # 3234.532

u_f_expts = 3236.5

#the ground state vibrational HBr wavefunction

def psi_u(r):
    return (1/(np.pi*a_0**2))**(1/4)*np.exp(-0.5*((r-r_0)/a_0)**2)



#Potential energy curve using an exponential shape

def f(r,du_f,u_f):
        return du_f*np.exp(-(F_fo/du_f)*(r-r_0))+u_f
    
# HBr 2p^-2 sigma* experimental potential
    
def u_f_expt(r):
    return u_f_expts*r/r


#Computations 
    
r = np.arange(0., 6, 0.01)
 
du_f_1=1.73
du_f_2=2.19
du_f=1.96
du_f_4=2.19-1.96

out_file = input("\nEnter output file name: ")
out_file = out_file.strip()    
#Write to file
ofl = open(out_file,"w")
for i in range(len(f(r,du_f,u_f))):
    #ofl.write(str(r[i])+","+str(psi_u(r)[i])+"\n")
    ofl.write(str(r[i])+","+str(f(r,du_f,u_f)[i])+"\n")
    #ofl.write(str(r[i])+","+str(f(r,du_f_3)[i])+"\n")
ofl.close()
print("Output written to file: ",out_file)

error = f(r,du_f,u_f)-f(r,du_f_1,u_f_1)

#data = loadtxt('slope.txt')
#d = data[:, 0]
#t = data[:, 1]
#k = data[:, 2]
#j = data[:, 3]
#l = data[:, 4]
#m = data[:, 5]

#Display/plots


fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('H-Br distance ($\AA$) ',fontsize=16)
ax1.set_ylabel('Binding energy (eV)', color = color,fontsize=16)

ax1.plot(r,u_f_expt(r),'--g',linewidth=3)
plt.text(1.9, 3237,'Br $2p^{-2}\sigma^*$',fontsize=16)
plt.text(2.2, 3246,'HBr',fontsize=20)
plt.text(1.35, 3232,'FC',fontsize=20)
plt.errorbar(r, f(r,du_f_1,u_f_1), yerr=error, fmt='o', color='red')
#plt.plot(d,t,'--r',linewidth=3)
#plt.plot(k,j,'--k',linewidth=3)
#plt.plot(l,m,'--k',linewidth=3)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 
color = 'tab:blue'
ax2.set_ylabel('FWHM=FC_zone', color = color,fontsize=16)
ax2.plot(r,psi_u(r),'-*', color = color,linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)
ax1.set_xlim([0.6,2.5])
ax1.set_ylim([3231,3248])
ax1.tick_params(direction='in',width=2)
ax2.tick_params(direction='in',width=2)
for axis in ['top','bottom','left','right']:
  ax1.spines[axis].set_linewidth(2)

fig.tight_layout()
plt.savefig('PES.pdf')
plt.show()
       


    
    
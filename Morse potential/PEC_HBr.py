# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:33:45 2020

@author: nboudjem
"""


import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
from scipy.constants import h, c
from morse import Morse, FAC
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 14})
rc('text', usetex=True)

COLOUR1 = (0.6196, 0.0039, 0.2588, 1.0)

# Atom masses and equilibrium bond length for (1H)(35Cl).
mA, mB = 1., 79.90
X_re = 1.41443e-10
X_Te = 0
X_we, X_wexe = 2648.975, 45.217

X = Morse(mA, mB, X_we, X_wexe, X_re, X_Te)
r=X.make_rgrid()
X.V = X.Vmorse(X.r)

E1 = X.Emorse(0)
E2 = X.Emorse(2)
E3 = X.Emorse(3)
E4 = X.Emorse(4)
E5 = X.Emorse(5)
E6 = X.Emorse(6)
E7 = X.Emorse(7)
E8 = X.Emorse(8)

psi = X.calc_psi(0)

out_file = input("\nEnter output file name: ")
out_file = out_file.strip()    
#Write to file
ofl = open(out_file,"w")
for i in range(len(psi)):
    ofl.write(str(r[i])+","+str(psi[i])+"\n")
ofl.close()
print("Output written to file: ",out_file)




fig, ax = plt.subplots()
X.plot_V(ax, color='k')

#X.draw_Elines(range(X.vmax), ax)
#X.draw_Elines(X.get_vmax(), ax, linestyles='--', linewidths=1)

X.plot_psi([10, 15], ax, scaling=1, color=COLOUR1)
X.label_levels([10, 15], ax)


X.plot_psi([7, 8], ax, scaling=1, color=COLOUR1)
X.label_levels([7, 8], ax)
X.plot_psi([5, 6], ax, scaling=1, color=COLOUR1)
X.label_levels([5, 6], ax)

X.plot_psi([3, 4], ax, scaling=1, color=COLOUR1)
X.label_levels([3, 4], ax)
X.plot_psi([0, 1], ax, scaling=1, color=COLOUR1)
X.label_levels([0, 1], ax)

ax.set_xlabel(r'$r\;/\mathrm{\\A}$')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('morse-psi.pdf')
plt.show()
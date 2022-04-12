# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:02:14 2022

@author: Nagawa
"""

import numpy as np
import matplotlib.pyplot as plt

#Constantes:

d = 2.5*1e-3 #+-0.00001 m
p1 = 1.03*1e3 #kg/m3
p2 = 1.293 #kg/m3
N = 1.82*1e-5 #kg/(m*s)
g = 9.81 #m/s2
Dp1p2 = p1 - p2

    
#Dados:

data = np.loadtxt('data.dat', dtype=np.float64)

U = data[:,0] #V
t1 = data[:,1] #s
s1d = data[:,2] #div
t2 = data[:,3] #s
s2d = data[:,4] #div
s1 = data[:,5]*1e-3 #mm
s2 = data[:,6]*1e-3 #mm
v1 = data[:,7]*1e-3 #mm/s
v2 = data[:,8]*1e-3 #mm/s
Dv1v2 = data[:,9]*1e-3 #m/s
Sv1v2 = v1 + v2 #m/s

#Calculo dos Coeficientes:

C1 = (9/2)*(np.pi)*d*np.sqrt((N**3)/(g*Dp1p2)) #kg*m/(m*s)^1/2
C2 = (3/2)*np.sqrt((N)/(g*Dp1p2)) #(m*s)^1/2

#Calculo de Q:
    
Q = C1*(Sv1v2/U)*np.sqrt(Dv1v2)
Q2 = Q*1e19

#Calculo de r:

r = C2*np.sqrt(Dv1v2)

#Calculo de n e e:

n = np.array([5, 2, 2, 2, 4, 8, 9, 2, 7, 7, 5, 5, 10, 4, 7, 14])

e = Q/n
em = np.mean(e)

def func(x, a, b):
    return a*x + b

from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(n,Q)

eajuste = slope
m = np.array([2,4,5,7,8,9,10,14])



#Graficos:

plt.axhline(y=3.2, color='k', ls='--', lw=0.5)
plt.axhline(y=6.4, color='k', ls='--', lw=0.5)
plt.axhline(y=8.0, color='k', ls='--', lw=0.5)
plt.axhline(y=9.6, color='k', ls='--', lw=0.5)
plt.axhline(y=11.2, color='k', ls='--', lw=0.5)
plt.axhline(y=12.8, color='k', ls='--', lw=0.5)
plt.axhline(y=14.4, color='k', ls='--', lw=0.5)
plt.axhline(y=16.0, color='k', ls='--', lw=0.5)
plt.axhline(y=24.0, color='k', ls='--', lw=0.5)


plt.scatter(n, Q2, marker='.', linewidths=0.2)
plt.plot(m, m*eajuste*1e19 + intercept, label=r'Regressão linear - $ \mathrm{e} = 1.603 \times 10^{19}$')
plt.plot(m, m*em*1e19, label=r'Média - $ \mathrm{e_{m}} = 1.656 \times 10^{19}$')
plt.ylim(0,25)
plt.xlim(0,15)
plt.yticks(ticks=np.linspace(0,24,16))
plt.xticks(ticks=np.linspace(0,15,16))
plt.xlabel('n')
plt.ylabel(r'$\mathrm{Q} \times 10^{19}$ (C)')
plt.legend(loc='lower right', fontsize='small')
plt.title('Carga da gotícula (Q) x múltiplo de e (n)')
plt.show()

print(r'$r \times 10^{7}$ (m)$', '\n', (r*1e7).reshape(len(r),1))
print(r'$Q \times 10^{19}$ (C)$', '\n', Q2.reshape(len(Q2),1))
print('n', '\n', n.reshape(len(n),1))
print(r'$(\mathrm{e} \pm 0.13) \times 10^{19}$ (C)', '\n', (e*1e19).reshape(len(e),1))





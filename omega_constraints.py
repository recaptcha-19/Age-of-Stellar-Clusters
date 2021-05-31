import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from scipy.integrate import quad

Mpc = 10**6*u.pc
Gyr = u.yr*10**9
H0 = 72*u.km/(u.s*Mpc)
omega_m0 = np.linspace(0, 1, num = 100)
omega_l0 = 1 - omega_m0
ages = [] 
def func(x,a,b):
    return 1/np.sqrt(a/x + b)

H0_inv = 1/H0
H0_inv = H0_inv.to(Gyr)

for omega in omega_m0:
    age  = H0_inv*quad(func, 0, 1, args = (omega, 1 - omega))
    ages.append(age)

ages = np.asarray(ages)
ages = ages[:,0]
print(ages)
print(omega_m0[ages > 12])  #values of omega_m0 corresponding to age limit obtained from star clusters

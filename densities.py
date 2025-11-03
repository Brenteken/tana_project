from astropy import units
import numpy as np

def hernquist(r_kpc, mass_sol, param_kpc):
    constant = 2*mass_sol / (4*np.pi*param_kpc)
    density = constant / ((r_kpc / param_kpc) * (1 + r_kpc/param_kpc)**3)
    return density

def plummer(r_kpc, mass_sol, param_kpc):
    constant = (3*mass_sol)/(4*np.pi*(param_kpc**3))
    density = constant*(1 + (r_kpc**2)/(param_kpc**2))**(-5/2)
    return density
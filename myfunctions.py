import numpy as np
import math

def rect(Sps):
   return [1]*Sps
   
def saw(Sps):
    return np.linspace(0,Sps-1,Sps)/(Sps-1)

def cos(Sps, k):
    n=np.linspace(0,Sps-1,Sps)
    return np.cos(2*math.pi*k*n/Sps)


from math import pi,sin,sqrt
import matplotlib.pyplot as plt
import numpy as np
from random import random
from scipy.optimize import curve_fit

#from donnees import *


# I) question 1

def echantillon(a,b,N):
    L=[a+((b-a)/N)*k for k in range(N+1)]
    return L
# question 2
 
Lt=echantillon(-pi,pi,1000)
Ly_ideal=[sin(t) for t in Lt]

# question 3

def nombre_alea(a,b):
    x=random()*((b-a)+a)
    return x

print(nombre_alea(1,10))

import numpy as np

def sig(x, deriv = False):
    if not deriv:
        return 1/(1 + np.exp(-x))
    else:
        return x*(1-x)
import numpy as np

def MOP2(x):
    n = np.size(x)

    z1 = 1 - np.exp(-np.power(sum(x - (1/np.sqrt(n))), 2))

    z2 = 1 - np.exp(-np.power(sum(x + (1/np.sqrt(n))), 2))

    z = np.array([z1, z2])

    return z[:, None]
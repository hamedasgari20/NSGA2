import numpy as np
from numpy import random as ra
import random


def Mutate(x, mu, sigma):

    nVar = len(x)

    nMu = np.ceil(mu * nVar)

    j = random.sample(range(1, nVar), int(nMu))

    y = x

    y[j] = x[j] + sigma * ra.normal(len(j))

    return y
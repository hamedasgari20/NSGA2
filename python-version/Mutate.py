import random

import numpy as np
from numpy import random as ra


def mutate(x, mu, sigma):
    """
    This function mutates a member of the population based on mutation rate.
    """
    nvar = len(x)

    nmu = np.ceil(mu * nvar)

    j = random.sample(range(1, nvar), int(nmu))

    y = x

    y[j] = x[j] + sigma * ra.normal(len(j))

    return y

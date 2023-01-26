import numpy as np
import matplotlib.pyplot as plt


def PlotCosts(pop):

    nObj = len(pop[0]["Cost"])
    n = len(pop)

    Costs = np.zeros((nObj, n))

    for j in range(n):
        Costs[:, j] = pop[j]["Cost"].ravel()

    plt.plot(Costs[0,:], Costs[1,:], 'ro')
    plt.show()
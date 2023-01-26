import matplotlib.pyplot as plt
import numpy as np


def plot_costs(pop):
    """
    This function plots the results
    """
    nobj = len(pop[0]["Cost"])
    n = len(pop)

    costs = np.zeros((nobj, n))

    for j in range(n):
        costs[:, j] = pop[j]["Cost"].ravel()

    plt.plot(costs[0, :], costs[1, :], 'ro')
    plt.show()

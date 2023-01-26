import numpy as np


def cal_crowding_distance(pop, f):
    """
    This function calculates crowding distance and list of frontiers
    """

    nf = len(f)
    nobj = len(pop[0]["Cost"])

    for k in range(nf):

        n = len(f[k])

        costs = np.zeros((nobj, n))

        for j in range(n):
            costs[:, j] = pop[f[k][j]]["Cost"].ravel()

        d = np.zeros((n, nobj))

        for j in range(nobj):

            so = np.argsort(costs[j, :])
            cj = costs[j, :][so]

            d[so[0], j] = np.inf

            for i in range(1, n - 1):
                d[so[i], j] = np.abs(cj[i + 1] - cj[i - 1]) / np.abs(cj[1] - cj[-1])

            d[so[-1], j] = np.inf

        for i in range(n):
            pop[f[k][i]]["CrowdingDistance"] = sum(d[i, :])

    return pop

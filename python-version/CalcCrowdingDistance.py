import numpy as np

def CalcCrowdingDistance(pop, F):

    nF = len(F)
    nObj = len(pop[0]["Cost"])

    for k in range(nF):

        n = len(F[k])

        Costs = np.zeros((nObj, n))

        for j in range(n):
            Costs[:, j] = pop[F[k][j]]["Cost"].ravel()

        d=np.zeros((n, nObj))

        for j in range(nObj):

            so = np.argsort(Costs[j, :])
            cj = Costs[j, :][so]

            d[so[0], j] = np.inf


            for i in range(1, n-1):
                d[so[i], j] = np.abs(cj[i+1]-cj[i-1])/np.abs(cj[1]-cj[-1])

            d[so[-1], j] = np.inf

        for i in range(n):

            pop[F[k][i]]["CrowdingDistance"] = sum(d[i, :])

    return pop

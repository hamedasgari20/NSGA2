import numpy as np
from Dominates import Dominates


def NonDominatedSorting(pop):
    nPop = np.size(pop)

    for i in pop:
        i["DominationSet"] = []
        i["DominatedCount"] = 0

    F = []

    for i in range(len(pop)):
        for j in range(i+1, len(pop)):
            p = pop[i]
            q = pop[j]

            if Dominates(p, q):
                p["DominationSet"].append(j)
                q["DominatedCount"] = q["DominatedCount"] + 1

            if Dominates(q, p):
                q["DominationSet"].append(i)
                p["DominatedCount"] = p["DominatedCount"] + 1

            pop[i] = p
            pop[j] = q

        if pop[i]["DominatedCount"] == 0:
            F.append(i)
            pop[i]["Rank"] = 1

    k = 1

    while True:
        Q = []
        for i in range(F[k]):
            p = pop[i]

            for j in p["DominationSet"]:
                q = pop[j]

                q["DominatedCount"] = q["DominatedCount"] - 1

                if q["DominatedCount"] == 0:
                    Q.append(j)
                    q["Rank"] = k + 1

                pop[j] = q

        if len(Q)==0:
            break

        F[k+1]=Q

        k=k+1

    return [pop, F]

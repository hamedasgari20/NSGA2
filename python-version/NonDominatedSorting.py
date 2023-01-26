from Dominates import dominates


def non_dominated_sorting(pop):
    """
    This function sorts population based on non dominated sorting algorithm

    """
    for i in range(len(pop)):
        pop[i]["DominationSet"] = []
        pop[i]["DominatedCount"] = 0

    f = [[]]

    for i in range(len(pop)):
        for j in range(i + 1, len(pop)):
            p = pop[i]
            q = pop[j]

            if dominates(p, q):
                p["DominationSet"].append(j)
                q["DominatedCount"] = q["DominatedCount"] + 1

            if dominates(q, p):
                q["DominationSet"].append(i)
                p["DominatedCount"] = p["DominatedCount"] + 1

            pop[i] = p
            pop[j] = q

        if pop[i]["DominatedCount"] == 0:
            f[0].append(i)
            pop[i]["Rank"] = 1

    k = 0

    while True:
        Q = []
        for i in f[k]:
            p = pop[i]

            for j in p["DominationSet"]:
                q = pop[j]

                q["DominatedCount"] = q["DominatedCount"] - 1

                if q["DominatedCount"] == 0:
                    Q.append(j)
                    q["Rank"] = k + 1

                pop[j] = q

        if len(Q) == 0:
            break

        f.append(Q)

        k = k + 1

    return [pop, f]

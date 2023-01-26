from operator import itemgetter


def sort_population(pop):
    """
    This function sorts populations based on crowding distance and rank
    """
    # Sort Based on Crowding Distance
    pop = sorted(pop, key=itemgetter('CrowdingDistance'), reverse=False)

    # Sort Based on Rank
    pop = sorted(pop, key=itemgetter('Rank'), reverse=False)

    # Update Fronts
    ranks = []
    for i in range(len(pop)):
        ranks.append(pop[i]["Rank"])
    max_rank = max(ranks)
    f = []
    for r in range(1, max_rank + 1):
        li = []
        li = [i for i in range(len(ranks)) if ranks[i] == r]
        f.append(li)

    return pop, f

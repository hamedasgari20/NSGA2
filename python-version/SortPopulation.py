import numpy as np
from operator import itemgetter


def SortPopulation(pop):

    # Sort Based on Crowding Distance
    pop = sorted(pop, key=itemgetter('CrowdingDistance'), reverse=False)

    # Sort Based on Rank
    pop = sorted(pop, key=itemgetter('Rank'), reverse=False)

    # Update Fronts
    Ranks = []
    for i in range(len(pop)):
        Ranks.append(pop[i]["Rank"])
    MaxRank=max(Ranks)
    F=[]
    for r in range(1, MaxRank+1):
        li = []
        li = [i for i in range(len(Ranks)) if Ranks[i] == r]
        F.append(li)

    return pop, F
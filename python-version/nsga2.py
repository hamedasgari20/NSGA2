import numpy as np

from MOP2 import MOP2
from NonDominatedSorting import NonDominatedSorting
from CalcCrowdingDistance import CalcCrowdingDistance
from SortPopulation import SortPopulation
from Crossover import Crossover
from Mutate import Mutate
from PlotCosts import PlotCosts
# Problem Definition

CostFunction = MOP2  # Cost Function

nVar = 3  # Number of Decision Variables

VarMin = -5  # Lower Bound of Variables
VarMax = 5  # Upper Bound of Variables

# Number of Objective Functions
nObj = np.size(CostFunction(np.random.uniform(VarMin, VarMax, nVar)))

## NSGA-II Parameters
MaxIt = 100;  # Maximum Number of Iterations

nPop = 50;  # Population Size

pCrossover = 0.7;  # Crossover Percentage
nCrossover = 2 * round(pCrossover * nPop / 2);  # Number of Parnets (Offsprings)

pMutation = 0.4;  # Mutation Percentage
nMutation = round(pMutation * nPop);  # Number of Mutants

mu = 0.02;  # Mutation Rate

sigma = 0.1 * (VarMax - VarMin);  # Mutation Step Size

## Initialization

pop = [{
    "Position": [],
    "Cost": [],
    "Rank": [],
    "DominationSet": [],
    "DominatedCount": [],
    "CrowdingDistance": [],
} for _ in range(nPop)]

for item in pop:
    item["Position"] = np.random.uniform(VarMin, VarMax, nVar)
    item["Cost"] = CostFunction(item["Position"])

## Non-Dominated Sorting
pop, F = NonDominatedSorting(pop)

# Calculate Crowding Distance
pop = CalcCrowdingDistance(pop, F)

# Sort Population
pop, F = SortPopulation(pop)


## NSGA-II Main Loop

for it in range(1, MaxIt):

    # Crossover
    popc1 = [{
        "Position": [],
        "Cost": [],
        "Rank": [],
        "DominationSet": [],
        "DominatedCount": [],
        "CrowdingDistance": [],
    } for _ in range(int(nCrossover/2))]

    popc2 = [{
        "Position": [],
        "Cost": [],
        "Rank": [],
        "DominationSet": [],
        "DominatedCount": [],
        "CrowdingDistance": [],
    } for _ in range(int(nCrossover/2))]

    for k in range(int(nCrossover/2)):
        i1 = np.random.randint(1, nPop)
        p1 = pop[i1]

        i2 = np.random.randint(1, nPop)
        p2 = pop[i2]

        popc1[k]["Position"], popc2[k]["Position"] = Crossover(p1["Position"], p2["Position"])

        popc1[k]["Cost"] = CostFunction(popc1[k]["Position"])
        popc2[k]["Cost"] = CostFunction(popc2[k]["Position"])

    popc1 = popc1 + popc2
    popc = popc1


    # Mutation
    popm = [{
        "Position": [],
        "Cost": [],
        "Rank": [],
        "DominationSet": [],
        "DominatedCount": [],
        "CrowdingDistance": [],
    } for _ in range(nMutation)]
    for k in range(nMutation):

        i = np.random.randint(1, nPop)
        p = pop[i]

        popm[k]["Position"] = Mutate(p["Position"], mu, sigma)

        popm[k]["Cost"] = CostFunction(popm[k]["Position"])

    # Merge
    pop = popc + popm + pop




    ## Non-Dominated Sorting
    pop, F = NonDominatedSorting(pop)

    # Calculate Crowding Distance
    pop = CalcCrowdingDistance(pop, F)

    # Sort Population
    pop, F = SortPopulation(pop)


    # Truncate
    pop = pop[0:nPop]




    ## Non-Dominated Sorting
    pop, F = NonDominatedSorting(pop)

    # Calculate Crowding Distance
    pop = CalcCrowdingDistance(pop, F)

    # Sort Population
    pop, F = SortPopulation(pop)



    # Store F1
    F1 = [pop[i] for i in F[0]]

    # Show Iteration Information
    print('Iteration {} : Number of F1 Members = {}'.format(it, len(F1)))

PlotCosts(pop)



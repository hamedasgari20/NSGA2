import numpy as np

from MOP2 import MOP2
from NonDominatedSorting import NonDominatedSorting

# Problem Definition

CostFunction = MOP2  # Cost Function

nVar = 3  # Number of Decision Variables

VarMin = -5  # Lower Bound of Variables
VarMax = 5  # Upper Bound of Variables

# Number of Objective Functions
nObj = np.size(CostFunction(np.random.uniform(VarMin, VarMax, nVar)))

## NSGA-II Parameters

MaxIt = 100;  # Maximum Number of Iterations

nPop = 10;  # Population Size

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


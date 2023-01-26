import numpy as np

from CalcCrowdingDistance import cal_crowding_distance
from Crossover import crossover
from MOP2 import mop2
from Mutate import mutate
from NonDominatedSorting import non_dominated_sorting
from PlotCosts import plot_costs
from SortPopulation import sort_population

# Problem Definition
cost_function = mop2  # Cost Function
nvar = 3  # Amount Decision Variables
var_min = -5  # Lower Bound of Variables
var_max = 5  # Upper Bound of Variables

# Amount Objective Functions
nObj = np.size(cost_function(np.random.uniform(var_min, var_max, nvar)))

# NSGA-II Parameters
max_it = 100  # Maximum Amount Iterations
npop = 50;  # Population Size
p_crossover = 0.7;  # Crossover Percentage
n_crossover = 2 * round(p_crossover * npop / 2);  # Amount Parents (Offsprings)
p_mutation = 0.4;  # Mutation Percentage
n_mutation = round(p_mutation * npop);  # Amount Mutants
mu = 0.02;  # Mutation Rate
sigma = 0.1 * (var_max - var_min);  # Mutation Step Size

# Initialization

pop = [{
    "Position": [],
    "Cost": [],
    "Rank": [],
    "DominationSet": [],
    "DominatedCount": [],
    "CrowdingDistance": [],
} for _ in range(npop)]

for item in pop:
    item["Position"] = np.random.uniform(var_min, var_max, nvar)
    item["Cost"] = cost_function(item["Position"])

# Non-Dominated Sorting
pop, F = non_dominated_sorting(pop)

# Calculate Crowding Distance
pop = cal_crowding_distance(pop, F)

# Sort Population
pop, F = sort_population(pop)

# NSGA-II Main Loop

for it in range(1, max_it):

    # Crossover
    popc1 = [{
        "Position": [],
        "Cost": [],
        "Rank": [],
        "DominationSet": [],
        "DominatedCount": [],
        "CrowdingDistance": [],
    } for _ in range(int(n_crossover / 2))]

    popc2 = [{
        "Position": [],
        "Cost": [],
        "Rank": [],
        "DominationSet": [],
        "DominatedCount": [],
        "CrowdingDistance": [],
    } for _ in range(int(n_crossover / 2))]

    for k in range(int(n_crossover / 2)):
        i1 = np.random.randint(1, npop)
        p1 = pop[i1]

        i2 = np.random.randint(1, npop)
        p2 = pop[i2]

        popc1[k]["Position"], popc2[k]["Position"] = crossover(p1["Position"], p2["Position"])

        popc1[k]["Cost"] = cost_function(popc1[k]["Position"])
        popc2[k]["Cost"] = cost_function(popc2[k]["Position"])

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
    } for _ in range(n_mutation)]
    for k in range(n_mutation):
        i = np.random.randint(1, npop)
        p = pop[i]

        popm[k]["Position"] = mutate(p["Position"], mu, sigma)

        popm[k]["Cost"] = cost_function(popm[k]["Position"])

    # Merge
    pop = popc + popm + pop

    # Non-Dominated Sorting
    pop, F = non_dominated_sorting(pop)

    # Calculate Crowding Distance
    pop = cal_crowding_distance(pop, F)

    # Sort Population
    pop, F = sort_population(pop)

    # Truncate
    pop = pop[0:npop]

    # Non-Dominated Sorting
    pop, F = non_dominated_sorting(pop)

    # Calculate Crowding Distance
    pop = cal_crowding_distance(pop, F)

    # Sort Population
    pop, F = sort_population(pop)

    # Store F1
    F1 = [pop[i] for i in F[0]]

    # Show Iteration Information
    print('Iteration {} : Number of F1 Members = {}'.format(it, len(F1)))

plot_costs(pop)

import numpy as np


def crossover(x1, x2):
    """
    This function create get parents and creates children (crossover operator)
    """

    alpha = np.random.rand(len(x1))

    y1 = alpha * x1 + (1 - alpha) * x2
    y2 = alpha * x2 + (1 - alpha) * x1

    return y1, y2

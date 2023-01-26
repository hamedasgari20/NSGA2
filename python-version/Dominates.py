def dominates(x, y):
    """
    This function calculate domination for two member of population
    """
    b = all(x["Cost"] <= y["Cost"]) and any(x["Cost"] < y["Cost"])

    return b

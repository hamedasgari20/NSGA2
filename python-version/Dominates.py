def Dominates(x, y):
    b = all(x["Cost"] <= y["Cost"]) and any(x["Cost"] < y["Cost"])

    return b

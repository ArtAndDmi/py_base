import math

def find_twin_pairs(X, threshold):
    res = []

    for i in range(len(X)):
        for j in range(i + 1, len(X)):

            distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(X[i], X[j])))

            if distance <= threshold:
                res.append((i, j, distance))

    return res

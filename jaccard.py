import numpy as np

def jaccard_sim(set_A, set_B):
    intersection = np.intersect1d(set_A, set_B)
    union = np.union1d(set_A, set_B)

    if len(union) == 0:
        return 0
    else:
        return (len(intersection)) / (len(union))
    

# Test cases
print(jaccard_sim(np.array([1, 2,3, 4, 5]), np.array([3, 4, 5, 6, 7])))


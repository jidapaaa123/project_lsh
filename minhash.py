# quick check to see if my function works
# and also export the function

import random as rand
import numpy as np
import os
import sys 
os.system('cls')

# (each column is a set)
data_matrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
])

# (each hash function is a column)
hash_index_matrix = np.array([
    [0, 3, 4, 4],
    [2, 1, 5, 0],
    [4, 5, 6, 1],
    [1, 3, 0, 2],
    [3, 1, 1, 3],
])

# The project specifies 
#   "Create a Python function that will return the 
#    result of a minhash function"
# But this just takes in a 
# matrix of >= 1 minhash function (hash_mat)...
# So hopefully that's ok
def minhash(data_mat, hash_mat):
    # resulting sig_mat has 
    # 1 column per set
    # 1 row per hash function (each hash function is a column in hash_mat)
    _, cols = data_mat.shape
    _, rows = hash_mat.shape
    sig_mat = np.full((rows, cols), sys.maxsize)
    # for every row index in hash_mat
    for i in range(len(hash_mat)):
        hash_row = hash_mat[i]
        data_row = data_mat[i]
        in_columns = np.where(data_row == 1)[0] # see which sets the hash applies to
        # print(f"hash: {hash_row} for row: {data_row}")
        # print(f"sets: {in_columns}")

        # iterate on those sets/columns
        for col_i in in_columns:
            column = sig_mat[:, col_i] # select col_i
            new_column = list(map(lambda curr_sig, hash_row:
                                hash_row if hash_row < curr_sig
                                else curr_sig,
                                column, hash_row
                                )
                             )
            # replace column in actual array
            sig_mat[:, col_i] = new_column
    
    return sig_mat

print(minhash(data_matrix, hash_index_matrix))
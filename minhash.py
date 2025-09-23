# quick check to see if my function works
# and also export the function

import random as rand
import numpy as np
import os
os.system('cls')

data_matrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
])
signature_matrix = np.full((4, 4), 9)
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
def minhash(data_mat, sig_mat, hash_mat):
    # for every row index in hash_mat
    for i in range(len(hash_mat)):
        hash_row = hash_index_matrix[i]
        data_row = data_mat[i]
        in_columns = np.where(data_row == 1)[0] # see which sets the hash applies to
        print(f"hash: {hash_row} for row: {data_row}")
        print(f"sets: {in_columns}")

        # iterate on those sets/columns
        for col_i in in_columns:
            column = sig_mat[:, col_i] # select col_i
            new_column = list(map(lambda curr_sig, hash_row:
                                hash_row if hash_row < curr_sig
                                else curr_sig,
                                column, hash_row
                                )
                             )
            print(new_column)
            # replace column in actual array
            sig_mat[:, col_i] = new_column
    
    return sig_mat


print(minhash(data_matrix, signature_matrix, hash_index_matrix))
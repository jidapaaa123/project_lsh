import os 
import pandas as pd
import random as rand
import matplotlib.pyplot as plt
import numpy as np
import itertools as iter

# my own modules
from minhash import minhash
from jaccard import jaccard_sim


os.system('cls')

NUM_OF_HASH_FUNCTIONS = 250
path = "./food_consumption.csv"
df = pd.read_csv(path)

# Pivot Table of data
pivot = pd.pivot_table(
    df,
    index="food_category",
    columns="country",
    values=["consumption", "co2_emission"],
    )


# Normalize each column --> (x - min) / (min - max)
pivot['consumption'] = pivot['consumption'].apply(lambda col: (col - col.min()) / (col.max() - col.min()))
# print(pivot['consumption'])

# Turn all values into 1's and 0's, with threshold being >= 0.5
pivot['consumption'] = pivot['consumption'].map((lambda x: 1 if x >= 0.5 else 0))
# print(pivot['consumption'])

# I just noticed the project doesn't seem to care about
# the co2_emission column, so I'll ignore it now

# minhash function can just be random permutation of range(rows)
rows = len(pivot.index) # = 11 rows
possible_indices = range(rows)
# 250 functions = 250 columns
# 11 rows
hash_matrix = np.empty((rows, NUM_OF_HASH_FUNCTIONS), dtype=int) 
    # declare the type because I don't like 
    # seeing the periods after the numbers

# generate 250 minhash functions
# populate into each column of hash_matrix
for i in range(NUM_OF_HASH_FUNCTIONS):
    hash_func = np.random.permutation(possible_indices)
    hash_matrix[:, i] = hash_func


signature_matrix = minhash(pivot['consumption'].to_numpy(), hash_matrix)
first_band = signature_matrix[:5, :] # takes the first 5 rows

column_tuples = [tuple(first_band[:, j]) for j in range(first_band.shape[1])]
# bucket by identical tuples
from collections import defaultdict
buckets = defaultdict(list)     # to not check for missing keys
bucket_sizes = defaultdict(int)

# NOTE: this actually buckets IDENTICAL band-signatures together...
# It's jut such a big data set that somehow it still gets buckets
#   with multiple sets
for set, sig in enumerate(column_tuples):
    buckets[sig].append(set)
    bucket_sizes[sig] += 1

# sort the buckets
sorted_bucket_sizes_items = sorted(bucket_sizes.items(), key=lambda item: item[1], reverse=True)
sorted_bucket_sizes = dict(sorted_bucket_sizes_items)
# print(sorted_bucket_sizes)

TOP_CANDIDATE_PAIRS = 5
top_signatures = list(sorted_bucket_sizes.keys())[:TOP_CANDIDATE_PAIRS]
# print(top_signatures)

# JACCARD SIMILARITY ON FULL SIGNATURES

jaccard_similarities = defaultdict(float)
# per each top signature...
import itertools
for sig in top_signatures:
    sets = buckets[sig]     # sets in the same band-signature bucket

    if len(sets) <= 1:       # otherwise just skip this signature...
        break                # and because it's sorted, just skip the rest too

    # for each combination of the sets...
    for i, j in itertools.combinations(sets, 2):
        # ith and jth columns of the full signature_matrix!
        sim = jaccard_sim(np.array(signature_matrix[:, i]), 
                          np.array(signature_matrix[:, j]))
        jaccard_similarities[(i, j)] = sim

# sort by the value of the key-value pair
sorted_jSim_items = sorted(jaccard_similarities.items(), key=lambda item: item[1], reverse=True)
jaccard_similarities = dict(sorted_jSim_items)

# FULL JACCARD SIMILARITY OF ALL CANDIDATE PAIRS
import shutil

# PRINT JACCARD VALUES
# but replace set_index with country names
file_path = './final_data.txt'

print("Writing to file...")
with open(file_path, 'w') as file:
    file.write('=' * shutil.get_terminal_size()[0] + '\n')
    for key, value in jaccard_similarities.items():
        country0 = pivot['consumption'].columns[key[0]]
        country1 = pivot['consumption'].columns[key[1]]
        file.write(f"({country0}, {country1}): {value}," + '\n')
    file.write('=' * shutil.get_terminal_size()[0] + '\n')

print("Data from this run (and only this run) can now be seen in the final_data.txt file")




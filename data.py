import os 
import pandas as pd
import random as rand
import matplotlib.pyplot as plt
import numpy as np

# my own module
from minhash import minhash


os.system('cls')

path = "./food_consumption.csv"
df = pd.read_csv(path)

# Pivot Table of data
pivot = pd.pivot_table(
    df,
    index="food_category",
    columns="country",
    values=["consumption", "co2_emission"],
    )

# print(pivot["consumption"] + 50)


# Normalize each column --> (x - min) / (min - max)
pivot['consumption'] = pivot['consumption'].apply(lambda col: (col - col.min()) / (col.max() - col.min()))
pivot['co2_emission'] = pivot['co2_emission'].apply(lambda col: (col - col.min()) / (col.max() - col.min()))

# print(pivot['consumption'])
# print(pivot['co2_emission'])

# Turn all values into 1's and 0's, with threshold being >= 0.5
pivot['consumption'] = pivot['consumption'].applymap(lambda x: 1 if x >= 0.5 else 0)
pivot['co2_emission'] = pivot['co2_emission'].applymap(lambda x: 1 if x >= 0.5 else 0)

print(pivot['consumption'])
# print(pivot['co2_emission'])

# I just noticed the project doesn't seem to care about
# the co2_emission column, so I'll ignore it now
# def minhash():

rows = pivot.index
cols = len(pivot.columns)









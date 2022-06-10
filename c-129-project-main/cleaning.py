
import pandas as pd
import csv

df = pd.read_csv("Processed_data/total_stars.csv")

del df["Luminosity"]

data = df.dropna()

data.reset_index(drop = True, inplace =True)

data.to_csv("final.csv")


import pandas as pd
import matplotlib.pyplot as plt

headers = ["data", "visitors"]
data = pd.read_csv("visitors.csv", skiprows=4, names=headers)
# print(data.head())

headers = ["data", "visitors_new"]
data_new = pd.read_csv("visitors-new.csv", skiprows=4, names=headers)
# print(data_new.head())



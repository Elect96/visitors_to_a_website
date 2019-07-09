import pandas as pd
import matplotlib.pyplot as plt

headers = ["date", "visitors"]
data = pd.read_csv("visitors.csv", skiprows=4, names=headers)
data.head()

headers = ["date", "visitors_new"]
data_new = pd.read_csv("visitors-new.csv", skiprows=4, names=headers)
data_new.head()

data_combined = pd.merge(data, data_new)
data_combined.head()
data_combined.sort_values(by=["date"], inplace=True)
data_combined.set_index("date", inplace=True)
data_combined.head()
data_combined.plot()
plt.show()

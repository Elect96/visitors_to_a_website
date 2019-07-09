import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("operating-systems.csv")
data.rename(columns={"Item": "Operating System"}, inplace=True)

os_new = data[["Operating System", "Value Percent"]]
os_new.set_index("Operating System", inplace=True)

explode = (0.1, 0, 0, 0, 0)
colors_mine = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightcyan']
os_new[:5].plot(kind="pie", y="Value Percent", autopct='%.2f%%', shadow=True, explode=explode,
                legend=False, colors=colors_mine)
plt.show()


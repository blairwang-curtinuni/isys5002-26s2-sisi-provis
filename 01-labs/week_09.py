print("Hello, Week 9! 5 weeks to go!")

import pandas as pd

df = pd.read_csv("week_09_dataset.csv")

#df_perth = df[df["city"] == "Perth"]
#print(df_perth)

# Average temperature for each city
#print(df.groupby("city")["temperature"].mean())

import matplotlib.pyplot as plt

avg_temp = df.groupby("city")["temperature"].mean()

avg_temp.plot(kind="bar", title="Fig 1. Average temperature by city")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("avg_temp.png")
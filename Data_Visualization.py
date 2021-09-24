import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Star_Data.csv")

df.head()

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius,mass)

plt.title("Radius and Mass of the Stars")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,gravity)
plt.title("Mass and Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()
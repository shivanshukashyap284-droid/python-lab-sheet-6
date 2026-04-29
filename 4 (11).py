import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns

# Generate dataset
time = np.arange(0, 24, 1)  # 24 hours
vehicle_count = np.random.randint(100, 1000, size=24)
speed = np.random.randint(20, 80, size=24)

df = pd.DataFrame({"Time": time, "Vehicles": vehicle_count, "Speed": speed})

# Peak traffic hours
peak_hours = df[df["Vehicles"] > df["Vehicles"].quantile(0.9)]

# Relationship
print("Correlation Speed vs Vehicles:", df["Speed"].corr(df["Vehicles"]))

# Visualizations
plt.plot(df["Time"], df["Vehicles"]); plt.title("Traffic vs Time"); plt.show()
sns.scatterplot(x="Vehicles", y="Speed", data=df); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

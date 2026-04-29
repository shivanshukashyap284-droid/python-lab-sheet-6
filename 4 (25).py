import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
plt.figure(figsize=(10,5))
plt.plot(data["Day"], data["Traffic"], label="Traffic")
plt.plot(data["Day"], data["AQI"], label="AQI")
plt.plot(data["Day"], data["Energy"], label="Energy")
plt.legend()
plt.title("Urban Trends Over Time")
plt.show()

# Scatterplot Traffic vs AQI
sns.scatterplot(x="Traffic", y="AQI", data=data)
plt.title("Traffic vs AQI")
plt.show()

# Barplot Energy vs Activity
sns.barplot(x="Activity", y="Energy", data=data)
plt.title("Average Energy Consumption by Activity Level")
plt.show()

# Boxplot AQI
sns.boxplot(y="AQI", data=data)
plt.title("AQI Outliers")
plt.show()

# Heatmap correlations
plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Histogram with KDE
sns.histplot(data["Traffic"], kde=True)
plt.title("Traffic Distribution")
plt.show()

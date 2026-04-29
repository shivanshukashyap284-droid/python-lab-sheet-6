import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns

# Generate dataset
students = 30
marks = np.random.randint(40, 100, (students, 3))
age = np.random.randint(18, 25, students)

df = pd.DataFrame(marks, columns=["Math", "Science", "English"])
df["Age"] = age

# Handle missing values & duplicates
df.iloc[2, 1] = np.nan
df.drop_duplicates(inplace=True)
df.fillna(df.mean(), inplace=True)

# Stats
print(df.describe())

# Assign grades
df["Average"] = df[["Math","Science","English"]].mean(axis=1)
df["Grade"] = pd.cut(df["Average"], bins=[0,50,65,80,100],
                     labels=["D","C","B","A"])

# Visualizations
df[["Math","Science","English"]].plot(kind="line"); plt.show()
df.mean().plot(kind="bar"); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

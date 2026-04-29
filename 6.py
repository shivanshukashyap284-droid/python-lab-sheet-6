age = np.random.randint(18, 60, 50)
income = np.random.randint(20000, 100000, 50)
score = np.random.randint(1, 100, 50)

df = pd.DataFrame({"Age": age, "Income": income, "Score": score})

# Categorize customers
df["Segment"] = pd.cut(df["Score"], bins=[0,40,70,100],
                       labels=["Low","Medium","High"])

sns.scatterplot(x="Age", y="Income", hue="Segment", data=df); plt.show()
sns.pairplot(df, hue="Segment"); plt.show()
sns.boxplot(y="Income", data=df); plt.show()

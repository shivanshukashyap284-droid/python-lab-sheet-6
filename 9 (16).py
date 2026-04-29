players = ["P1","P2","P3","P4","P5"]
matches = np.random.randint(10, 50, 5)
runs = np.random.randint(200, 2000, 5)
strike_rate = np.random.randint(80, 150, 5)

df = pd.DataFrame({"Player": players, "Matches": matches,
                   "Runs": runs, "StrikeRate": strike_rate})

# Rank players
print(df.sort_values("Runs", ascending=False))

# Visualizations
sns.barplot(x="Player", y="Runs", data=df); plt.show()
sns.scatterplot(x="Runs", y="StrikeRate", data=df); plt.show()
sns.violinplot(y="Runs", data=df); plt.show()

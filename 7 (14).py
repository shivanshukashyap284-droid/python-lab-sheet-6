days = np.arange(1, 31)
energy = np.random.randint(100, 500, 30)
temp = np.random.randint(15, 40, 30)

df = pd.DataFrame({"Day": days, "Energy": energy, "Temp": temp})

# High usage
print(df[df["Energy"] > df["Energy"].quantile(0.9)])

# Visualizations
plt.plot(df["Day"], df["Energy"]); plt.title("Energy Trend"); plt.show()
sns.scatterplot(x="Temp", y="Energy", data=df); plt.show()
sns.histplot(df["Energy"], kde=True); plt.show()

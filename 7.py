dates = pd.date_range("2021-01-01", periods=30)
cases = np.random.randint(100, 1000, 30)
recoveries = np.random.randint(50, 900, 30)
deaths = np.random.randint(1, 50, 30)

df = pd.DataFrame({"Date": dates, "Cases": cases,
                   "Recoveries": recoveries, "Deaths": deaths})

df["GrowthRate"] = df["Cases"].pct_change()

plt.plot(df["Date"], df["Cases"]); plt.show()
sns.histplot(df["Cases"], kde=True); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

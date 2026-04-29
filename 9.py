days = np.arange(1, 31)
stockA = np.random.randint(100, 200, 30)
stockB = np.random.randint(50, 150, 30)

df = pd.DataFrame({"Day": days, "StockA": stockA, "StockB": stockB})
df["MA_A"] = df["StockA"].rolling(5).mean()

plt.plot(df["Day"], df["StockA"], label="StockA")
plt.plot(df["Day"], df["MA_A"], label="MA_A"); plt.legend(); plt.show()
sns.histplot(df["StockA"], kde=True); plt.show()
sns.lineplot(data=df[["StockA","StockB"]]); plt.show()

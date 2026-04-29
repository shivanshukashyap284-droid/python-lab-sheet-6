products = ["P1","P2","P3","P4","P5"]
sales = np.random.randint(100, 1000, 5)
profit = np.random.randint(10, 200, 5)

df = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})

print(df.groupby("Product")["Sales"].agg(["sum","mean"]))
print("Best:", df.loc[df["Sales"].idxmax()])
print("Worst:", df.loc[df["Sales"].idxmin()])

sns.barplot(x="Product", y="Sales", data=df); plt.show()
plt.plot(df["Product"], df["Sales"]); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

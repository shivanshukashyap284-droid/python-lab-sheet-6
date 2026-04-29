orders = np.arange(1, 21)
products = np.random.choice(["A","B","C"], 20)
qty = np.random.randint(1, 10, 20)
price = np.random.randint(100, 500, 20)

df = pd.DataFrame({"OrderID": orders, "Product": products,
                   "Quantity": qty, "Price": price})
df["Revenue"] = df["Quantity"] * df["Price"]

print("Top products:", df.groupby("Product")["Revenue"].sum())

sns.barplot(x="Product", y="Revenue", data=df); plt.show()
df.groupby("Product")["Revenue"].sum().plot(kind="pie"); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

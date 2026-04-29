# Example: E-commerce dataset
products = ["A","B","C","D"]
sales = np.random.randint(100, 1000, 20)
profit = np.random.randint(10, 200, 20)

df = pd.DataFrame({"Product": np.random.choice(products, 20),
                   "Sales": sales, "Profit": profit})

# Cleaning
df.drop_duplicates(inplace=True)

# Stats
print(df.describe())

# Feature creation
df["ProfitMargin"] = df["Profit"] / df["Sales"]

# Visualizations
plt.plot(df["Sales"]); plt.title("Sales Trend"); plt.show()
sns.barplot(x="Product", y="Sales", data=df); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

# Insights
print("Top product:", df.groupby("Product")["Sales"].sum().idxmax())
print("Correlation Sales-Profit:", df["Sales"].corr(df["Profit"]))

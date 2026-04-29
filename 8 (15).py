cust_id = np.arange(1, 21)
balance = np.random.randint(1000, 10000, 20)
transactions = np.random.randint(10, 100, 20)
loan_status = np.random.choice(["Approved","Rejected"], 20)

df = pd.DataFrame({"CustomerID": cust_id, "Balance": balance,
                   "Transactions": transactions, "LoanStatus": loan_status})

# High-value customers
print(df[df["Balance"] > df["Balance"].quantile(0.9)])

# Visualizations
sns.countplot(x="LoanStatus", data=df); plt.show()
sns.boxplot(y="Balance", data=df); plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm"); plt.show()

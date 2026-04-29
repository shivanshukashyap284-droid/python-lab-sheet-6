income = np.random.randint(20000, 100000, 30)
credit = np.random.randint(300, 850, 30)
loan_amt = np.random.randint(5000, 50000, 30)
status = np.random.choice(["Approved","Rejected"], 30)

df = pd.DataFrame({"Income": income, "CreditScore": credit,
                   "LoanAmount": loan_amt, "Status": status})

# Trends
print(df.groupby("Status")["LoanAmount"].mean())

# Visualizations
sns.countplot(x="Status", data=df); plt.show()
sns.scatterplot(x="Income", y="LoanAmount", hue="Status", data=df); plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm"); plt.show()

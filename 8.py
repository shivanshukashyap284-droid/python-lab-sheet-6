ids = np.arange(1, 21)
salary = np.random.randint(30000, 120000, 20)
experience = np.random.randint(1, 20, 20)
dept = np.random.choice(["HR","IT","Finance"], 20)

df = pd.DataFrame({"ID": ids, "Salary": salary,
                   "Experience": experience, "Dept": dept})

print(df.groupby("Dept")["Salary"].mean())
print("Outliers:", df[df["Salary"] > df["Salary"].quantile(0.95)])

sns.boxplot(y="Salary", data=df); plt.show()
sns.barplot(x="Dept", y="Salary", data=df); plt.show()
sns.violinplot(x="Dept", y="Experience", data=df); plt.show()

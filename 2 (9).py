marks = np.random.randint(40, 100, 50)
category = np.random.choice(["GEN","OBC","SC"], 50)
status = np.random.choice(["Admitted","Rejected"], 50)

df = pd.DataFrame({"Marks": marks, "Category": category, "Status": status})

print("Selection ratio:", (df["Status"]=="Admitted").mean())

sns.countplot(x="Status", data=df); plt.show()
sns.barplot(x="Category", y=(df["Status"]=="Admitted").astype(int), data=df); plt.show()
sns.histplot(df["Marks"], kde=True); plt.show()

patients = np.arange(1, 21)
age = np.random.randint(20, 70, 20)
disease = np.random.choice(["Flu","Covid","Diabetes"], 20)
recovery = np.random.randint(5, 30, 20)

df = pd.DataFrame({"PatientID": patients, "Age": age,
                   "Disease": disease, "RecoveryDays": recovery})

# Trends
print(df.groupby("Disease")["RecoveryDays"].mean())

# Visualizations
sns.boxplot(y="RecoveryDays", data=df); plt.show()
sns.countplot(x="Disease", data=df); plt.show()
sns.histplot(df["Age"], kde=True); plt.show()

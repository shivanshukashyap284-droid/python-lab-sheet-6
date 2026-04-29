products = ["A","B","C","D","E"]
rating = np.random.randint(1, 5, 5)
review_score = np.random.randint(1, 10, 5)

df = pd.DataFrame({"Product": products, "Rating": rating,
                   "ReviewScore": review_score})

# Low-rated products
print(df[df["Rating"] <= 2])

# Visualizations
sns.barplot(x="Product", y="Rating", data=df); plt.show()
sns.boxplot(y="ReviewScore", data=df); plt.show()
sns.histplot(df["Rating"], kde=True); plt.show()

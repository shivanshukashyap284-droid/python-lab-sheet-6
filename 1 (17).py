posts = np.arange(1, 21)
likes = np.random.randint(50, 500, 20)
shares = np.random.randint(10, 100, 20)
comments = np.random.randint(5, 50, 20)

df = pd.DataFrame({"PostID": posts, "Likes": likes,
                   "Shares": shares, "Comments": comments})

# Engagement
df["Engagement"] = df["Likes"] + df["Shares"] + df["Comments"]
print(df.nlargest(3, "Engagement"))

# Visualizations
sns.barplot(x="PostID", y="Engagement", data=df); plt.show()
sns.scatterplot(x="Likes", y="Shares", data=df); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()

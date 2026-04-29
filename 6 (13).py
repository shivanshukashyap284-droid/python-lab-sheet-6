movies = ["M1","M2","M3","M4","M5"]
ratings = np.random.randint(1, 10, 5)
genres = ["Action","Drama","Comedy","Action","Drama"]
views = np.random.randint(100, 1000, 5)

df = pd.DataFrame({"Movie": movies, "Rating": ratings, "Genre": genres, "Views": views})

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Average rating per genre
print(df.groupby("Genre")["Rating"].mean())

# Top-rated movies
print(df.nlargest(3, "Rating"))

# Visualizations
sns.barplot(x="Genre", y="Rating", data=df); plt.show()
sns.boxplot(y="Rating", data=df); plt.show()
sns.countplot(x="Genre", data=df); plt.show()

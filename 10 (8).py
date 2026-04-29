temp = np.random.randint(10, 40, 30)
humidity = np.random.randint(20, 90, 30)
wind = np.random.randint(0, 20, 30)

df = pd.DataFrame({"Temp": temp, "Humidity": humidity, "Wind": wind})

print(df.describe())
print("Extreme temps:", df[df["Temp"] > 35])

plt.plot(df["Temp"]); plt.show()
sns.scatterplot(x="Humidity", y="Temp", data=df); plt.show()
sns.boxplot(y="Temp", data=df); plt.show()

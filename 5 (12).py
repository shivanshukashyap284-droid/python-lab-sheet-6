flights = np.arange(1, 21)
passengers = np.random.randint(50, 300, 20)
delay = np.random.randint(0, 180, 20)

df = pd.DataFrame({"FlightID": flights, "Passengers": passengers, "Delay": delay})

# Busiest flights
print(df.nlargest(3, "Passengers"))

# Visualizations
plt.plot(df["FlightID"], df["Passengers"]); plt.title("Passenger Trend"); plt.show()
sns.scatterplot(x="Passengers", y="Delay", data=df); plt.show()
sns.boxplot(y="Delay", data=df); plt.show()

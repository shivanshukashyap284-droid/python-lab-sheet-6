# Descriptive statistics
stats = data.describe()

# Peak traffic days
peak_traffic = data[data["Traffic"] > data["Traffic"].quantile(0.95)]

# High pollution days
high_pollution = data[data["AQI"] > 200]

# Abnormal energy consumption (above 95th percentile)
abnormal_energy = data[data["Energy"] > data["Energy"].quantile(0.95)]

# Relationship analysis
traffic_aqi_corr = data["Traffic"].corr(data["AQI"])
temp_energy_corr = data["Temperature"].corr(data["Energy"])

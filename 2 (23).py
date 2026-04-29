# Introduce missing values
data.loc[5, "AQI"] = np.nan
data.loc[20, "Energy"] = np.nan

# Introduce duplicates
data = pd.concat([data, data.iloc[10:12]], ignore_index=True)

# Handle missing values (fill with mean)
data["AQI"].fillna(data["AQI"].mean(), inplace=True)
data["Energy"].fillna(data["Energy"].mean(), inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Create new features
data["Energy_per_Traffic"] = data["Energy"] / data["Traffic"]
data["Pollution_per_Traffic"] = data["AQI"] / data["Traffic"]

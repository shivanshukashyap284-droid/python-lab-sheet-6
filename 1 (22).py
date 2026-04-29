import numpy as np
import pandas as pd

np.random.seed(42)  # reproducibility
days = 100

# Generate synthetic data
traffic = np.random.randint(2000, 10000, days)          # vehicles
aqi = np.random.randint(50, 300, days)                  # Air Quality Index
energy = np.random.randint(1000, 5000, days)            # energy units
temperature = np.random.randint(10, 40, days)           # °C
activity = np.random.randint(1, 10, days)               # public activity score

# Create DataFrame
data = pd.DataFrame({
    "Day": np.arange(1, days+1),
    "Traffic": traffic,
    "AQI": aqi,
    "Energy": energy,
    "Temperature": temperature,
    "Activity": activity
})

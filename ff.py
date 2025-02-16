import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Simulated market data (typically sourced from an API or database)
data = {
    'Contract': ['Spot', 'Month+1', 'Month+2', 'Quarter+1', 'Year+1'],
    'Price': [90, 92, 94, 98, 105],  # Simulated prices (£/MWh)
    'Tenor': [0, 1, 2, 3, 12]  # Contract months ahead
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Interpolate the forward curve (Spline Interpolation for smooth curve)
curve_interpolator = interp1d(df['Tenor'], df['Price'], kind='cubic', fill_value='extrapolate')
tenors = np.linspace(0, 12, 100)  # Generate a smooth range of tenors
prices = curve_interpolator(tenors)

# Plot the forward curve
plt.figure(figsize=(8, 5))
plt.plot(df['Tenor'], df['Price'], 'o', label="Market Prices")  # Market data points
plt.plot(tenors, prices, label="Interpolated Forward Curve", linestyle="--")
plt.xlabel("Months Ahead")
plt.ylabel("Price (£/MWh)")
plt.title("Interpolated Forward Curve")
plt.legend()
plt.grid()
plt.show()

# Simulated hedging strategy: Rolling hedge (buying forward contracts every month)
exposure = 100  # MWh to hedge per month
hedge_prices = curve_interpolator(np.arange(1, 13))  # Prices for each month ahead
hedged_costs = np.sum(hedge_prices * exposure) / 12  # Averaged cost per month

print(f"Estimated hedging cost per MWh: £{hedged_costs:.2f}")
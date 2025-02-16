Yes, they likely use an API to fetch UK day-ahead hourly prices from exchanges like EPEX SPOT or Nord Pool. Let’s go step by step to get the data and visualize it using Python.

1. Getting UK Day-Ahead Hourly Prices via API

Most energy companies pull market data using APIs rather than manual downloads. The key APIs for UK electricity markets are:

🔹 a) EPEX SPOT API (European Power Exchange)
	•	Provides day-ahead hourly auction prices for the UK and Europe.
	•	Requires API credentials (provided by EPEX).

📌 Endpoint (Example):

https://api.epexspot.com/public/marketdata

🔹 b) Nord Pool API (Northern European Market)
	•	Covers UK, Nordics, and some European power markets.
	•	Offers REST API for fetching prices programmatically.

📌 Endpoint (Example):

https://www.nordpoolgroup.com/api/marketdata

🔹 c) Bloomberg API (If Veolia Uses Bloomberg)
	•	Provides historical and real-time power prices.
	•	Requires Bloomberg Terminal access.

📌 Example Bloomberg Function for Excel/Python:

BDH("UKBL1 Index", "PX_LAST", "2024-02-15", "2024-02-16")

2. Python Script to Fetch EPEX SPOT Prices

If Veolia provides access to EPEX SPOT API, here’s how you can pull UK day-ahead hourly prices:

Step 1: Install Dependencies

pip install requests pandas matplotlib

Step 2: Fetch Data from EPEX SPOT API

import requests
import pandas as pd
import matplotlib.pyplot as plt

# EPEX API URL (Replace with actual endpoint)
api_url = "https://api.epexspot.com/public/marketdata"

# API Parameters (Adjust based on EPEX documentation)
params = {
    "market": "UK",
    "product": "DayAhead",
    "date": "2024-02-16",  # Adjust date as needed
    "currency": "GBP"
}

# Fetch data from API
response = requests.get(api_url, params=params)

# Convert to JSON
data = response.json()

# Extract hourly prices (Adjust key names based on actual API response)
hourly_prices = data["prices"]

# Convert to DataFrame
df = pd.DataFrame(hourly_prices, columns=["Hour", "Price (£/MWh)"])
df["Hour"] = df["Hour"].astype(int)  # Ensure hour is an integer

# Print sample data
print(df.head())

# Plot Day-Ahead Price Trends
plt.figure(figsize=(10, 5))
plt.plot(df["Hour"], df["Price (£/MWh)"], marker="o", linestyle="-", color="b")
plt.xlabel("Hour of Day")
plt.ylabel("Power Price (£/MWh)")
plt.title("UK Day-Ahead Power Prices")
plt.xticks(range(0, 24))  # Ensure all 24 hours are displayed
plt.grid(True)
plt.show()

3. Alternative: Fetch UK Day-Ahead Prices from Nord Pool API

If they use Nord Pool, modify the API URL:

api_url = "https://www.nordpoolgroup.com/api/marketdata"
params = {
    "market": "UK",
    "date": "2024-02-16",
    "currency": "GBP"
}

📌 API Access Note: You may need API keys or login credentials from your company.

4. Expected Output
	•	A table with hourly electricity prices for the UK market.
	•	A line chart showing price trends across 24 hours.

📊 Example Data (Hypothetical Output)

Hour	Price (£/MWh)
00	55.2
01	54.8
02	53.5
…	…
23	72.1

📈 Chart: Hourly Price Trends
The visualization will show how power prices fluctuate across the day, which is important for hedging and trading decisions.

5. Next Steps

✅ Check API Access – Find out whether Veolia uses EPEX, Nord Pool, or Bloomberg.
✅ Modify API Calls – Adjust the script based on your company’s API documentation.
✅ Automate Data Retrieval – Schedule daily price fetching using cron jobs or Airflow.
✅ Compare Prices Over Time – Analyze weekly/monthly trends for trading insights.

Would you like help automating daily price reports or setting up alerts for price spikes?
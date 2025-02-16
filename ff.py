import requests
import pandas as pd
import matplotlib.pyplot as plt
from xbbg import blp  # Bloomberg API (if available)

# Function to fetch data from EPEX SPOT API
def fetch_epex_spot_prices():
    """
    Fetch UK Day-Ahead Hourly Prices from EPEX SPOT API.
    Requires an API key (check with Veolia).
    """
    api_url = "https://api.epexspot.com/public/marketdata"  # Replace with actual API URL
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Add your API key
    params = {
        "market": "UK",
        "product": "DayAhead",
        "date": "2024-02-16",  # Modify to get real-time data
        "currency": "GBP"
    }

    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        hourly_prices = data.get("prices", [])  # Extract prices
        df = pd.DataFrame(hourly_prices, columns=["Hour", "Price (£/MWh)"])
        df["Hour"] = df["Hour"].astype(int)
        return df
    else:
        print(f"EPEX API Error: {response.status_code}")
        return None

# Function to fetch data from Nord Pool API
def fetch_nordpool_prices():
    """
    Fetch UK Day-Ahead Hourly Prices from Nord Pool API.
    API key may be required.
    """
    api_url = "https://www.nordpoolgroup.com/api/marketdata"  # Replace with actual API URL
    params = {
        "market": "UK",
        "date": "2024-02-16",  # Modify for real-time data
        "currency": "GBP"
    }

    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        hourly_prices = data.get("prices", [])  # Extract prices
        df = pd.DataFrame(hourly_prices, columns=["Hour", "Price (£/MWh)"])
        df["Hour"] = df["Hour"].astype(int)
        return df
    else:
        print(f"Nord Pool API Error: {response.status_code}")
        return None

# Function to fetch data from Bloomberg API (Requires Bloomberg Terminal)
def fetch_bloomberg_prices():
    """
    Fetch UK Day-Ahead Power Prices from Bloomberg API.
    Requires Bloomberg Terminal running.
    """
    try:
        df = blp.bdh(tickers="UKBL1 Index", flds="PX_LAST", start_date="2024-02-16", end_date="2024-02-16")
        df = df.reset_index()
        df.columns = ["Date", "Price (£/MWh)"]
        return df
    except Exception as e:
        print(f"Bloomberg API Error: {e}")
        return None

# Function to visualize the fetched data
def plot_prices(df, title):
    """
    Plots hourly UK power prices.
    """
    if df is not None and not df.empty:
        plt.figure(figsize=(10, 5))
        plt.plot(df["Hour"], df["Price (£/MWh)"], marker="o", linestyle="-")
        plt.xlabel("Hour of Day")
        plt.ylabel("Power Price (£/MWh)")
        plt.title(title)
        plt.xticks(range(0, 24))
        plt.grid(True)
        plt.show()
    else:
        print("No data available for plotting.")

# Main execution
if __name__ == "__main__":
    # Choose the API to fetch data
    source = "epex"  # Change to "nordpool" or "bloomberg" as needed

    if source == "epex":
        df = fetch_epex_spot_prices()
        title = "UK Day-Ahead Power Prices (EPEX SPOT)"
    elif source == "nordpool":
        df = fetch_nordpool_prices()
        title = "UK Day-Ahead Power Prices (Nord Pool)"
    elif source == "bloomberg":
        df = fetch_bloomberg_prices()
        title = "UK Day-Ahead Power Prices (Bloomberg)"
    else:
        print("Invalid source selected.")
        df = None

    # Plot data if available
    plot_prices(df, title)
import requests
import pandas as pd
import matplotlib.pyplot as plt

# -------- UPDATE YOUR API KEY + CITY ----------
API_KEY = "8c9fdad80c86647a6f89487152f3a550"      # <-- add your API key here
CITY = "Mumbai"               # You can change this
# ------------------------------------------------

# API URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extract weather info
    forecasts = data["list"]

    dates = []
    temps = []
    humidity = []

    for item in forecasts:
        dates.append(item["dt_txt"])
        temps.append(item["main"]["temp"])
        humidity.append(item["main"]["humidity"])

    # Create DataFrame
    df = pd.DataFrame({
        "Date-Time": dates,
        "Temperature (°C)": temps,
        "Humidity (%)": humidity
    })

    print(df.head())  # Preview in terminal

    # ★ Visualization Dashboard ★
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date-Time"], df["Temperature (°C)"], marker='o')
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Date-Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("API request failed. Check API key or internet.")
   
plt.figure(figsize=(12, 6))
plt.plot(df["Date-Time"], df["Temperature (°C)"], marker='o')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date-Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# --- Graph save in folder ---
plt.savefig("TemperatureGraph.png")   

plt.show()  # Graph window open
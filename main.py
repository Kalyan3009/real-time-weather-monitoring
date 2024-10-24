import time
import sys
from datetime import datetime, date, timedelta
from app.api_client import get_weather, get_forecast
from app.data_processor import store_weather_data, calculate_daily_summary, store_forecast_data
from app.visualization import plot_temperature_trends
from app.alert_system import trigger_alert
from app.database import init_db

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
breach_counts = {city: 0 for city in CITIES}
last_summary_date = None

def main(target_hour=None, days=None):
    """Main function to run weather monitoring system."""
    print("Initializing the database...")
    init_db()

    global last_summary_date

    print("Starting weather monitoring system...")
    while True:
        try:
            # Fetch weather and forecast data for each city
            for city in CITIES:
                print(f"Fetching weather for {city}...")
                weather_data = get_weather(city)
                store_weather_data(city, weather_data)
                check_consecutive_breaches(city, weather_data)

                print(f"Fetching forecast for {city}...")
                forecast_data = get_forecast(city)
                store_forecast_data(city, forecast_data)

            # Get the current date and hour for summary calculations
            current_date = date.today()
            current_hour = datetime.now().hour

            # Check if it's the target hour or midnight for summary calculations
            if (target_hour is not None and current_hour == target_hour) or \
               (target_hour is None and current_hour == 0):
                if last_summary_date != current_date:
                    summary_date = current_date - timedelta(days=0)
                    print(f"Calculating summaries for all cities on {summary_date}...")

                    # Calculate daily summaries and plot trends for all cities
                    for city in CITIES:
                        print(f"Calculating summary for {city} on {summary_date}...")
                        calculate_daily_summary(city, summary_date)
                        plot_temperature_trends(city)

                    last_summary_date = current_date  # Update the last summary date

            print("Sleeping for 1 minute...")
            time.sleep(60)  # Sleep to avoid frequent requests

        except Exception as e:
            print(f"[ERROR] An exception occurred: {e}")
            break

def check_consecutive_breaches(city, weather_data):
    """Check for consecutive threshold breaches and trigger alerts."""
    temp = weather_data["temp"]
    if temp > 28.0:
        breach_counts[city] += 1
        if breach_counts[city] >= 2:
            trigger_alert(city, f"Temperature alert! {temp}°C exceeded for two consecutive updates.")
    else:
        breach_counts[city] = 0

if __name__ == "__main__":
    # Get the target hour from command-line arguments, if provided
    target_hour = int(sys.argv[1]) if len(sys.argv) > 1 else None
    days = int(sys.argv[2]) if len(sys.argv) > 2 else None
    main(target_hour, days)
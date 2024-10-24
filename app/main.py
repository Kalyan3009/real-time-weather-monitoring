from app.api_client import get_weather, kelvin_to_celsius
from app.data_processor import store_weather_data, calculate_daily_summary
from app.alert_system import check_thresholds
from datetime import datetime
import time

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def main():
    while True:
        for city in CITIES:
            weather_data = get_weather(city)
            store_weather_data(city, weather_data)
            check_thresholds(city)

        # Perform daily summary calculation at midnight
        if datetime.now().hour == 0:
            for city in CITIES:
                calculate_daily_summary(city, datetime.today().date())

        time.sleep(300)  # 5-minute interval

if __name__ == "__main__":
    main()
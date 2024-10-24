import smtplib
from app.database import SessionLocal, WeatherData
from datetime import datetime
from matplotlib import pyplot as plt
THRESHOLDS = {
    "temperature": 28.0,
    "humidity": 80
}

def check_thresholds(city, weather_data):
    temp = weather_data["temp"]
    humidity = weather_data["humidity"]

    if temp > THRESHOLDS["temperature"]:
        trigger_alert(city, f"Temperature alert! {temp}°C exceeds {THRESHOLDS['temperature']}°C")

    if humidity > THRESHOLDS.get("humidity", 100):
        trigger_alert(city, f"Humidity alert! {humidity}% exceeds {THRESHOLDS['humidity']}%")

# def trigger_alert(city, message):
#     print(f"ALERT for {city}: {message}")

from datetime import datetime

# Global list to store alerts (or store in the database)
alert_log = []

def trigger_alert(city, message):
    """Trigger an alert and log it."""
    timestamp = datetime.now()
    alert = {"city": city, "message": message, "timestamp": timestamp}
    alert_log.append(alert)

    print(f"ALERT for {city}: {message} at {timestamp}")

def plot_alerts():
    """Plot a timeline of triggered alerts."""
    if not alert_log:
        print("No alerts to display.")
        return

    # Extract data for plotting
    times = [alert["timestamp"] for alert in alert_log]
    cities = [alert["city"] for alert in alert_log]
    messages = [alert["message"] for alert in alert_log]

    # Create a scatter plot for alerts
    plt.figure(figsize=(10, 6))
    plt.scatter(times, cities, marker='o', color='red')

    for i, msg in enumerate(messages):
        plt.annotate(msg, (times[i], cities[i]), textcoords="offset points", xytext=(0, 5), ha='center')

    plt.xlabel('Time')
    plt.ylabel('City')
    plt.title('Triggered Alerts Timeline')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    # Optional: Send email alert (Replace with your SMTP details)
    # with smtplib.SMTP("smtp.gmail.com", 587) as server:
    #     server.starttls()
    #     server.login("your_email@gmail.com", "your_password")
    #     message = f"Subject: Weather Alert\n\n{city} has reached {temp}°C."
    #     server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", message)

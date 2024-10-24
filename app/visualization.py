import matplotlib.pyplot as plt
from app.database import SessionLocal, DailySummary

def plot_temperature_trends(city):
    """Plot historical temperature trends for a city."""
    session = SessionLocal()
    summaries = session.query(DailySummary).filter(DailySummary.city == city).all()

    if not summaries:
        print(f"No data available for {city}.")
        return

    # Extract data for plotting
    dates = [s.date for s in summaries]
    avg_temps = [s.avg_temp for s in summaries]
    max_temps = [s.max_temp for s in summaries]
    min_temps = [s.min_temp for s in summaries]

    # Plot the temperature trends
    plt.figure(figsize=(10, 6))
    plt.plot(dates, avg_temps, label='Average Temperature', marker='o')
    plt.plot(dates, max_temps, label='Max Temperature', linestyle='--', marker='x')
    plt.plot(dates, min_temps, label='Min Temperature', linestyle=':', marker='s')

    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Trends for {city}')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    print(f"Displaying plot for {city}...")
    
    # Force plot to show in blocking mode
    plt.show(block=True)

    session.close()
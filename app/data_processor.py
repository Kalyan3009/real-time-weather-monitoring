from app.database import SessionLocal, WeatherData, DailySummary, ForecastData
from sqlalchemy import func
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.exc import IntegrityError
from app.database import SessionLocal, WeatherData, DailySummary
from datetime import datetime, timezone
from app.database import SessionLocal, WeatherData, DailySummary
from sqlalchemy import func, and_

def store_weather_data(city, weather_data):
    session = SessionLocal()

    try:
        timestamp = datetime.now()  # Use the current timestamp
        print(f"[DEBUG] Storing weather data for {city} at {timestamp}")

        new_record = WeatherData(
            city=city,
            temp=weather_data["temp"],
            feels_like=weather_data["feels_like"],
            humidity=weather_data["humidity"],
            wind_speed=weather_data["wind_speed"],
            main=weather_data["main"],
            timestamp=timestamp
        )
        session.add(new_record)
        session.commit()  # Commit the transaction
        print(f"[SUCCESS] Weather data for {city} stored successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to store weather data: {e}")
        session.rollback()  # Rollback the transaction if there's an error
    finally:
        session.close()

def store_forecast_data(city, forecast_data):
    """Store or update forecast data for the next 5 days."""
    session = SessionLocal()

    try:
        for forecast in forecast_data:
            # Create the INSERT statement
            stmt = insert(ForecastData).values(
                city=city,
                forecast_date=forecast["date"],
                min_temp=forecast["min_temp"],
                max_temp=forecast["max_temp"],
                humidity=forecast["humidity"],
                weather_condition=forecast["weather_condition"]
            )

            # Use the ON DUPLICATE KEY UPDATE clause
            stmt = stmt.on_duplicate_key_update(
                min_temp=stmt.inserted.min_temp,
                max_temp=stmt.inserted.max_temp,
                humidity=stmt.inserted.humidity,
                weather_condition=stmt.inserted.weather_condition
            )

            # Execute the statement
            session.execute(stmt)

        session.commit()
        print(f"Forecast data stored successfully for {city}.")
    except Exception as e:
        print(f"An error occurred while storing forecast data: {e}")
        session.rollback()
    finally:
        session.close()

def calculate_daily_summary(city, summary_date):
    """Calculate and store the daily weather summary."""
    print(f"[DEBUG] Calculating summary for {city} on {summary_date}...")

    session = SessionLocal()

    # Define the time range for the day
    start_of_day = datetime.combine(summary_date, datetime.min.time())
    end_of_day = datetime.combine(summary_date, datetime.max.time())

    # Query all records for the given city within the date range
    records = session.query(
        WeatherData.temp, WeatherData.humidity, WeatherData.main
    ).filter(
        and_(
            WeatherData.city == city,
            WeatherData.timestamp >= start_of_day,
            WeatherData.timestamp <= end_of_day
        )
    ).all()

    print(f"[DEBUG] Retrieved {len(records)} records for {city} on {summary_date}.")

    if records:
        # Calculate summary values
        avg_temp = sum(r[0] for r in records) / len(records)
        max_temp = max(r[0] for r in records)
        min_temp = min(r[0] for r in records)
        avg_humidity = sum(r[1] for r in records) / len(records)

        weather_conditions = [r[2] for r in records]
        dominant_weather = max(set(weather_conditions), key=weather_conditions.count)

        # Create or update the daily summary
        summary = DailySummary(
            city=city,
            date=summary_date,
            avg_temp=avg_temp,
            max_temp=max_temp,
            min_temp=min_temp,
            avg_humidity=avg_humidity,
            dominant_weather=dominant_weather
        )

        try:
            session.merge(summary)  # Insert or update if it exists
            session.commit()
            print(f"[SUCCESS] Summary stored for {city} on {summary_date}.")
        except Exception as e:
            print(f"[ERROR] Failed to store summary for {city}: {e}")
            session.rollback()
    else:
        print(f"[WARNING] No data available to summarize for {city} on {summary_date}.")

    session.close()
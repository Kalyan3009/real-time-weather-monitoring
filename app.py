from flask import Flask, jsonify, render_template
from flask_cors import CORS
from app.database import SessionLocal, WeatherData

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def index():
    """Serve the dashboard HTML."""
    return render_template("dashboard.html")

@app.route("/api/weather_data", methods=["GET"])
def get_weather_data():
    """Fetch and return weather data."""
    session = SessionLocal()
    try:
        weather_records = session.query(WeatherData).all()
        data = [
            {
                "city": record.city,
                "temp": record.temp,
                "feels_like": record.feels_like,
                "humidity": record.humidity,
                "wind_speed": record.wind_speed,
                "main": record.main,
                "timestamp": record.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            for record in weather_records
        ]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
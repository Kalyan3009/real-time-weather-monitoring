from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# MySQL Configuration
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB", "weather_monitor")

# Database URL
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    temp = Column(Float, nullable=False)
    feels_like = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    wind_speed = Column(Float, nullable=False)
    main = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False)

class DailySummary(Base):
    __tablename__ = 'daily_summary'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    avg_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    min_temp = Column(Float, nullable=False)
    avg_humidity = Column(Integer, nullable=False)
    dominant_weather = Column(String(50), nullable=False)

class ForecastData(Base):
    __tablename__ = 'forecast_data'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    forecast_date = Column(Date, nullable=False)
    min_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    weather_condition = Column(String(50), nullable=False)

# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
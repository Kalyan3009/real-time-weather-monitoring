@echo off
:: Set MySQL credentials and other configurations
set MYSQL_USER=root
set MYSQL_HOST=localhost
set DATABASE_NAME=weather_monitor

:: Create SQL script directly
echo CREATE DATABASE IF NOT EXISTS %DATABASE_NAME%; > temp_script.sql
echo USE %DATABASE_NAME%; >> temp_script.sql

:: Create weather_data table
echo CREATE TABLE IF NOT EXISTS weather_data ( >> temp_script.sql
echo     id INT AUTO_INCREMENT PRIMARY KEY, >> temp_script.sql
echo     city VARCHAR(50) NOT NULL, >> temp_script.sql
echo     temp FLOAT NOT NULL, >> temp_script.sql
echo     feels_like FLOAT NOT NULL, >> temp_script.sql
echo     humidity INT NOT NULL, >> temp_script.sql
echo     wind_speed FLOAT NOT NULL, >> temp_script.sql
echo     main VARCHAR(50) NOT NULL, >> temp_script.sql
echo     timestamp DATETIME NOT NULL, >> temp_script.sql
echo     INDEX (city), >> temp_script.sql
echo     INDEX (timestamp) >> temp_script.sql
echo ); >> temp_script.sql

:: Create daily_summary table
echo CREATE TABLE IF NOT EXISTS daily_summary ( >> temp_script.sql
echo     id INT AUTO_INCREMENT PRIMARY KEY, >> temp_script.sql
echo     city VARCHAR(50) NOT NULL, >> temp_script.sql
echo     date DATE NOT NULL, >> temp_script.sql
echo     avg_temp FLOAT NOT NULL, >> temp_script.sql
echo     max_temp FLOAT NOT NULL, >> temp_script.sql
echo     min_temp FLOAT NOT NULL, >> temp_script.sql
echo     avg_humidity INT NOT NULL, >> temp_script.sql
echo     dominant_weather VARCHAR(50) NOT NULL, >> temp_script.sql
echo     UNIQUE (city, date) >> temp_script.sql
echo ); >> temp_script.sql

:: Create forecast_data table
echo CREATE TABLE IF NOT EXISTS forecast_data ( >> temp_script.sql
echo     id INT AUTO_INCREMENT PRIMARY KEY, >> temp_script.sql
echo     city VARCHAR(50) NOT NULL, >> temp_script.sql
echo     forecast_date DATE NOT NULL, >> temp_script.sql
echo     min_temp FLOAT NOT NULL, >> temp_script.sql
echo     max_temp FLOAT NOT NULL, >> temp_script.sql
echo     humidity INT NOT NULL, >> temp_script.sql
echo     weather_condition VARCHAR(50) NOT NULL, >> temp_script.sql
echo     UNIQUE (city, forecast_date) >> temp_script.sql
echo ); >> temp_script.sql

:: Execute the SQL commands using MySQL
echo Executing SQL script...
mysql -u %MYSQL_USER% -h %MYSQL_HOST% < temp_script.sql

:: Clean up temporary files
echo Cleaning up...
del temp_script.sql

echo Database setup completed.
pause
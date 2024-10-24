
# Weather Monitoring Dashboard

This project is a **Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates** that provides **real-time weather data** visualization using **Flask** and **Chart.js**. It displays trends for **temperature and humidity** along with tabular weather data for multiple cities.

---

### Project Features

- Real-time weather data visualization.
- Temperature and humidity **line charts** using Chart.js.
- **Responsive dashboard** built with Bootstrap.
- **Data storage** in MySQL/MariaDB database.
- Integration with **XAMPP Server** for MySQL and Apache.

---

### Technologies Used

- **Python** (Flask Framework)
- **Chart.js** for frontend graphs
- **Bootstrap** for styling
- **MariaDB/MySQL** as the database
- **XAMPP Server** to host MySQL and Apache

---

### Prerequisites

1. **XAMPP Server**: [Download XAMPP](https://www.apachefriends.org/download.html)  
   Ensure **Apache** and **MySQL** services are running.

2. **Python 3.x**: [Download Python](https://www.python.org/downloads/)

3. Install Python dependencies:
   ```bash
   pip install flask flask-cors mysql-connector-python
   ```

---

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Start XAMPP Server**:
   - Open **XAMPP Control Panel** and **start Apache and MySQL**.

3. **Create MySQL Database**:
   - Go to **phpMyAdmin**: [http://localhost/phpmyadmin](http://localhost/phpmyadmin)
   - Create a **database named `weather_monitor`**.
   - Run the following SQL to create the `weather_data` table:
     ```sql
     CREATE TABLE IF NOT EXISTS weather_data (
         id INT AUTO_INCREMENT PRIMARY KEY,
         city VARCHAR(50) NOT NULL,
         temp FLOAT NOT NULL,
         feels_like FLOAT NOT NULL,
         humidity INT NOT NULL,
         wind_speed FLOAT NOT NULL,
         main VARCHAR(50) NOT NULL,
         timestamp DATETIME NOT NULL,
         INDEX (city),
         INDEX (timestamp)
     );
     ```

4. **Set Up Flask App**:
   - Ensure the **static files** (`bootstrap.min.css`, `chart.js`, `chartjs-adapter-date-fns.js`) are in the **`static` folder**.
   - Place **HTML templates** (e.g., `dashboard.html`) in the **`templates` folder**.

5. **Run the Flask App**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   - Visit the dashboard at:  
     [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

7. **Verify the API**:
   - Check the API endpoint:  
     [http://127.0.0.1:5000/api/weather_data](http://127.0.0.1:5000/api/weather_data)

---

### Project Folder Structure

```
/your_project
│
├── app/
│   ├── __init__.py
│   ├── api_client.py
│   ├── data_processor.py
│   ├── alert_system.py
│   ├── database.py
│   └── models.py
├── templates/
│   └── dashboard.html
├── static/
│   ├── bootstrap.min.css
│   ├── chart.js
│   └── chartjs-adapter-date-fns.js
├── app.py
└── README.md
```

---

### How It Works

1. **Backend**:  
   The Flask app fetches data from a **MariaDB/MySQL database** via the `/api/weather_data` API.

2. **Frontend**:  
   The dashboard uses **Chart.js** to render temperature and humidity line charts and Bootstrap for styling.

3. **Database**:  
   Weather data is stored in the `weather_data` table, which is queried to populate the dashboard.

---

### Troubleshooting

1. **Database Errors**:
   - Ensure **Apache** and **MySQL** services are running in XAMPP.
   - Verify the **database credentials** in your `database.py`.

2. **Graph Not Displaying**:
   - Check the browser **console (F12)** for JavaScript errors.
   - Ensure **static files** are correctly loaded.

3. **CORS Issues**:
   - Make sure **CORS** is enabled in Flask using:
     ```python
     from flask_cors import CORS
     CORS(app)
     ```

---


This **README.md** covers everything from installation to troubleshooting. If you need further help, feel free to contact me through the repository’s issue tracker.

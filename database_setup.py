import sqlite3


def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('weather_data_demo.db')
    cursor = conn.cursor()

    # Create 'locations' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            location_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            country TEXT NOT NULL,
            region TEXT
        );
    ''')

    # Create 'forecasts' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS forecasts (
            forecast_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            max_temp REAL,
            min_temp REAL,
            avg_temp REAL,
            total_precipitation REAL,
            max_wind_speed REAL,
            FOREIGN KEY(location_id) REFERENCES locations(location_id)
        )
    ''')

    # Create 'conditions' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conditions (
            condition_id INTEGER PRIMARY KEY AUTOINCREMENT,
            forecast_id INTEGER NOT NULL,
            time TEXT NOT NULL,
            temperature REAL,
            wind_speed REAL,
            precipitation REAL,
            cloud_cover INTEGER,
            humidity INTEGER,
            pressure REAL,
            icon TEXT,
            FOREIGN KEY(forecast_id) REFERENCES forecasts(forecast_id)
        )
    ''')

    # Create 'astro' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS astro (
            astro_id INTEGER PRIMARY KEY AUTOINCREMENT,
            forecast_id INTEGER NOT NULL,
            sunrise TEXT,
            sunset TEXT,
            moonrise TEXT,
            moonset TEXT,
            FOREIGN KEY(forecast_id) REFERENCES forecasts(forecast_id)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()

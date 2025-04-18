# MetraWeather Desktop Application

**MetraWeather** is a Python-based desktop application that provides real-time weather forecasts and historical weather data for locations across the Philippines. Leveraging data from the WeatherAPI, MetraWeather offers users a sleek interface to view up-to-date weather conditions, including temperature, wind speed, humidity, and precipitation.

![MetraWeather Screenshot](screenshot.png) <!-- Replace with actual screenshot if available -->

## 🌟 Features

- **Current Weather Forecasts**: Access 7-day weather forecasts for any location in the Philippines, complete with daily maximum and minimum temperatures, average temperatures, and chances of precipitation.
- **Historical Weather Data**: Retrieve and review past weather conditions by selecting a specific date, aiding in research and planning.
- **Data Persistence**: Weather data is stored in a local SQLite database for offline access and historical reference.
- **Customizable Locations**: Input any city or region within the Philippines to receive localized weather information.
- **User-friendly Interface**: Designed with simplicity in mind, providing an intuitive and straightforward user experience.
- **Alert System**: Receive notifications for severe weather conditions in your selected locations.

## 🛠 Technologies Used

- **Python 3**: Core programming language for application development.
- **Tkinter**: Standard GUI library for building the desktop interface.
- **SQLite**: Lightweight database for storing and retrieving weather data.
- **WeatherAPI.com**: Source of all weather data presented by the application.

## 🚀 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jayelcee/Weather_System_with_GUI.git
   cd Weather_System_with_GUI
   ```

2. **Install Dependencies**

   Ensure you have Python 3 installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain WeatherAPI Key**

   - Sign up at [WeatherAPI.com](https://www.weatherapi.com/) to obtain a free API key.
   - Replace the placeholder in the code with your actual API key.

4. **Run the Application**

   ```bash
   python main.py
   ```

## 🖼 Screenshots

![Main Interface](assets/screenshot_main.png)
*Main interface displaying current weather information.*

![Historical Data](assets/screenshot_history.png)
*View of historical weather data for a selected date.*

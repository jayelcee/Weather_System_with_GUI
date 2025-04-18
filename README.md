# MetraWeather Desktop Application

**MetraWeather** is a Python-based desktop application that provides real-time weather forecasts and historical weather data for locations across the world. Leveraging data from the WeatherAPI, MetraWeather offers users a sleek interface to view up-to-date weather conditions, including temperature, wind speed, humidity, and precipitation.

## 🧠 Program Flowchart
![flowchart](https://github.com/user-attachments/assets/6ed542a2-4f78-44e8-b2fe-99cb72de1285)


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

## 🎬 Video Demonstration
https://youtu.be/UABt6QdWHMY

## 📑 Detailed Documentation:
https://github.com/jayelcee/Weather_System_with_GUI/blob/master/Project%20Documentation.pdf

## 👩🏻‍💻 Developers
- Altares, Cyril John
- Camasura, Jasmine L.
- Cudiamat, Ma. Angeline C.
- Jestingor, Neal Tracy D.

## 🚀 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jayelcee/Weather_System_with_GUI.git
   cd Weather_System_with_GUI
   ```

2. **Install Dependencies**

   Ensure you have Python 3 installed. Then, install the required packages.  

   Create a virtual environment to isolate your project dependencies.
   ```bash
   python3 -m venv venv
   ```
   Activate the virtual environment.
   ```bash
   source venv/bin/activate
   ```
   Install the required dependencies inside the virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   python main.py
   ```

## 🖼 Screenshots

![current1](https://github.com/user-attachments/assets/cc4c86cb-2557-48b5-a3b8-22e3e3a3b127)  
   *View of current weather information.*

![historical](https://github.com/user-attachments/assets/6fab3574-96d3-4f3b-b101-fa5e44a680ed)  
   *View of historical weather data for a selected date.*

![alert1](https://github.com/user-attachments/assets/7c7f490e-ad7b-48f0-8787-5d067fc23c20)
![alert2](https://github.com/user-attachments/assets/dc27be6c-880a-4a99-b71c-f360dda0d704)  
   *Display alert details if there are.*

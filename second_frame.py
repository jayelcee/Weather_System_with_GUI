import customtkinter as ctk
from weather_frame import WeatherFrame
from detail_frame import DetailFrame
from data_frame import DataFrame
from alert import Alert
from threading import Thread
from datetime import datetime, timedelta
from weather_api import WeatherApi
from time import sleep
from PIL import Image


class SecondFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs): # Initialize customtkinter UI elements for previous forecast
        super().__init__(master, **kwargs)

        self.data = {}
        self.count = 0

        self.search_entry = ctk.CTkEntry(master=self, placeholder_text="Search location...", width=200, height=50,
                                         corner_radius=8, font=("Arial", 16))
        self.search_entry.grid(row=0, column=0, padx=[0, 420], pady=[75, 0])
        self.search_entry.bind("<Return>", self.search)

        self.date_entry = ctk.CTkEntry(master=self, placeholder_text="Date: YYYY-MM-DD", width=200, height=50,
                                         corner_radius=8, font=("Arial", 16))
        self.date_entry.grid(row=0, column=0, pady=[75, 0])
        self.date_entry.bind("<Return>", self.search)

        self.message_label = ctk.CTkLabel(master=self, text="", font=("Arial Bold", 12), anchor="center",
                                          text_color="red")
        self.message_label.grid(row=0, column=0, padx=[375, 0], pady=[95, 10])

        self.grid_columnconfigure(0, weight=1)

        self.date_label = ctk.CTkLabel(master=self, text="Today's Weather Forecast", font=("Arial Bold", 24))
        self.date_label.grid(row=2, column=0, padx=20, pady=[10, 10], sticky="w")

        self.detail_frame = DetailFrame(master=self)
        self.detail_frame.grid(row=3, column=0, padx=20, pady=[0, 20], sticky="nsew")

        self.data_frame = DataFrame(master=self)
        self.data_frame.grid(row=4, column=0, padx=20, pady=[0, 5], sticky="nsew")

    def content(self): # It takes data to be displayed, can be called to refresh and display another set of data
        self.date_label.configure(text=self.set_label_text())
        self.detail_frame.content(self.data)
        self.data_frame.content(self.data)

    def set_label_text(self): # It displays the date status
        current_date = datetime.now().date() # Get current date
        formatted_date = datetime.strptime(self.data["forecast"]["forecastday"][self.count]["date"], "%Y-%m-%d").date() # Set format for date
        date_name = formatted_date.strftime("%A") # Get name of day (Monday, Tuesday, etc.)
        month = formatted_date.strftime('%B') # Get name of the month

        location = self.data["location"]
        name = location["name"]
        region = location["region"]
        country = location["country"]

        if formatted_date == current_date: # If date of data is same in current_date
            return f"Today's Weather Forecast - {name}, {region}, {country}"
        elif formatted_date == current_date - timedelta(days=1): # If date of data is same in yesterday (current_date - 1)
            return f"Yesterday's Weather Forecast - {name}, {region}, {country}"
        elif formatted_date == current_date + timedelta(days=1): # If date of data is same in tomorrow (current_date + 1)
            return f"Tomorrow's Weather Forecast - {name}, {region}, {country}"
        else:
            return f"{date_name} {str(formatted_date).split('-')[2]} {month} Weather Forecast - {name}, {region}, {country}"

    def delete_message_text(self): # Delete message after searching
        sleep(5)
        self.message_label.configure(text="")

    def search(self, event): # Start search in a thread; it means API will run in background to avoid lagging/overloading the system
        Thread(target=self.request).start()

    def request(self): # Search request to call API to get previous forecast
        location = self.search_entry.get()
        date = self.date_entry.get()

        if location != "" or date != "": # Check if CTK.entry if one of them is empty
            try:
                self.data = WeatherApi().request_prev_forecast(location, date)
                self.count = 0
                self.content()

            except Exception as e: # Check if errors
                print(f"{e}")
                if "HTTP" in str(e): # If the API takes time to respond
                    self.message_label.configure(text="Timeout Error")
                elif "forecast" in str(e): # If the date is over or below the date in API's server
                    self.message_label.configure(text="Invalid Date")
                else: # If no such location is found 
                    self.message_label.configure(text="No Location Found")

                Thread(target=self.delete_message_text).start()

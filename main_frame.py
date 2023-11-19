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


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.data = {}
        self.count = 0
        self.alert_toplvl = None

        self.search_entry = ctk.CTkEntry(master=self, placeholder_text="Search location...", width=200, height=50,
                                         corner_radius=8, font=("Arial", 16))
        self.search_entry.grid(row=0, column=0, pady=[10, 0])
        self.search_entry.bind("<Return>", self.search)

        self.message_label = ctk.CTkLabel(master=self, text="", font=("Arial Bold", 12), anchor="center",
                                          text_color="red")
        self.message_label.grid(row=0, column=0, padx=[375, 0], pady=[20, 10])

        self.alert_image = ctk.CTkImage(Image.open("alert.png"), size=(30, 30))
        self.alert_label = ctk.CTkLabel(master=self, text="", image=self.alert_image, anchor="center")
        self.alert_label.grid(row=0, column=0, padx=[0, 250], pady=[20, 10])
        self.alert_label.bind("<Button-1>", self.alert)

        self.grid_columnconfigure(0, weight=1)

        self.weather_frame = WeatherFrame(master=self)
        self.weather_frame.grid(row=1, column=0, padx=20, pady=[20, 5], sticky="nsew")

        self.date_label = ctk.CTkLabel(master=self, text="Today's Weather Forecast", font=("Arial Bold", 24))
        self.date_label.grid(row=2, column=0, padx=20, pady=[10, 10], sticky="w")

        self.detail_frame = DetailFrame(master=self)
        self.detail_frame.grid(row=3, column=0, padx=20, pady=[0, 20], sticky="nsew")

        self.data_frame = DataFrame(master=self)
        self.data_frame.grid(row=4, column=0, padx=20, pady=[0, 5], sticky="nsew")

        self.previous_btn = ctk.CTkButton(master=self, border_width=0, corner_radius=8, height=45, width=150,
                                          text="Previous Day",
                                          command=self.previous, state="disabled")
        self.previous_btn.grid(row=5, column=0, padx=340, pady=[0, 10], sticky="w")

        self.next_btn = ctk.CTkButton(master=self, border_width=0, corner_radius=8, height=45, width=150,
                                      text="Next Day",
                                      command=self.next, state="normal")
        self.next_btn.grid(row=5, column=0, padx=340, pady=[0, 10], sticky="e")

    def content(self):
        self.weather_frame.grid()
        self.weather_frame.content(self.data)
        self.date_label.configure(text=self.set_label_text())
        self.detail_frame.content(self.data)
        self.data_frame.content(self.data)
        self.search_entry.grid_configure(pady=[10, 0])
        self.previous_btn.configure(state="disabled")
        self.previous_btn.configure(state="normal")

    def next(self):
        if self.data:
            self.count += 1
            self.detail_frame.content(self.data, self.count)
            self.data_frame.content(self.data, self.count)
            self.date_label.configure(text=self.set_label_text())

            self.search_entry.grid_configure(pady=[75, 10])

            if self.count < 7:
                self.previous_btn.configure(state="normal")

            if self.count == 6:
                self.next_btn.configure(state="disabled")

            if self.count > 0:
                self.weather_frame.grid_remove()

    def previous(self):
        if self.data:
            self.count -= 1
            self.detail_frame.content(self.data, self.count)
            self.data_frame.content(self.data, self.count)
            self.date_label.configure(text=self.set_label_text())

            if self.count < 7:
                self.next_btn.configure(state="normal")

            if self.count == 0:
                self.previous_btn.configure(state="disabled")
                self.weather_frame.grid()
                self.search_entry.grid_configure(pady=[10, 0])

    def set_label_text(self):
        current_date = datetime.now().date()
        formatted_date = datetime.strptime(self.data["forecast"]["forecastday"][self.count]["date"], "%Y-%m-%d").date()
        date_name = formatted_date.strftime("%A")
        month = formatted_date.strftime('%B')

        location = self.data["location"]
        name = location["name"]
        country = location["country"]

        if formatted_date == current_date:
            return f"Today's Weather Forecast - {name}, {country}"
        elif formatted_date == current_date - timedelta(days=1):
            return f"Yesterday's Weather Forecast - {name}, {country}"
        elif formatted_date == current_date + timedelta(days=1):
            return f"Tomorrow's Weather Forecast - {name}, {country}"
        else:
            return f"{date_name} {str(formatted_date).split('-')[2]} {month} Weather Forecast - {name}, {country}"

    def delete_message_text(self):
        sleep(5)
        self.message_label.configure(text="")

    def search(self, event):
        Thread(target=self.request).start()

    def request(self):
        location = self.search_entry.get()

        if location != "":
            try:
                self.data = WeatherApi().request_forecast(location)
                self.count = 0
                self.content()

            except Exception as e:
                if "HTTP" in str(e):
                    self.message_label.configure(text="Timeout Error")
                else:
                    self.message_label.configure(text="No Location Found")

                Thread(target=self.delete_message_text).start()

    def alert(self, event):
        if self.alert_toplvl is None or not self.alert_toplvl.winfo_exists():
            self.alert_toplvl = Alert(master=self.master, data=self.data)
        else:
            self.alert_toplvl.destroy()
            self.alert_toplvl = Alert(master=self.master, data=self.data)

import customtkinter as ctk
from PIL import Image


class DetailFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_columnconfigure((2, 3, 4, 5, 6), weight=0)

        self.sunrise_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12))
        self.sunrise_label.grid(row=0, column=0, padx=[20, 3], pady=10, sticky="w")

        self.moonrise_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12))
        self.moonrise_label.grid(row=0, column=1, padx=3, pady=10, sticky="w")

        self.max_temp_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12), width=75)
        self.max_temp_label.grid(row=0, column=2, padx=3, pady=10, sticky="nsew")

        self.min_temp_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12), width=75)
        self.min_temp_label.grid(row=0, column=3, padx=3, pady=10, sticky="nsew")

        self.avg_temp_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12), width=75)
        self.avg_temp_label.grid(row=0, column=4, padx=3, pady=10, sticky="nsew")

        self.precip_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12), width=75)
        self.precip_label.grid(row=0, column=5, padx=3, pady=10, sticky="nsew")

        self.max_wind_label = ctk.CTkLabel(master=self, text="-", font=("Arial Bold", 12), width=75)
        self.max_wind_label.grid(row=0, column=6, padx=[3, 20], pady=10, sticky="nsew")

    def content(self, data, count=0):
        if data:
            forecast_day = data["forecast"]["forecastday"][count]

            astro = forecast_day["astro"]
            day = forecast_day["day"]

            sunrise = astro["sunrise"]
            sunset = astro["sunset"]
            moonrise = astro["moonrise"]
            moonset = astro["moonset"]

            maxtemp_c = day["maxtemp_c"]
            mintemp_c = day["mintemp_c"]
            avgtemp_c = day["avgtemp_c"]
            totalprecip_mm = day["totalprecip_mm"]
            maxwind_kph = day["maxwind_kph"]

            self.sunrise_label.configure(text=f" Sunrise: {sunrise}\nSunset: {sunset}")
            self.moonrise_label.configure(text=f" Moonrise: {moonrise}\nMoonSet: {moonset}")
            self.max_temp_label.configure(text=f" Max: \n{maxtemp_c} °C")
            self.min_temp_label.configure(text=f" Min: \n{mintemp_c} °C")
            self.avg_temp_label.configure(text=f" Avg: \n{avgtemp_c} °C")
            self.precip_label.configure(text=f" Precip: \n{totalprecip_mm} mm")
            self.max_wind_label.configure(text=f" Max Wind: \n{maxwind_kph} kph")

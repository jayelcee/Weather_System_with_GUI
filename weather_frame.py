import customtkinter as ctk
from PIL import Image


class WeatherFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.condition_image = ctk.CTkImage(Image.open("weather_image/day/113.png"), size=(150,150))

        self.condition_label = ctk.CTkLabel(master=self, text="-", image=self.condition_image, anchor="center")
        self.condition_label.grid(row=0,rowspan=4, column=0, padx=[50, 0], pady=10)

        self.condition_text = ctk.CTkLabel(master=self, text="-", anchor="center", font=("Arial Bold", 24))
        self.condition_text.grid(row=0,rowspan=4, column=1, columnspan=6, padx=[5,10], pady=10, sticky="w")

        self.wind_label = ctk.CTkLabel(master=self, text="-", anchor="center", font=("Arial Bold", 16))
        self.wind_label.grid(row=0, column=7, padx=[5, 50], pady=[30, 0], sticky="nsew")

        self.precip_label = ctk.CTkLabel(master=self, text="-", anchor="center", font=("Arial Bold", 16))
        self.precip_label.grid(row=1, column=7, padx=[5, 50], sticky="nsew")

        self.pressure_label = ctk.CTkLabel(master=self, text="-", anchor="center", font=("Arial Bold", 16))
        self.pressure_label.grid(row=2, column=7, padx=[5, 50], sticky="nsew")

        self.temp_label = ctk.CTkLabel(master=self, text="-", anchor="center", font=("Arial Bold", 36))
        self.temp_label.grid(row=3, column=7, padx=[5, 50], pady=[0, 30], sticky="nsew")

    def content(self, data):
        if data:
            current = data["current"]

            temperature = current["temp_c"]
            is_day = "day" if current["is_day"] else "night"

            condition = current["condition"]
            condition_text = condition["text"]
            condition_image = Image.open(f"weather_image/{is_day}/{condition['icon'].split('/')[6]}")

            wind_kph = current["wind_kph"]
            precip_mm = current["precip_mm"]
            cloud = current["cloud"]
            humidity = current["humidity"]
            pressure_in = current["pressure_in"]

            self.condition_image.configure(dark_image=condition_image, light_image=condition_image)
            self.condition_text.configure(text=condition_text)

            self.wind_label.configure(text=f"Wind: {wind_kph} kph")
            self.precip_label.configure(text=f"Precip: {precip_mm} mm")
            self.pressure_label.configure(text=f"Pressure: {pressure_in} in")
            self.temp_label.configure(text=f"{temperature} °C")
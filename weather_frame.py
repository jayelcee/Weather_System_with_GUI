import customtkinter as ctk
from statistics import mean
from PIL import Image


class WeatherFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs): # Initialize customtkinter UI elements
        super().__init__(master, **kwargs)

        self.master = master

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.condition_image = ctk.CTkImage(Image.open("weather_image/day/113.png"), size=(150, 150))

        self.condition_label = ctk.CTkLabel(master=self, text="-", image=self.condition_image, anchor="center")
        self.condition_label.grid(row=0, rowspan=4, column=0, padx=[50, 0], pady=10)

        self.condition_text = ctk.CTkLabel(master=self, text="-", anchor="center", font=("Arial Bold", 24))
        self.condition_text.grid(row=0, rowspan=4, column=1, columnspan=6, padx=[5, 10], pady=10, sticky="w")

        self.wind_label = ctk.CTkLabel(master=self, text="-", anchor="e", font=("Arial Bold", 16))
        self.wind_label.grid(row=0, column=7, padx=[5, 50], pady=[30, 0], sticky="nsew")

        self.precip_label = ctk.CTkLabel(master=self, text="-", anchor="e", font=("Arial Bold", 16))
        self.precip_label.grid(row=1, column=7, padx=[5, 50], sticky="nsew")

        self.pressure_label = ctk.CTkLabel(master=self, text="-", anchor="e", font=("Arial Bold", 16))
        self.pressure_label.grid(row=2, column=7, padx=[5, 50], sticky="nsew")

        self.temp_label = ctk.CTkLabel(master=self, text="-", anchor="e", font=("Arial Bold", 36))
        self.temp_label.grid(row=3, column=7, padx=[5, 50], pady=[0, 30], sticky="nsew")

    def content(self, data, count=0, is_current_day=True): # It takes data to be displayed, can be called to refresh and display another set of data
        if data: # If there is data from the API display it
            if is_current_day:
                weather_data = data['current']
                pressure_in = weather_data.get("pressure_in", "N/A")
            else:
                forecast_day_data = data["forecast"]["forecastday"][count]
                weather_data = forecast_day_data["day"]
                hours = forecast_day_data["hour"]
                pressures = [hour["pressure_in"] for hour in hours if hour.get("pressure_in") is not None]
                pressure_in = mean(pressures) if pressures else "N/A"

            condition = weather_data["condition"]
            condition_text = condition["text"]
            icon_path = condition['icon'].split('/')[-1]
            condition_icon_path = f"weather_image/day/{icon_path}"
            condition_icon = Image.open(condition_icon_path)

            wind_kph = weather_data.get("wind_kph", weather_data.get("maxwind_kph", "N/A"))
            precip_mm = weather_data.get("precip_mm", weather_data.get("totalprecip_mm", "N/A"))
            temperature = weather_data.get("temp_c", weather_data.get("avgtemp_c", "N/A"))

            self.condition_image.configure(dark_image=condition_icon, light_image=condition_icon)
            self.condition_text.configure(text=condition_text)
            self.wind_label.configure(text=f"Max Wind: {wind_kph} kph")
            self.precip_label.configure(text=f"Total Precipitation: {precip_mm} mm")
            self.pressure_label.configure(
                text=f"Average Pressure: {pressure_in:.2f} in" if isinstance(pressure_in, float) else f"Pressure: {pressure_in}"
            )
            
            self.temp_label.configure(text=f"{temperature} °C")

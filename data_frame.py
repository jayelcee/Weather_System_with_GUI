import customtkinter as ctk
from PIL import Image
from datetime import datetime


class DataFrame(ctk.CTkFrame): # Initialize customtkinter UI elements for forecast
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.count = 0

        headers = ["Icon", "Temperature", "Wind", "Precipitation", "Cloud", "Humidity", "Pressure"]

        for index, header in enumerate(headers, start=1): # Display headers vertically
            header_label = ctk.CTkLabel(master=self, text=header, fg_color="gray", height=50, width=100,
                                        corner_radius=3, font=("Arial Bold", 12))
            header_label.grid(row=index, column=0, padx=[9, 2], pady=[2, 2])

        self.bg_color = ("white", "gray75")
        self.text_color = "black"

        for i in range(1, 9): # Set default display as empty
            self.date_label = ctk.CTkLabel(master=self, text="N/a", fg_color="gray", height=50, width=100,
                                           corner_radius=3, font=("Arial Bold", 12))
            self.date_label.grid(row=0, column=i, padx=[2, 2], pady=[9, 2], sticky="nsew")

            self.icon_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color, fg_color=self.bg_color,
                                           height=50, width=100,
                                           corner_radius=3, font=("Arial Bold", 12))
            self.icon_label.grid(row=1, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

            self.temp_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color, fg_color=self.bg_color,
                                           height=50, width=100,
                                           corner_radius=3, font=("Arial Bold", 12))
            self.temp_label.grid(row=2, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

            self.wind_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color, fg_color=self.bg_color,
                                           height=50, width=100,
                                           corner_radius=3, font=("Arial Bold", 12))
            self.wind_label.grid(row=3, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

            self.precip_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color, fg_color=self.bg_color,
                                             height=50, width=100,
                                             corner_radius=3, font=("Arial Bold", 12))
            self.precip_label.grid(row=4, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

            self.cloud_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color, fg_color=self.bg_color,
                                            height=50, width=100,
                                            corner_radius=3, font=("Arial Bold", 12))
            self.cloud_label.grid(row=5, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

            self.humidity_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                               fg_color=self.bg_color,
                                               height=50, width=100,
                                               corner_radius=3, font=("Arial Bold", 12))
            self.humidity_label.grid(row=6, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

            self.pressure_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                               fg_color=self.bg_color,
                                               height=50, width=100,
                                               corner_radius=3, font=("Arial Bold", 12))
            self.pressure_label.grid(row=7, column=i, padx=[2, 2], pady=[2, 2], sticky="nsew")

    def content(self, data, count=0): # It takes data to be displayed, can be called to refresh and display another set of data
        if data: # If there is data from the API display it
            forecast_day = data["forecast"]["forecastday"][count]

            date = forecast_day["date"]
            hours = forecast_day["hour"]

            column = 1
            self.count = count

            for index, hour in enumerate(hours):
                if index % 3 == 0:
                    time = hour["time"].split(" ")[1]

                    temperature = hour["temp_c"]
                    is_day = "day" if int(time.split(":")[0]) <= 12 else "night"

                    condition = hour["condition"]
                    condition_text = condition["text"]
                    condition_code = condition["code"]

                    wind_kph = hour["wind_kph"]
                    precip_mm = hour["precip_mm"]
                    cloud = hour["cloud"]
                    humidity = hour["humidity"]
                    pressure_in = hour["pressure_in"]

                    self.date_label = ctk.CTkLabel(master=self, text="N/a", fg_color="gray", height=50, width=100,
                                                   corner_radius=3, font=("Arial Bold", 12))
                    self.date_label.grid(row=0, column=column, padx=[2, 2], pady=[9, 2], sticky="nsew")

                    self.icon_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                   fg_color=self.bg_color,
                                                   height=50, width=100,
                                                   corner_radius=3, font=("Arial Bold", 12))
                    self.icon_label.grid(row=1, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.temp_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                   fg_color=self.bg_color,
                                                   height=50, width=100,
                                                   corner_radius=3, font=("Arial Bold", 12))
                    self.temp_label.grid(row=2, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.wind_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                   fg_color=self.bg_color,
                                                   height=50, width=100,
                                                   corner_radius=3, font=("Arial Bold", 12))
                    self.wind_label.grid(row=3, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.precip_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                     fg_color=self.bg_color,
                                                     height=50, width=100,
                                                     corner_radius=3, font=("Arial Bold", 12))
                    self.precip_label.grid(row=4, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.cloud_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                    fg_color=self.bg_color,
                                                    height=50, width=100,
                                                    corner_radius=3, font=("Arial Bold", 12))
                    self.cloud_label.grid(row=5, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.humidity_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                       fg_color=self.bg_color,
                                                       height=50, width=100,
                                                       corner_radius=3, font=("Arial Bold", 12))
                    self.humidity_label.grid(row=6, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.pressure_label = ctk.CTkLabel(master=self, text="-", text_color=self.text_color,
                                                       fg_color=self.bg_color,
                                                       height=50, width=100,
                                                       corner_radius=3, font=("Arial Bold", 12))
                    self.pressure_label.grid(row=7, column=column, padx=[2, 2], pady=[2, 2], sticky="nsew")

                    self.date_label.configure(text=f"{self.get_date_name(date)}\n{time}")
                    self.icon_image = ctk.CTkImage(
                        Image.open(f"weather_image/{is_day}/{condition['icon'].split('/')[6]}"), size=(36, 36))
                    self.icon_label.configure(image=self.icon_image)
                    self.temp_label.configure(text=f"{temperature} °C")
                    self.wind_label.configure(text=f"{wind_kph}kph")
                    self.precip_label.configure(text=f"{precip_mm} mm")
                    self.cloud_label.configure(text=f"{cloud} %")
                    self.humidity_label.configure(text=f"{humidity} %")
                    self.pressure_label.configure(text=f"{pressure_in} in")

                    column += 1

    def get_date_name(self, date): # Set date and time format to be displayed formally
        formatted_date = datetime.strptime(date, "%Y-%m-%d").date()
        date_name = formatted_date.strftime("%A")

        return f"{date_name} {str(formatted_date).split('-')[2]}"

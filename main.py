import customtkinter as ctk
from main_frame import MainFrame
from second_frame import SecondFrame
from PIL import Image
from threading import Thread
from time import sleep

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

system_title = "MetraWeather"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(system_title)

        width = 1250
        height = 920
        self.geometry(f"{width}x{height}")

        self.logo_image = ctk.CTkImage(Image.open("logo.png"), size=(250, 250))
        self.logo_label = ctk.CTkLabel(master=self, text="", image=self.logo_image, anchor="center")
        self.logo_label.grid(row=0, column=0, padx=500, pady=[100, 0], sticky="nsew")

        self.app_label = ctk.CTkLabel(master=self, text=system_title, font=("Arial Bold", 36), anchor="center")
        self.app_label.grid(row=1, column=0, padx=500, sticky="nsew")

        Thread(target=self.show_frames).start()

        self.main_frame = MainFrame(master=self)
        self.second_frame = SecondFrame(master=self)
        self.side_frame = SideFrame(master=self)

    def show_frames(self):
        sleep(5)

        self.logo_label.grid_remove()
        self.app_label.grid_remove()

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.second_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.side_frame.grid(row=0, column=0, padx=[20, 0], pady=20, sticky="nsew")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # self.main_frame.grid_remove()
        self.second_frame.grid_remove()


class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        self.logo_image = ctk.CTkImage(Image.open("logo.png"), size=(175, 175))
        self.logo_label = ctk.CTkLabel(master=self, text="", image=self.logo_image, anchor="center")
        self.logo_label.grid(row=0, column=0, padx=10, pady=10)

        self.forecast_btn = ctk.CTkButton(master=self, width=170, height=45, border_width=0, corner_radius=8,
                                          text="Weather\nForecast", font=("Arial Bold", 18), command=self.show_forecast)
        self.forecast_btn.grid(row=1, column=0, padx=10, pady=5)

        self.time_btn = ctk.CTkButton(master=self, width=170, height=45, border_width=0, corner_radius=8,
                                      text="Previous\nWeather", font=("Arial Bold", 18), command=self.show_time)
        self.time_btn.grid(row=2, column=0, padx=10, pady=5)

        self.exit_btn = ctk.CTkButton(master=self, width=170, height=45, border_width=0, corner_radius=8,
                                      text="Exit", font=("Arial Bold", 18), command=self.exit)
        self.exit_btn.grid(row=3, column=0, padx=10, pady=5)

    @staticmethod
    def show_forecast():
        app.main_frame.grid()
        app.second_frame.grid_remove()

    @staticmethod
    def show_time():
        app.second_frame.grid()
        app.main_frame.grid_remove()

    @staticmethod
    def exit():
        app.destroy()

 
if __name__ == '__main__':
    app = App()
    app.resizable(False, True)
    app.mainloop()

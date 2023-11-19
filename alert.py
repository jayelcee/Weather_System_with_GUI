import customtkinter as ctk


class Alert(ctk.CTkToplevel):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)

        self.data = data
        self.title("Alerts")
        self.attributes('-topmost', 'true')

        if self.data:
            alerts = self.data["alerts"]["alert"]

            if len(alerts) > 0:
                for index, alert in enumerate(alerts):
                    headline = alert["headline"]
                    severity = alert["severity"]
                    urgency = alert["urgency"]
                    areas = alert["areas"]
                    event = alert["event"]
                    desc = alert["desc"]
                    instruction = alert["instruction"]

                    self.alert_label = ctk.CTkLabel(self,
                                                    text=f"Headline: {headline}\nSeverity: {severity}\n"
                                                         f"Urgency: {urgency}\nAreas: {areas}\nEvent: {event}\n"
                                                         f"Description: {desc}\nInstruction: {instruction}",
                                                    font=("Arial Bold", 12))
                    self.alert_label.grid(row=index, column=0, padx=20, pady=[20, 10])
            else:
                self.alert_label = ctk.CTkLabel(self, text="No Alerts Available Yet", font=("Arial Bold", 12))
                self.alert_label.grid(row=0, column=0, padx=20, pady=[20, 10])

        else:
            self.alert_label = ctk.CTkLabel(self, text="No Alerts Available Yet.",
                                            font=("Arial Bold", 16), wraplength=800)
            self.alert_label.grid(row=0, column=0, padx=20, pady=[20, 10])

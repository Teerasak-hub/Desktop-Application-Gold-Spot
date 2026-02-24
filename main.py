import customtkinter as ctk
from scraper import get_realtime_data

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GoldApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gold Tracker")
        self.geometry("400x380")

        # Header
        self.label = ctk.CTkLabel(self, text="Thai Gold Market", font=("Kanit", 22, "bold"))
        self.label.pack(pady=(25, 10))

        # Main Price Card
        self.thai_card = ctk.CTkFrame(self, fg_color="#2B2B2B", corner_radius=15)
        self.thai_card.pack(pady=10, padx=35, fill="x")

        self.thai_label = ctk.CTkLabel(self.thai_card, text="Current gold bar price", font=("Kanit", 12, "bold"),text_color="gray")
        self.thai_label.pack(pady=(10, 0))

        self.thai_label = ctk.CTkLabel(self.thai_card, text="--- ฿", font=("Kanit", 32, "bold"), text_color="#FFD700")
        self.thai_label.pack(pady=(5, 15))

        # Stats Row
        self.info_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.info_frame.pack(pady=10, padx=40, fill="x")

        self.world_label = ctk.CTkLabel(self.info_frame, text="Spot: -- USD", font=("Kanit", 14))
        self.world_label.pack(side="left")

        self.rate_label = ctk.CTkLabel(self.info_frame, text="Rate: -- THB", font=("Kanit", 14))
        self.rate_label.pack(side="right")

        # Button
        self.btn = ctk.CTkButton(self, text="Update_Data",
                                 command=self.refresh_data,
                                 height=40,
                                 corner_radius=10,
                                 font=("Kanit", 14))
        self.btn.pack(pady=(25, 20))

    def refresh_data(self):
        self.btn.configure(state="disabled", text="Fetching data...")
        self.update()

        data = get_realtime_data()
        if "error" not in data:
            self.thai_label.configure(text=f"{data['thai']} ฿")
            self.world_label.configure(text=f"Spot: {data['world']} USD")
            self.rate_label.configure(text=f"Rate: {data['rate']} THB")
        else:
            self.thai_label.configure(text="Error")

        self.btn.configure(state="normal", text="Update_Data")
if __name__ == "__main__":
    app = GoldApp()
    app.mainloop()


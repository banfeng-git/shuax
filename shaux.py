import tkinter as tk
import time

class FocusClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Focus Clock")
        self.geometry("200x100")
        self.label = tk.Label(self, text="", font=("Arial", 48))
        self.label.pack(pady=30)
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    app = FocusClock()
    app.mainloop()

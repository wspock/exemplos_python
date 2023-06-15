import tkinter as tk
import time
import math

class AnalogClock(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=200, height=200, bg="black")
        self.canvas.pack()

        self.hour_hand = self.canvas.create_line(100, 100, 100, 60, width=3, fill="#FFFF00")
        self.minute_hand = self.canvas.create_line(100, 100, 100, 40, width=2, fill="#FFFF00")
        self.second_hand = self.canvas.create_line(100, 100, 100, 30, width=1, fill="#FFFF00")

        self.create_arabic_numbers()

        self.update_clock()

    def create_arabic_numbers(self):
        arabic_numbers = [
            {'number': '١', 'angle': 30},
            {'number': '٢', 'angle': 60},
            {'number': '٣', 'angle': 90},
            {'number': '٤', 'angle': 120},
            {'number': '٥', 'angle': 150},
            {'number': '٦', 'angle': 180},
            {'number': '٧', 'angle': 210},
            {'number': '٨', 'angle': 240},
            {'number': '٩', 'angle': 270},
            {'number': '١٠', 'angle': 300},
            {'number': '١١', 'angle': 330},
            {'number': '١٢', 'angle': 0},
        ]

        for num in arabic_numbers:
            angle = math.radians(num['angle'])
            x = 100 + 80 * math.sin(angle)
            y = 100 - 80 * math.cos(angle)
            self.canvas.create_text(x, y, text=num['number'], font=('Arial', 16), fill='#FFFF00')

    def update_clock(self):
        now = time.localtime()
        hour_angle = (now.tm_hour % 12) * 30 + now.tm_min / 2
        minute_angle = now.tm_min * 6
        second_angle = now.tm_sec * 6

        self.canvas.coords(self.hour_hand, 100, 100, 100 + 40 * math.sin(math.radians(hour_angle)), 100 - 40 * math.cos(math.radians(hour_angle)))
        self.canvas.coords(self.minute_hand, 100, 100, 100 + 60 * math.sin(math.radians(minute_angle)), 100 - 60 * math.cos(math.radians(minute_angle)))
        self.canvas.coords(self.second_hand, 100, 100, 100 + 70 * math.sin(math.radians(second_angle)), 100 - 70 * math.cos(math.radians(second_angle)))

        self.after(1000, self.update_clock)

root = tk.Tk()
root.title("الساعة")
root.resizable(False, False)
clock = AnalogClock(root)
clock.pack()
root.mainloop()

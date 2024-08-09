
import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        # Configure grid layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        
        # Time Entry
        self.label = tk.Label(root, text="Enter time in seconds:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Timer Display
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.remaining_time = 0
        self.running = False
        self.timer_id = None

    def start_timer(self):
        if not self.running:
            try:
                self.remaining_time = int(self.entry.get())
                if self.remaining_time <= 0:
                    raise ValueError("Time must be positive")
                self.running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid positive integer.")
                self.running = False

    def update_timer(self):
        if self.running:
            if self.remaining_time > 0:
                mins, secs = divmod(self.remaining_time, 60)
                hours, mins = divmod(mins, 60)
                time_formatted = f"{hours:02}:{mins:02}:{secs:02}"
                self.time_label.config(text=time_formatted)
                self.remaining_time -= 1
                self.timer_id = self.root.after(1000, self.update_timer)
            else:
                self.time_label.config(text="Time's up!")
                self.running = False

    def stop_timer(self):
        if self.running:
            self.root.after_cancel(self.timer_id)
            self.running = False
            self.time_label.config(text="00:00:00")

# Create the main window and run the application
root = tk.Tk()
app = CountdownTimerApp(root)
root.mainloop()

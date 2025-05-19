import tkinter as tk
import psutil  # Used to get the cpu ram and disk info from the machine
import time
from tkinter import messagebox
import socket  # used to get the histname and ip address systeminfo


# Create the main window
window = tk.Tk()
window.geometry("450x150")
window.resizable(False, False)
window.configure(bg="black")
window.overrideredirect(True)

# Set window size
win_width = 250
win_height = 180

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate x and y to place window at top-right
x = screen_width - win_width - 10  # 10px padding from right edge
y = 10  # 10px from the top

# Position the window
window.geometry(f"{win_width}x{win_height}+{x}+{y}")

# Create labels for CPU, RAM, and Disk

hostname_label = tk.Label(window, text="", font=(
    "Arial", 12), fg="white", bg="black", anchor="w", justify="left")
hostname_label.pack(pady=5)

ipaddress_label = tk.Label(window, text="", font=(
    "Arial", 12), fg="white", bg="black", anchor="w", justify="left")
ipaddress_label.pack(pady=5)


# Create labels for CPU, RAM, and Disk
cpu_label = tk.Label(window, text="", font=(
    "Arial", 12), fg="white", bg="black", anchor="w", justify="left")
cpu_label.pack(pady=5)

ram_label = tk.Label(window, text="", font=(
    "Arial", 12), fg="white", bg="black", anchor="w", justify="left")
ram_label.pack(pady=5)

disk_label = tk.Label(window, text="", font=(
    "Arial", 12), fg="white", bg="black", anchor="w", justify="left")
disk_label.pack(pady=5)

# Function to update the info every second


def update_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    cpu_label.config(text=f" CPU Usage: {cpu}%")
    ram_label.config(text=f" RAM Usage: {ram}%")
    disk_label.config(text=f" DISK Usage: {disk}%")
    hostname_label.config(text=f" Host Name: {hostname}")
    ipaddress_label.config(text=f" IP Address: {ipaddress}")
    window.after(10000, update_stats)  # Schedule to run again in 1 second
    cpu_label.pack(anchor="w", padx=10, pady=5)
    ram_label.pack(anchor="w", padx=10, pady=5)
    disk_label.pack(anchor="w", padx=10, pady=5)
    hostname_label.pack(anchor="w", padx=10, pady=5)
    ipaddress_label.pack(anchor="w", padx=10, pady=5)


# Start updating
update_stats()

# Run the app

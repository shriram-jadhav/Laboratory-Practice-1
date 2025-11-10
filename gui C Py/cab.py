import tkinter as tk
from tkinter import messagebox
import random

def book_ride():
    pickup = pickup_entry.get()
    drop = drop_entry.get()
    vehicle = vehicle_var.get()

    if not pickup or not drop:
        messagebox.showwarning("Missing Info", "Please enter both pickup and drop locations!")
        return

    # Random fare & driver
    fare = random.randint(100, 500)
    driver = random.choice(["Ramesh", "Suresh", "Anil", "Vikram"])
    eta = random.randint(5, 15)

    result = f"🚖 Booking Confirmed!\n\nDriver: {driver}\nVehicle: {vehicle}\nFare: ₹{fare}\nETA: {eta} mins"
    result_label.config(text=result)

# GUI Window
root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("350x350")

tk.Label(root, text="🚕 Cab/Auto Booking App", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Pickup Location:").pack()
pickup_entry = tk.Entry(root, width=30)
pickup_entry.pack()

tk.Label(root, text="Drop Location:").pack()
drop_entry = tk.Entry(root, width=30)
drop_entry.pack()

tk.Label(root, text="Select Vehicle:").pack(pady=5)
vehicle_var = tk.StringVar(value="Auto")
tk.Radiobutton(root, text="Auto", variable=vehicle_var, value="Auto").pack()
tk.Radiobutton(root, text="Cab", variable=vehicle_var, value="Cab").pack()

tk.Button(root, text="Book Ride", bg="green", fg="white", command=book_ride).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue", justify="left")
result_label.pack(pady=10)

root.mainloop()

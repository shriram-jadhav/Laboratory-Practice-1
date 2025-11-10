import tkinter as tk
from datetime import datetime

def start_app():
    message_label.config(text="🎯 Welcome aboard! Let's begin your journey.", fg="green")

def update_time():
    current_time = datetime.now().strftime("%A, %d %B %Y | %I:%M %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # updates time every second

# Main window
root = tk.Tk()
root.title("Welcome Screen")
root.geometry("450x300")
root.configure(bg="#E8F0FE")

# Heading
tk.Label(root, text="✨ Welcome to Smart App ✨", 
         font=("Arial", 18, "bold"), bg="#E8F0FE", fg="#0B5394").pack(pady=15)

# Tagline
tk.Label(root, text="Making life easier, one click at a time!", 
         font=("Arial", 11, "italic"), bg="#E8F0FE", fg="gray").pack()

# Dynamic Time & Date
time_label = tk.Label(root, font=("Arial", 10), bg="#E8F0FE", fg="#333")
time_label.pack(pady=10)
update_time()

# Welcome Message
message_label = tk.Label(root, text="We’re glad to have you here!", 
                         font=("Arial", 12), bg="#E8F0FE", fg="black")
message_label.pack(pady=20)

# Buttons
btn_frame = tk.Frame(root, bg="#E8F0FE")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start", bg="#4CAF50", fg="white", width=10, 
          font=("Arial", 11, "bold"), command=start_app).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Exit", bg="#D32F2F", fg="white", width=10, 
          font=("Arial", 11, "bold"), command=root.destroy).grid(row=0, column=1, padx=10)

# Footer
tk.Label(root, text="© 2025 SmartApp Technologies", font=("Arial", 9), 
         bg="#E8F0FE", fg="gray").pack(side="bottom", pady=8)

root.mainloop()

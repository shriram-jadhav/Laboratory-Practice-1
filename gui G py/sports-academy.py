import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    sport = sport_var.get()

    if not name or not age or not sport:
        messagebox.showwarning("Missing Info", "Please fill all required fields!")
        return

    result = f"✅ Registration Successful!\n\nName: {name}\nAge: {age}\nGender: {gender}\nSport: {sport}"
    messagebox.showinfo("Registration Complete", result)

# Main window
root = tk.Tk()
root.title("Sports Academy Registration Form")
root.geometry("350x400")

tk.Label(root, text="🏅 Sports Academy Registration", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Full Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Select Sport:").pack(pady=5)
sport_var = tk.StringVar(value="Cricket")
sports = ["Cricket", "Football", "Badminton", "Swimming", "Tennis"]
for s in sports:
    tk.Radiobutton(root, text=s, variable=sport_var, value=s).pack(anchor="w", padx=80)

tk.Button(root, text="Register", bg="blue", fg="white", command=register).pack(pady=15)

root.mainloop()

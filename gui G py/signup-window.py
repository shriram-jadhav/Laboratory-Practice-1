import tkinter as tk
from tkinter import messagebox

def signup():
    name = name_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    confirm = confirm_entry.get()

    if not name or not email or not password or not confirm:
        messagebox.showwarning("Missing Info", "Please fill all fields!")
        return
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    messagebox.showinfo("Success", f"✅ Account Created Successfully!\nWelcome, {name}!")

    clear_form()

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("🧾 Sign-Up Window")
root.geometry("400x400")
root.config(bg="#E3F2FD")

tk.Label(root, text="Create Your Account", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#0D47A1").pack(pady=15)

frame = tk.Frame(root, bg="#E3F2FD")
frame.pack(pady=10)

# Full Name
tk.Label(frame, text="Full Name:", font=("Arial", 11), bg="#E3F2FD").grid(row=0, column=0, sticky="e", pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Email
tk.Label(frame, text="Email:", font=("Arial", 11), bg="#E3F2FD").grid(row=1, column=0, sticky="e", pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

# Password
tk.Label(frame, text="Password:", font=("Arial", 11), bg="#E3F2FD").grid(row=2, column=0, sticky="e", pady=5)
pass_entry = tk.Entry(frame, width=30, show="*")
pass_entry.grid(row=2, column=1, pady=5)

# Confirm Password
tk.Label(frame, text="Confirm Password:", font=("Arial", 11), bg="#E3F2FD").grid(row=3, column=0, sticky="e", pady=5)
confirm_entry = tk.Entry(frame, width=30, show="*")
confirm_entry.grid(row=3, column=1, pady=5)

# Buttons
tk.Button(root, text="Sign Up", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
          width=12, command=signup).pack(pady=10)
tk.Button(root, text="Clear", bg="#D32F2F", fg="white", font=("Arial", 11, "bold"),
          width=12, command=clear_form).pack()

tk.Label(root, text="Already have an account? Login here.", font=("Arial", 9),
         bg="#E3F2FD", fg="gray").pack(pady=15)

root.mainloop()

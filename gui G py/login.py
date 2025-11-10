import tkinter as tk
from tkinter import messagebox

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Login Successful", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Login Window")
root.geometry("350x250")
root.config(bg="#E3F2FD")

# Title label
tk.Label(root, text="🔐 User Login", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#0D47A1").pack(pady=15)

# Username
tk.Label(root, text="Username:", font=("Arial", 11), bg="#E3F2FD").pack()
username_entry = tk.Entry(root, width=25)
username_entry.pack(pady=5)

# Password
tk.Label(root, text="Password:", font=("Arial", 11), bg="#E3F2FD").pack()
password_entry = tk.Entry(root, show="*", width=25)
password_entry.pack(pady=5)

# Remember Me
remember_var = tk.IntVar()
tk.Checkbutton(root, text="Remember Me", variable=remember_var, bg="#E3F2FD").pack(pady=5)

# Buttons
tk.Button(root, text="Login", width=10, bg="#1E88E5", fg="white", font=("Arial", 10, "bold"),
          command=login).pack(pady=5)
tk.Button(root, text="Clear", width=10, bg="#D32F2F", fg="white", font=("Arial", 10, "bold"),
          command=clear_fields).pack()

# Footer
tk.Label(root, text="© 2025 Secure Login System", font=("Arial", 9), bg="#E3F2FD", fg="gray").pack(side="bottom", pady=10)

root.mainloop()

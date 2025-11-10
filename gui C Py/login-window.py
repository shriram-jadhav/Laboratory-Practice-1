import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    user_type = user_type_var.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields!")
        return
    
    # Check credentials (sample)
    if username == "admin" and password == "admin123":
        remember = "Yes" if remember_var.get() else "No"
        messagebox.showinfo("Success", f"Welcome {username}!\nUser Type: {user_type}\nRemember Me: {remember}")
        clear_fields()
    else:
        messagebox.showerror("Error", "Invalid credentials!")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    remember_var.set(False)

# Main window
root = tk.Tk()
root.title("Login")
root.geometry("350x400")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="LOGIN", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

# User Type (Radio Buttons)
tk.Label(root, text="Login As:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor=tk.W, padx=40)
user_type_var = tk.StringVar(value="Student")
user_frame = tk.Frame(root, bg="#f0f0f0")
user_frame.pack(anchor=tk.W, padx=40, pady=5)
tk.Radiobutton(user_frame, text="Student", variable=user_type_var, value="Student", bg="#f0f0f0").pack(side=tk.LEFT)
tk.Radiobutton(user_frame, text="Teacher", variable=user_type_var, value="Teacher", bg="#f0f0f0").pack(side=tk.LEFT)
tk.Radiobutton(user_frame, text="Admin", variable=user_type_var, value="Admin", bg="#f0f0f0").pack(side=tk.LEFT)

# Username
tk.Label(root, text="Username:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor=tk.W, padx=40, pady=(15, 5))
username_entry = tk.Entry(root, font=("Arial", 11), width=30)
username_entry.pack(padx=40)

# Password
tk.Label(root, text="Password:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor=tk.W, padx=40, pady=(15, 5))
password_entry = tk.Entry(root, font=("Arial", 11), width=30, show="*")
password_entry.pack(padx=40)

# Remember Me (Checkbox)
remember_var = tk.BooleanVar()
tk.Checkbutton(root, text="Remember Me", variable=remember_var, font=("Arial", 9), bg="#f0f0f0").pack(anchor=tk.W, padx=40, pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)
tk.Button(button_frame, text="Login", command=login, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields, bg="#f44336", fg="white", font=("Arial", 11, "bold"), width=10).pack(side=tk.LEFT, padx=5)

# Demo credentials label
tk.Label(root, text="Demo: admin / admin123", font=("Arial", 8), fg="gray", bg="#f0f0f0").pack(pady=10)

root.mainloop()
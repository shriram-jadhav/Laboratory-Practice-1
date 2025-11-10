import tkinter as tk
from tkinter import ttk, messagebox

def signup():
    name = name_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm = confirm_entry.get()
    gender = gender_var.get()
    country = country_var.get()
    
    # Validation
    if not name or not email or not username or not password:
        messagebox.showerror("Error", "Please fill all required fields!")
        return
    
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    
    if not gender:
        messagebox.showerror("Error", "Please select gender!")
        return
    
    if country == "Select Country":
        messagebox.showerror("Error", "Please select country!")
        return
    
    if not terms_var.get():
        messagebox.showerror("Error", "Please accept Terms and Conditions!")
        return
    
    # Success
    newsletter = "Yes" if newsletter_var.get() else "No"
    messagebox.showinfo("Success", f"Account Created!\n\nName: {name}\nEmail: {email}\nUsername: {username}\nNewsletter: {newsletter}")
    clear_form()

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)
    gender_var.set("")
    country_var.set("Select Country")
    terms_var.set(False)
    newsletter_var.set(False)

# Main window
root = tk.Tk()
root.title("Sign Up")
root.geometry("450x650")
root.config(bg="#f0f0f0")

# Header
tk.Label(root, text="CREATE ACCOUNT", font=("Arial", 18, "bold"), bg="#673AB7", fg="white", pady=15).pack(fill=tk.X)

# Form Frame
form_frame = tk.Frame(root, bg="white", padx=30, pady=20)
form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Name
tk.Label(form_frame, text="Full Name: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=(10, 5))
name_entry = tk.Entry(form_frame, font=("Arial", 10), width=35)
name_entry.pack(pady=(0, 10))

# Email
tk.Label(form_frame, text="Email: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=5)
email_entry = tk.Entry(form_frame, font=("Arial", 10), width=35)
email_entry.pack(pady=(0, 10))

# Username
tk.Label(form_frame, text="Username: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=5)
username_entry = tk.Entry(form_frame, font=("Arial", 10), width=35)
username_entry.pack(pady=(0, 10))

# Password
tk.Label(form_frame, text="Password: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=5)
password_entry = tk.Entry(form_frame, font=("Arial", 10), width=35, show="*")
password_entry.pack(pady=(0, 10))

# Confirm Password
tk.Label(form_frame, text="Confirm Password: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=5)
confirm_entry = tk.Entry(form_frame, font=("Arial", 10), width=35, show="*")
confirm_entry.pack(pady=(0, 10))

# Gender (Radio Buttons)
tk.Label(form_frame, text="Gender: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=5)
gender_var = tk.StringVar()
gender_frame = tk.Frame(form_frame, bg="white")
gender_frame.pack(anchor=tk.W, pady=(0, 10))
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="white").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="white").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", bg="white").pack(side=tk.LEFT, padx=5)

# Country (Combobox)
tk.Label(form_frame, text="Country: *", font=("Arial", 10, "bold"), bg="white").pack(anchor=tk.W, pady=5)
country_var = tk.StringVar()
country_combo = ttk.Combobox(form_frame, textvariable=country_var, 
                            values=["India", "USA", "UK", "Canada", "Australia", "Other"],
                            font=("Arial", 10), width=33, state="readonly")
country_combo.pack(pady=(0, 10))
country_combo.set("Select Country")

# Newsletter (Checkbox)
newsletter_var = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Subscribe to newsletter", variable=newsletter_var, 
              font=("Arial", 9), bg="white").pack(anchor=tk.W, pady=5)

# Terms and Conditions (Checkbox)
terms_var = tk.BooleanVar()
tk.Checkbutton(form_frame, text="I agree to Terms and Conditions *", variable=terms_var,
              font=("Arial", 9, "bold"), bg="white", fg="#673AB7").pack(anchor=tk.W, pady=5)

# Required fields note
tk.Label(form_frame, text="* Required fields", font=("Arial", 8), fg="gray", bg="white").pack(anchor=tk.W, pady=(10, 0))

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Sign Up", command=signup, bg="#673AB7", fg="white", 
         font=("Arial", 11, "bold"), width=12, cursor="hand2").pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Clear", command=clear_form, bg="#9E9E9E", fg="white",
         font=("Arial", 11, "bold"), width=12, cursor="hand2").pack(side=tk.LEFT, padx=10)

# Login link
tk.Label(root, text="Already have an account? Login here", font=("Arial", 9, "underline"),
        fg="#673AB7", bg="#f0f0f0", cursor="hand2").pack(pady=10)

root.mainloop()
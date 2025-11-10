import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    course = course_listbox.get(tk.ACTIVE)
    hosteller = "Yes" if hostel_var.get() else "No"

    if name == "" or age == "":
        messagebox.showwarning("Input Error", "Please fill all fields!")
    else:
        messagebox.showinfo("Registration Successful",
                            f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}\nHosteller: {hosteller}")

def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Male")
    hostel_var.set(0)
    course_listbox.selection_clear(0, tk.END)

# Main Window
root = tk.Tk()
root.title("🎓 Student Registration Form")
root.geometry("400x500")
root.config(bg="#E8F5E9")

# Title
tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold"),
         bg="#E8F5E9", fg="#1B5E20").pack(pady=15)

# Name
tk.Label(root, text="Full Name:", font=("Arial", 11), bg="#E8F5E9").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Age
tk.Label(root, text="Age:", font=("Arial", 11), bg="#E8F5E9").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

# Gender
tk.Label(root, text="Gender:", font=("Arial", 11), bg="#E8F5E9").pack()
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#E8F5E9").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#E8F5E9").pack()

# Course Selection (Listbox)
tk.Label(root, text="Select Course:", font=("Arial", 11), bg="#E8F5E9").pack(pady=(10, 0))
course_listbox = tk.Listbox(root, height=4)
courses = ["Computer Engineering", "IT", "ENTC", "Mechanical", "Civil"]
for c in courses:
    course_listbox.insert(tk.END, c)
course_listbox.pack(pady=5)

# Hostel Checkbox
hostel_var = tk.IntVar()
tk.Checkbutton(root, text="Hosteller", variable=hostel_var, bg="#E8F5E9").pack(pady=5)

# Buttons
tk.Button(root, text="Submit", bg="#43A047", fg="white", font=("Arial", 10, "bold"),
          width=12, command=submit_form).pack(pady=10)
tk.Button(root, text="Clear", bg="#E53935", fg="white", font=("Arial", 10, "bold"),
          width=12, command=clear_form).pack()

# Footer
tk.Label(root, text="© 2025 Student Registration System", font=("Arial", 9),
         bg="#E8F5E9", fg="gray").pack(side="bottom", pady=10)

root.mainloop()

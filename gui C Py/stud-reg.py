import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    
    if not name or not email or not gender:
        messagebox.showerror("Error", "Please fill all required fields!")
        return
    
    # Get selected course
    try:
        course = course_listbox.get(course_listbox.curselection())
    except:
        messagebox.showerror("Error", "Please select a course!")
        return
    
    # Get hobbies
    hobbies = []
    if sports_var.get():
        hobbies.append("Sports")
    if music_var.get():
        hobbies.append("Music")
    
    details = f"Name: {name}\nEmail: {email}\nGender: {gender}\nCourse: {course}\nHobbies: {', '.join(hobbies)}"
    messagebox.showinfo("Registration Success", details)

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender_var.set("")
    sports_var.set(False)
    music_var.set(False)
    course_listbox.selection_clear(0, tk.END)

# Main window
root = tk.Tk()
root.title("Student Registration")
root.geometry("400x450")

# Title
tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold"), bg="lightblue").pack(fill=tk.X, pady=10)

# Name
tk.Label(root, text="Name:", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=20)

# Email
tk.Label(root, text="Email:", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=20)

# Gender (Radio buttons)
tk.Label(root, text="Gender:", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=5)
gender_var = tk.StringVar()
gender_frame = tk.Frame(root)
gender_frame.pack(anchor=tk.W, padx=20)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side=tk.LEFT)

# Course (Listbox)
tk.Label(root, text="Select Course:", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=5)
course_listbox = tk.Listbox(root, height=4, width=40)
for course in ["Computer Science", "Engineering", "Business", "Arts"]:
    course_listbox.insert(tk.END, course)
course_listbox.pack(padx=20)

# Hobbies (Checkbuttons)
tk.Label(root, text="Hobbies:", font=("Arial", 10)).pack(anchor=tk.W, padx=20, pady=5)
hobbies_frame = tk.Frame(root)
hobbies_frame.pack(anchor=tk.W, padx=20)
sports_var = tk.BooleanVar()
music_var = tk.BooleanVar()
tk.Checkbutton(hobbies_frame, text="Sports", variable=sports_var).pack(side=tk.LEFT)
tk.Checkbutton(hobbies_frame, text="Music", variable=music_var).pack(side=tk.LEFT)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
tk.Button(button_frame, text="Submit", command=submit_form, bg="green", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", command=clear_form, bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_text.get("1.0", "end-1c")
    disease = disease_listbox.get(tk.ACTIVE)
    symptoms = []
    if chk_fever.get():
        symptoms.append("Fever")
    if chk_cough.get():
        symptoms.append("Cough")
    if chk_pain.get():
        symptoms.append("Body Pain")

    if not name or not age or not address:
        messagebox.showwarning("Missing Info", "Please fill all required fields!")
        return

    info = f"""✅ Registration Successful!

Name: {name}
Age: {age}
Gender: {gender}
Address: {address}
Disease Selected: {disease}
Symptoms: {', '.join(symptoms) if symptoms else 'None'}
"""
    messagebox.showinfo("Patient Registered", info)

def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    chk_fever.set(0)
    chk_cough.set(0)
    chk_pain.set(0)
    disease_listbox.selection_clear(0, tk.END)

# Main window
root = tk.Tk()
root.title("🏥 Hospital Patient Registration Form")
root.geometry("550x600")
root.configure(bg="#F0F8FF")

tk.Label(root, text="Patient Registration Form", font=("Arial", 18, "bold"), 
         fg="#0B5394", bg="#F0F8FF").pack(pady=15)

# Frame for form
frame = tk.Frame(root, bg="#F0F8FF")
frame.pack(pady=10)

# Name
tk.Label(frame, text="Full Name:", font=("Arial", 11), bg="#F0F8FF").grid(row=0, column=0, sticky="e", pady=5)
name_entry = tk.Entry(frame, width=35)
name_entry.grid(row=0, column=1, pady=5)

# Age
tk.Label(frame, text="Age:", font=("Arial", 11), bg="#F0F8FF").grid(row=1, column=0, sticky="e", pady=5)
age_entry = tk.Entry(frame, width=10)
age_entry.grid(row=1, column=1, sticky="w", pady=5)

# Gender
tk.Label(frame, text="Gender:", font=("Arial", 11), bg="#F0F8FF").grid(row=2, column=0, sticky="e", pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#F0F8FF").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#F0F8FF").grid(row=2, column=1, sticky="e")

# Address (Text box)
tk.Label(frame, text="Address:", font=("Arial", 11), bg="#F0F8FF").grid(row=3, column=0, sticky="ne", pady=5)
address_text = tk.Text(frame, width=30, height=4)
address_text.grid(row=3, column=1, pady=5)

# Disease (Listbox)
tk.Label(frame, text="Select Disease:", font=("Arial", 11), bg="#F0F8FF").grid(row=4, column=0, sticky="ne", pady=5)
disease_listbox = tk.Listbox(frame, height=5, selectmode=tk.SINGLE, width=28)
diseases = ["Fever", "Cold", "Cough", "Diabetes", "Injury", "Other"]
for d in diseases:
    disease_listbox.insert(tk.END, d)
disease_listbox.grid(row=4, column=1, pady=5)

# Symptoms (Checkbuttons)
tk.Label(frame, text="Symptoms:", font=("Arial", 11), bg="#F0F8FF").grid(row=5, column=0, sticky="ne", pady=5)
chk_fever = tk.IntVar()
chk_cough = tk.IntVar()
chk_pain = tk.IntVar()
symptom_frame = tk.Frame(frame, bg="#F0F8FF")
symptom_frame.grid(row=5, column=1, sticky="w")
tk.Checkbutton(symptom_frame, text="Fever", variable=chk_fever, bg="#F0F8FF").pack(anchor="w")
tk.Checkbutton(symptom_frame, text="Cough", variable=chk_cough, bg="#F0F8FF").pack(anchor="w")
tk.Checkbutton(symptom_frame, text="Body Pain", variable=chk_pain, bg="#F0F8FF").pack(anchor="w")

# Buttons
btn_frame = tk.Frame(root, bg="#F0F8FF")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Submit", bg="#4CAF50", fg="white", width=12, font=("Arial", 11, "bold"), command=submit_form).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", bg="#D32F2F", fg="white", width=12, font=("Arial", 11, "bold"), command=clear_form).grid(row=0, column=1, padx=10)

# Footer
tk.Label(root, text="© 2025 CityCare Hospital", font=("Arial", 9), bg="#F0F8FF", fg="gray").pack(side="bottom", pady=8)

root.mainloop()

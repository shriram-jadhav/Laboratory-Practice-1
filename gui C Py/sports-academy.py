import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class SportsAcademyForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Academy Registration")
        self.root.geometry("420x580")
        self.root.resizable(True, True)
        self.root.config(bg="#f0f4f8")
        
        # Variables
        self.reg_id = f"SA{datetime.now().strftime('%Y%m%d%H%M')}"
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Male")
        self.sport_var = tk.StringVar(value="Cricket")
        
        # Experience checkboxes
        self.beginner_var = tk.IntVar(value=1)
        self.intermediate_var = tk.IntVar()
        self.advanced_var = tk.IntVar()
        
        # Days checkboxes
        self.weekday_var = tk.IntVar()
        self.weekend_var = tk.IntVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#059669", height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="⚽ Sports Academy", font=("Arial", 16, "bold"),
                bg="#059669", fg="white").pack(pady=10)
        tk.Label(header, text="Registration Form", font=("Arial", 9),
                bg="#059669", fg="#d1fae5").pack()
        
        # Main Frame
        main = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=2)
        main.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        f = tk.Frame(main, bg="white", padx=15, pady=15)
        f.pack(fill=tk.BOTH, expand=True)
        
        # Registration ID
        tk.Label(f, text=f"Registration ID: {self.reg_id}", 
                font=("Arial", 8, "bold"), bg="white", 
                fg="#059669").grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Name
        tk.Label(f, text="Full Name *", font=("Arial", 9, "bold"),
                bg="white").grid(row=1, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.name_var, font=("Arial", 9),
                width=28).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        
        # Age & Gender
        tk.Label(f, text="Age *", font=("Arial", 9, "bold"),
                bg="white").grid(row=3, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.age_var, font=("Arial", 9),
                width=8).grid(row=4, column=0, sticky="w", pady=(0, 8))
        
        tk.Label(f, text="Gender *", font=("Arial", 9, "bold"),
                bg="white").grid(row=3, column=1, sticky="w", pady=(0, 3), padx=(10, 0))
        
        gender_f = tk.Frame(f, bg="white")
        gender_f.grid(row=4, column=1, sticky="w", pady=(0, 8), padx=(10, 0))
        tk.Radiobutton(gender_f, text="Male", variable=self.gender_var,
                      value="Male", font=("Arial", 8), bg="white").pack(side=tk.LEFT, padx=(0, 5))
        tk.Radiobutton(gender_f, text="Female", variable=self.gender_var,
                      value="Female", font=("Arial", 8), bg="white").pack(side=tk.LEFT)
        
        # Phone
        tk.Label(f, text="Phone *", font=("Arial", 9, "bold"),
                bg="white").grid(row=5, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.phone_var, font=("Arial", 9),
                width=28).grid(row=6, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        
        # Email
        tk.Label(f, text="Email", font=("Arial", 9, "bold"),
                bg="white").grid(row=7, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.email_var, font=("Arial", 9),
                width=28).grid(row=8, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        
        # Sport Selection
        tk.Label(f, text="Select Sport *", font=("Arial", 9, "bold"),
                bg="white").grid(row=9, column=0, sticky="w", pady=(0, 3))
        
        sports = ["Cricket", "Football", "Basketball", "Tennis", 
                 "Badminton", "Swimming", "Athletics", "Volleyball"]
        sport_combo = ttk.Combobox(f, textvariable=self.sport_var, values=sports,
                                   font=("Arial", 9), width=26, state="readonly")
        sport_combo.grid(row=10, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        
        # Experience Level
        tk.Label(f, text="Experience Level *", font=("Arial", 9, "bold"),
                bg="white").grid(row=11, column=0, columnspan=2, sticky="w", pady=(3, 5))
        
        tk.Checkbutton(f, text="Beginner", variable=self.beginner_var,
                      font=("Arial", 8), bg="white").grid(row=12, column=0, sticky="w", pady=2)
        tk.Checkbutton(f, text="Intermediate", variable=self.intermediate_var,
                      font=("Arial", 8), bg="white").grid(row=13, column=0, sticky="w", pady=2)
        tk.Checkbutton(f, text="Advanced", variable=self.advanced_var,
                      font=("Arial", 8), bg="white").grid(row=14, column=0, sticky="w", pady=2)
        
        # Preferred Days
        tk.Label(f, text="Preferred Days *", font=("Arial", 9, "bold"),
                bg="white").grid(row=11, column=1, sticky="w", pady=(3, 5), padx=(10, 0))
        
        tk.Checkbutton(f, text="Weekdays", variable=self.weekday_var,
                      font=("Arial", 8), bg="white").grid(row=12, column=1, 
                      sticky="w", pady=2, padx=(10, 0))
        tk.Checkbutton(f, text="Weekends", variable=self.weekend_var,
                      font=("Arial", 8), bg="white").grid(row=13, column=1, 
                      sticky="w", pady=2, padx=(10, 0))
        
        # Configure grid
        f.columnconfigure(0, weight=1)
        
        # Buttons
        btn_f = tk.Frame(f, bg="white")
        btn_f.grid(row=15, column=0, columnspan=2, pady=(15, 5))
        
        tk.Button(btn_f, text="Register", command=self.register,
                 bg="#059669", fg="white", font=("Arial", 10, "bold"),
                 padx=25, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT, padx=3)
        
        tk.Button(btn_f, text="Clear", command=self.clear,
                 bg="#dc2626", fg="white", font=("Arial", 10, "bold"),
                 padx=25, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT, padx=3)
    
    def register(self):
        # Validation
        if not self.name_var.get():
            messagebox.showerror("Error", "Enter name!")
            return
        
        if not self.age_var.get():
            messagebox.showerror("Error", "Enter age!")
            return
        
        if not self.phone_var.get():
            messagebox.showerror("Error", "Enter phone!")
            return
        
        # Collect experience
        exp = []
        if self.beginner_var.get(): exp.append("Beginner")
        if self.intermediate_var.get(): exp.append("Intermediate")
        if self.advanced_var.get(): exp.append("Advanced")
        
        if not exp:
            messagebox.showerror("Error", "Select experience level!")
            return
        
        # Collect days
        days = []
        if self.weekday_var.get(): days.append("Weekdays")
        if self.weekend_var.get(): days.append("Weekends")
        
        if not days:
            messagebox.showerror("Error", "Select preferred days!")
            return
        
        # Success message
        msg = f"✓ Registration Successful!\n\n"
        msg += f"ID: {self.reg_id}\n"
        msg += f"Name: {self.name_var.get()}\n"
        msg += f"Age: {self.age_var.get()}\n"
        msg += f"Gender: {self.gender_var.get()}\n"
        msg += f"Sport: {self.sport_var.get()}\n"
        msg += f"Level: {', '.join(exp)}\n"
        msg += f"Days: {', '.join(days)}\n"
        msg += f"\nWelcome to our academy!"
        
        messagebox.showinfo("Success", msg)
        self.clear()
    
    def clear(self):
        self.name_var.set("")
        self.age_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.gender_var.set("Male")
        self.sport_var.set("Cricket")
        self.beginner_var.set(1)
        self.intermediate_var.set(0)
        self.advanced_var.set(0)
        self.weekday_var.set(0)
        self.weekend_var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SportsAcademyForm(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class TinyPatientForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Form")
        self.root.geometry("320x420")
        self.root.resizable(True, True)
        self.root.config(bg="#f0f4f8")
        
        # Variables
        self.id = f"P{datetime.now().strftime('%H%M%S')}"
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="M")
        self.blood_var = tk.StringVar(value="A+")
        
        # Checkboxes
        self.diabetes_var = tk.IntVar()
        self.bp_var = tk.IntVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        hdr = tk.Frame(self.root, bg="#2563eb", height=50)
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)
        
        tk.Label(hdr, text="🏥 Patient Form", font=("Arial", 11, "bold"),
                bg="#2563eb", fg="white").pack(pady=12)
        
        # Main
        main = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=2)
        main.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        f = tk.Frame(main, bg="white", padx=12, pady=12)
        f.pack(fill=tk.BOTH, expand=True)
        
        # ID
        tk.Label(f, text=f"ID: {self.id}", font=("Arial", 8, "bold"),
                bg="white", fg="#2563eb").grid(row=0, column=0, columnspan=2, pady=(0, 8))
        
        # Name
        tk.Label(f, text="Name", font=("Arial", 8, "bold"),
                bg="white").grid(row=1, column=0, sticky="w", pady=(0, 2))
        tk.Entry(f, textvariable=self.name_var, font=("Arial", 8),
                width=22).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 6))
        
        # Age
        tk.Label(f, text="Age", font=("Arial", 8, "bold"),
                bg="white").grid(row=3, column=0, sticky="w", pady=(0, 2))
        tk.Entry(f, textvariable=self.age_var, font=("Arial", 8),
                width=8).grid(row=4, column=0, sticky="w", pady=(0, 6))
        
        # Gender
        tk.Label(f, text="Gender", font=("Arial", 8, "bold"),
                bg="white").grid(row=3, column=1, sticky="w", pady=(0, 2), padx=(8, 0))
        gf = tk.Frame(f, bg="white")
        gf.grid(row=4, column=1, sticky="w", pady=(0, 6), padx=(8, 0))
        tk.Radiobutton(gf, text="M", variable=self.gender_var, value="M",
                      font=("Arial", 7), bg="white").pack(side=tk.LEFT, padx=(0, 4))
        tk.Radiobutton(gf, text="F", variable=self.gender_var, value="F",
                      font=("Arial", 7), bg="white").pack(side=tk.LEFT)
        
        # Phone
        tk.Label(f, text="Phone", font=("Arial", 8, "bold"),
                bg="white").grid(row=5, column=0, sticky="w", pady=(0, 2))
        tk.Entry(f, textvariable=self.phone_var, font=("Arial", 8),
                width=22).grid(row=6, column=0, columnspan=2, sticky="ew", pady=(0, 6))
        
        # Blood
        tk.Label(f, text="Blood", font=("Arial", 8, "bold"),
                bg="white").grid(row=7, column=0, sticky="w", pady=(0, 2))
        ttk.Combobox(f, textvariable=self.blood_var, 
                    values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                    font=("Arial", 8), width=8, state="readonly").grid(row=8, column=0,
                    sticky="w", pady=(0, 6))
        
        # Conditions
        tk.Label(f, text="Conditions", font=("Arial", 8, "bold"),
                bg="white").grid(row=9, column=0, columnspan=2, sticky="w", pady=(3, 3))
        tk.Checkbutton(f, text="Diabetes", variable=self.diabetes_var,
                      font=("Arial", 7), bg="white").grid(row=10, column=0, sticky="w", pady=1)
        tk.Checkbutton(f, text="BP", variable=self.bp_var,
                      font=("Arial", 7), bg="white").grid(row=11, column=0, sticky="w", pady=1)
        
        # Department
        tk.Label(f, text="Dept", font=("Arial", 8, "bold"),
                bg="white").grid(row=12, column=0, columnspan=2, sticky="w", pady=(6, 2))
        
        lbf = tk.Frame(f, bg="white")
        lbf.grid(row=13, column=0, columnspan=2, sticky="w", pady=(0, 8))
        
        sb = tk.Scrollbar(lbf)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.dept = tk.Listbox(lbf, height=3, font=("Arial", 7),
                              yscrollcommand=sb.set, width=25)
        self.dept.pack(side=tk.LEFT)
        sb.config(command=self.dept.yview)
        
        for d in ["Cardiology", "Neurology", "Pediatrics", "General", "Surgery", "Emergency"]:
            self.dept.insert(tk.END, d)
        
        # Buttons
        bf = tk.Frame(f, bg="white")
        bf.grid(row=14, column=0, columnspan=2, pady=(8, 0))
        
        tk.Button(bf, text="Register", command=self.register,
                 bg="#2563eb", fg="white", font=("Arial", 8, "bold"),
                 padx=15, pady=6, relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        
        tk.Button(bf, text="Clear", command=self.clear,
                 bg="#dc2626", fg="white", font=("Arial", 8, "bold"),
                 padx=15, pady=6, relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        
        f.columnconfigure(0, weight=1)
    
    def register(self):
        if not self.name_var.get() or not self.age_var.get() or not self.phone_var.get():
            messagebox.showerror("Error", "Fill all fields!")
            return
        
        if not self.dept.curselection():
            messagebox.showerror("Error", "Select dept!")
            return
        
        cond = []
        if self.diabetes_var.get(): cond.append("Diabetes")
        if self.bp_var.get(): cond.append("BP")
        
        dept = self.dept.get(self.dept.curselection())
        
        msg = f"✓ Registered!\n\n{self.id}\n{self.name_var.get()}\n"
        msg += f"{self.age_var.get()}yr {self.gender_var.get()}\n"
        msg += f"{self.blood_var.get()} | {self.phone_var.get()}\n"
        msg += f"{dept}\n{', '.join(cond) if cond else 'Healthy'}"
        
        messagebox.showinfo("Success", msg)
        self.clear()
    
    def clear(self):
        self.name_var.set("")
        self.age_var.set("")
        self.phone_var.set("")
        self.gender_var.set("M")
        self.blood_var.set("A+")
        self.diabetes_var.set(0)
        self.bp_var.set(0)
        self.dept.selection_clear(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TinyPatientForm(root)
    root.mainloop()
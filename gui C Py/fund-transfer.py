import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

class MiniTransferGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fund Transfer")
        self.root.geometry("350x450")
        self.root.resizable(True, True)
        self.root.config(bg="#f0f0f0")
        
        # Variables
        self.balance = 50000.00
        self.to_account_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.type_var = tk.StringVar(value="IMPS")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#1e3a8a", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="💰 Quick Transfer", font=("Arial", 14, "bold"),
                bg="#1e3a8a", fg="white").pack(pady=15)
        
        # Balance
        bal_frame = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=1)
        bal_frame.pack(fill=tk.X, padx=15, pady=10)
        
        tk.Label(bal_frame, text="Balance", font=("Arial", 8),
                bg="white", fg="#666").pack(pady=(8, 2))
        tk.Label(bal_frame, text=f"₹ {self.balance:,.2f}", 
                font=("Arial", 14, "bold"), bg="white", fg="#059669").pack(pady=(0, 8))
        
        # Form
        form = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=1)
        form.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        f = tk.Frame(form, bg="white", padx=15, pady=15)
        f.pack(fill=tk.BOTH, expand=True)
        
        # Name
        tk.Label(f, text="Name", font=("Arial", 9, "bold"),
                bg="white").grid(row=0, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.name_var, font=("Arial", 9), 
                width=30).grid(row=1, column=0, pady=(0, 10))
        
        # Account
        tk.Label(f, text="Account Number", font=("Arial", 9, "bold"),
                bg="white").grid(row=2, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.to_account_var, font=("Arial", 9),
                width=30).grid(row=3, column=0, pady=(0, 10))
        
        # Amount
        tk.Label(f, text="Amount (₹)", font=("Arial", 9, "bold"),
                bg="white").grid(row=4, column=0, sticky="w", pady=(0, 3))
        tk.Entry(f, textvariable=self.amount_var, font=("Arial", 9),
                width=30).grid(row=5, column=0, pady=(0, 10))
        
        # Type
        tk.Label(f, text="Type", font=("Arial", 9, "bold"),
                bg="white").grid(row=6, column=0, sticky="w", pady=(0, 5))
        
        type_frame = tk.Frame(f, bg="white")
        type_frame.grid(row=7, column=0, sticky="w", pady=(0, 15))
        
        tk.Radiobutton(type_frame, text="IMPS", variable=self.type_var,
                      value="IMPS", font=("Arial", 8), bg="white").pack(side=tk.LEFT, padx=(0, 10))
        tk.Radiobutton(type_frame, text="NEFT", variable=self.type_var,
                      value="NEFT", font=("Arial", 8), bg="white").pack(side=tk.LEFT, padx=(0, 10))
        tk.Radiobutton(type_frame, text="RTGS", variable=self.type_var,
                      value="RTGS", font=("Arial", 8), bg="white").pack(side=tk.LEFT)
        
        # Buttons
        btn_frame = tk.Frame(f, bg="white")
        btn_frame.grid(row=8, column=0, pady=(5, 0))
        
        tk.Button(btn_frame, text="Transfer", command=self.transfer,
                 bg="#1e3a8a", fg="white", font=("Arial", 9, "bold"),
                 padx=20, pady=8, relief=tk.FLAT).pack(side=tk.LEFT, padx=3)
        
        tk.Button(btn_frame, text="Clear", command=self.clear,
                 bg="#6b7280", fg="white", font=("Arial", 9, "bold"),
                 padx=20, pady=8, relief=tk.FLAT).pack(side=tk.LEFT, padx=3)
    
    def transfer(self):
        if not self.name_var.get():
            messagebox.showerror("Error", "Enter name!")
            return
        
        if not self.to_account_var.get():
            messagebox.showerror("Error", "Enter account!")
            return
        
        if not self.amount_var.get():
            messagebox.showerror("Error", "Enter amount!")
            return
        
        try:
            amt = float(self.amount_var.get())
            if amt <= 0:
                messagebox.showerror("Error", "Invalid amount!")
                return
            
            if amt > self.balance:
                messagebox.showerror("Error", "Insufficient balance!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid amount!")
            return
        
        # Process
        trans_id = f"TXN{random.randint(100000, 999999)}"
        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        self.balance -= amt
        
        msg = f"✓ Transfer Successful!\n\n"
        msg += f"ID: {trans_id}\n"
        msg += f"To: {self.name_var.get()}\n"
        msg += f"Amount: ₹{amt:,.2f}\n"
        msg += f"Type: {self.type_var.get()}\n"
        msg += f"Time: {time}\n\n"
        msg += f"Balance: ₹{self.balance:,.2f}"
        
        messagebox.showinfo("Success", msg)
        self.clear()
    
    def clear(self):
        self.to_account_var.set("")
        self.amount_var.set("")
        self.name_var.set("")
        self.type_var.set("IMPS")

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniTransferGUI(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

class MiniFeedbackForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Feedback")
        self.root.geometry("300x350")
        self.root.resizable(True, True)
        
        # Variables
        self.name_var = tk.StringVar()
        self.rating_var = tk.IntVar(value=5)
        self.breakfast_var = tk.IntVar()
        self.lunch_var = tk.IntVar()
        self.dinner_var = tk.IntVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Food Feedback", font=("Arial", 12, "bold"), 
                bg="#3498db", fg="white", pady=8).pack(fill=tk.X)
        
        # Main Frame
        f = tk.Frame(self.root, padx=15, pady=10)
        f.pack()
        
        # Name
        tk.Label(f, text="Name:", font=("Arial", 9)).grid(row=0, column=0, sticky="w", pady=4)
        tk.Entry(f, textvariable=self.name_var, width=20, font=("Arial", 9)).grid(row=0, column=1, pady=4)
        
        # Meals
        tk.Label(f, text="Meals:", font=("Arial", 9, "bold")).grid(row=1, column=0, columnspan=2, sticky="w", pady=(8, 3))
        tk.Checkbutton(f, text="Breakfast", variable=self.breakfast_var, font=("Arial", 8)).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(f, text="Lunch", variable=self.lunch_var, font=("Arial", 8)).grid(row=2, column=1, sticky="w")
        tk.Checkbutton(f, text="Dinner", variable=self.dinner_var, font=("Arial", 8)).grid(row=3, column=0, sticky="w")
        
        # Rating
        tk.Label(f, text="Rating:", font=("Arial", 9, "bold")).grid(row=4, column=0, columnspan=2, sticky="w", pady=(8, 3))
        tk.Scale(f, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.rating_var, 
                length=200, font=("Arial", 8)).grid(row=5, column=0, columnspan=2, pady=3)
        
        # Comments
        tk.Label(f, text="Comments:", font=("Arial", 9, "bold")).grid(row=6, column=0, columnspan=2, sticky="w", pady=(8, 3))
        self.comments = tk.Text(f, width=28, height=4, font=("Arial", 8), wrap=tk.WORD)
        self.comments.grid(row=7, column=0, columnspan=2, pady=3)
        
        # Buttons
        bf = tk.Frame(f)
        bf.grid(row=8, column=0, columnspan=2, pady=10)
        
        tk.Button(bf, text="Submit", command=self.submit, bg="#27ae60", 
                 fg="white", font=("Arial", 9, "bold"), padx=12, pady=4).pack(side=tk.LEFT, padx=3)
        tk.Button(bf, text="Clear", command=self.clear, bg="#95a5a6", 
                 fg="white", font=("Arial", 9, "bold"), padx=12, pady=4).pack(side=tk.LEFT, padx=3)
    
    def submit(self):
        if not self.name_var.get():
            messagebox.showwarning("Warning", "Enter name!")
            return
        
        meals = []
        if self.breakfast_var.get(): meals.append("B")
        if self.lunch_var.get(): meals.append("L")
        if self.dinner_var.get(): meals.append("D")
        
        messagebox.showinfo("Success", f"Thanks {self.name_var.get()}!\nRating: {self.rating_var.get()}/10")
        self.clear()
    
    def clear(self):
        self.name_var.set("")
        self.rating_var.set(5)
        self.breakfast_var.set(0)
        self.lunch_var.set(0)
        self.dinner_var.set(0)
        self.comments.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniFeedbackForm(root)
    root.mainloop()
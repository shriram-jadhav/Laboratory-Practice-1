import tkinter as tk
from tkinter import messagebox

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
        self.root.config(bg="#f0f4f8")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main Container
        main = tk.Frame(self.root, bg="#f0f4f8")
        main.pack(fill=tk.BOTH, expand=True, padx=30, pady=40)
        
        # Logo/Icon
        logo_frame = tk.Frame(main, bg="#3b82f6", width=80, height=80)
        logo_frame.pack(pady=(0, 20))
        logo_frame.pack_propagate(False)
        
        tk.Label(logo_frame, text="🚀", font=("Arial", 40), 
                bg="#3b82f6").pack(expand=True)
        
        # Welcome Text
        tk.Label(main, text="Welcome!", font=("Arial", 24, "bold"),
                bg="#f0f4f8", fg="#1e293b").pack(pady=(0, 5))
        
        tk.Label(main, text="We're glad to have you here", 
                font=("Arial", 11), bg="#f0f4f8", fg="#64748b").pack(pady=(0, 30))
        
        # Features Card
        features = tk.Frame(main, bg="white", relief=tk.RAISED, bd=2)
        features.pack(fill=tk.X, pady=(0, 25))
        
        feat_inner = tk.Frame(features, bg="white", padx=20, pady=15)
        feat_inner.pack(fill=tk.X)
        
        items = [
            ("✓", "Easy to use interface"),
            ("✓", "Secure & reliable"),
            ("✓", "24/7 support available")
        ]
        
        for icon, text in items:
            f = tk.Frame(feat_inner, bg="white")
            f.pack(fill=tk.X, pady=4)
            tk.Label(f, text=icon, font=("Arial", 10), bg="white",
                    fg="#22c55e", width=3).pack(side=tk.LEFT)
            tk.Label(f, text=text, font=("Arial", 9), bg="white",
                    fg="#475569", anchor="w").pack(side=tk.LEFT, fill=tk.X)
        
        # Buttons
        btn_frame = tk.Frame(main, bg="#f0f4f8")
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(btn_frame, text="Get Started", command=self.get_started,
                 bg="#3b82f6", fg="white", font=("Arial", 11, "bold"),
                 padx=40, pady=12, relief=tk.FLAT, cursor="hand2",
                 activebackground="#2563eb").pack(fill=tk.X, pady=(0, 8))
        
        tk.Button(btn_frame, text="Learn More", command=self.learn_more,
                 bg="white", fg="#3b82f6", font=("Arial", 10, "bold"),
                 padx=40, pady=10, relief=tk.SOLID, bd=1, cursor="hand2",
                 activebackground="#eff6ff").pack(fill=tk.X)
        
        # Footer
        footer = tk.Frame(main, bg="#f0f4f8")
        footer.pack(side=tk.BOTTOM, pady=(20, 0))
        
        tk.Label(footer, text="Already have an account?", 
                font=("Arial", 8), bg="#f0f4f8", fg="#64748b").pack(side=tk.LEFT)
        
        login_btn = tk.Label(footer, text="Sign In", font=("Arial", 8, "bold"),
                            bg="#f0f4f8", fg="#3b82f6", cursor="hand2")
        login_btn.pack(side=tk.LEFT, padx=(5, 0))
        login_btn.bind("<Button-1>", lambda e: self.sign_in())
    
    def get_started(self):
        messagebox.showinfo("Get Started", 
                           "Welcome aboard! 🎉\n\nLet's set up your account.")
        self.root.destroy()
    
    def learn_more(self):
        messagebox.showinfo("Learn More", 
                           "Discover all features:\n\n• Dashboard\n• Analytics\n• Reports\n• Settings")
    
    def sign_in(self):
        messagebox.showinfo("Sign In", "Redirecting to login page...")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeScreen(root)
    root.mainloop()
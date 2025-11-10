import tkinter as tk
from tkinter import messagebox

class HelpScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Help")
        self.root.geometry("450x500")
        self.root.resizable(True, True)
        self.root.config(bg="#f8fafc")
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        hdr = tk.Frame(self.root, bg="#1e40af", height=50)
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)
        tk.Label(hdr, text="❓ Help Center", font=("Arial", 13, "bold"),
                bg="#1e40af", fg="white").pack(pady=12)
        
        # Main
        main = tk.Frame(self.root, bg="#f8fafc")
        main.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Categories
        cat_frame = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
        cat_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(cat_frame, text="Topics", font=("Arial", 9, "bold"),
                bg="white").pack(pady=8)
        
        btn_frame = tk.Frame(cat_frame, bg="white")
        btn_frame.pack(pady=(0, 8))
        
        cats = ["Getting Started", "Settings", "FAQ", "Troubleshoot"]
        for cat in cats:
            tk.Button(btn_frame, text=cat, command=lambda c=cat: self.show(c),
                     bg="#e0e7ff", font=("Arial", 8), relief=tk.FLAT,
                     padx=8, pady=4).pack(side=tk.LEFT, padx=3)
        
        # Content
        content = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
        content.pack(fill=tk.BOTH, expand=True)
        
        # Search
        search = tk.Frame(content, bg="white")
        search.pack(fill=tk.X, padx=10, pady=10)
        
        self.search_var = tk.StringVar()
        tk.Entry(search, textvariable=self.search_var, font=("Arial", 9),
                width=25).pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(search, text="Search", command=self.search,
                 bg="#1e40af", fg="white", font=("Arial", 8, "bold"),
                 padx=10, pady=3).pack(side=tk.LEFT)
        
        # Text Area
        text_frame = tk.Frame(content, bg="white")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        sb = tk.Scrollbar(text_frame)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 9),
                           yscrollcommand=sb.set, bg="#f9fafb",
                           relief=tk.FLAT, padx=10, pady=10)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.config(command=self.text.yview)
        
        # Bottom
        bottom = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=1)
        bottom.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        tk.Label(bottom, text="Need Help?", font=("Arial", 8, "bold"),
                bg="white").pack(side=tk.LEFT, padx=10, pady=8)
        tk.Button(bottom, text="📧 Support", command=self.support,
                 bg="#059669", fg="white", font=("Arial", 8, "bold"),
                 padx=10, pady=4).pack(side=tk.LEFT, padx=3)
        tk.Button(bottom, text="💬 Chat", command=self.chat,
                 bg="#7c3aed", fg="white", font=("Arial", 8, "bold"),
                 padx=10, pady=4).pack(side=tk.LEFT, padx=3)
        
        self.show("Getting Started")
    
    def show(self, cat):
        self.text.delete("1.0", tk.END)
        content = {
            "Getting Started": """GETTING STARTED

1. Create Account
   • Sign up with email
   • Verify your email
   • Complete profile

2. Explore Features
   • Main dashboard
   • Tools menu
   • Settings

Tips:
→ Take the tour
→ Watch tutorials""",
            
            "Settings": """SETTINGS

Profile:
• Update info
• Change picture
• Edit preferences

Security:
• Change password
• Enable 2FA
• Review devices

Privacy:
• Data sharing
• Notifications
• Visibility""",
            
            "FAQ": """FAQ

Q: Reset password?
A: Click 'Forgot Password'

Q: Data secure?
A: Yes, encrypted

Q: Mobile app?
A: Yes, on app stores

Q: Export data?
A: Settings → Export

Q: Free trial?
A: Yes, 14 days""",
            
            "Troubleshoot": """TROUBLESHOOTING

Login Issues:
• Reset password
• Clear cache
• Check connection

Slow Performance:
• Close tabs
• Update app
• Check system

Errors:
• Note error code
• Restart app
• Contact support"""
        }
        self.text.insert("1.0", content.get(cat, "Not found"))
    
    def search(self):
        q = self.search_var.get()
        if q:
            messagebox.showinfo("Search", f"Searching: {q}")
        else:
            messagebox.showwarning("Search", "Enter search term")
    
    def support(self):
        messagebox.showinfo("Support", "Email: support@app.com\nPhone: 1-800-555-0100")
    
    def chat(self):
        messagebox.showinfo("Chat", "Connecting to agent...")

if __name__ == "__main__":
    root = tk.Tk()
    app = HelpScreen(root)
    root.mainloop()
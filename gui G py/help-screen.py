import tkinter as tk
from tkinter import messagebox

def contact_support():
    messagebox.showinfo("Contact Support", 
                        "📧 Email: support@smartapp.com\n☎️ Phone: +91 98765 43210")

# Main Window
root = tk.Tk()
root.title("Help - SmartApp")
root.geometry("500x400")
root.configure(bg="#F5F7FA")

# Heading
tk.Label(root, text="🆘 Help & Support Center", 
         font=("Arial", 18, "bold"), fg="#0B5394", bg="#F5F7FA").pack(pady=15)

# Sub-heading
tk.Label(root, text="Need assistance? We're here to help you!", 
         font=("Arial", 11, "italic"), bg="#F5F7FA", fg="gray").pack(pady=5)

# Help Content
help_text = """📋 Common Topics:
• How to use this app: Navigate using the main menu buttons.
• Forgot Password: Use 'Forgot Password' link on the login page.
• Payment Issues: Go to 'Settings → Payment Help'.
• Updating your profile: Visit 'Profile → Edit Info'.
• For bugs or feedback: Click 'Contact Support' below.
"""

help_label = tk.Label(root, text=help_text, justify="left", 
                      font=("Arial", 11), bg="#F5F7FA", fg="black", padx=20)
help_label.pack(pady=10, anchor="w")

# Buttons
btn_frame = tk.Frame(root, bg="#F5F7FA")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Contact Support", bg="#4CAF50", fg="white", 
          font=("Arial", 11, "bold"), width=15, command=contact_support).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Back", bg="#D32F2F", fg="white", 
          font=("Arial", 11, "bold"), width=10, command=root.destroy).grid(row=0, column=1, padx=10)

# Footer
tk.Label(root, text="© 2025 SmartApp Technologies — All Rights Reserved", 
         font=("Arial", 9), bg="#F5F7FA", fg="gray").pack(side="bottom", pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = name_entry.get()
    quality = quality_var.get()
    feedback = feedback_text.get("1.0", "end-1c")
    
    liked = []
    if taste_var.get(): liked.append("Taste")
    if service_var.get(): liked.append("Service")
    if clean_var.get(): liked.append("Cleanliness")
    
    if not name:
        messagebox.showwarning("Missing Info", "Please enter your name!")
        return

    msg = f"✅ Thank you, {name}!\n\nFood Quality: {quality}\nLiked: {', '.join(liked) if liked else 'None'}\nFeedback: {feedback}"
    messagebox.showinfo("Feedback Submitted", msg)

# Main Window
root = tk.Tk()
root.title("🍽️ Hotel Food Feedback Form")
root.geometry("400x450")
root.config(bg="#FFF3E0")

tk.Label(root, text="Customer Feedback Form", font=("Arial", 16, "bold"), bg="#FFF3E0", fg="#BF360C").pack(pady=10)

# Name
tk.Label(root, text="Your Name:", bg="#FFF3E0").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Food Quality (Radiobutton)
tk.Label(root, text="Rate Food Quality:", bg="#FFF3E0").pack()
quality_var = tk.StringVar(value="Excellent")
tk.Radiobutton(root, text="Excellent", variable=quality_var, value="Excellent", bg="#FFF3E0").pack()
tk.Radiobutton(root, text="Good", variable=quality_var, value="Good", bg="#FFF3E0").pack()
tk.Radiobutton(root, text="Average", variable=quality_var, value="Average", bg="#FFF3E0").pack()
tk.Radiobutton(root, text="Poor", variable=quality_var, value="Poor", bg="#FFF3E0").pack()

# What customer liked
tk.Label(root, text="What did you like?", bg="#FFF3E0").pack(pady=5)
taste_var = tk.IntVar()
service_var = tk.IntVar()
clean_var = tk.IntVar()
tk.Checkbutton(root, text="Taste", variable=taste_var, bg="#FFF3E0").pack()
tk.Checkbutton(root, text="Service", variable=service_var, bg="#FFF3E0").pack()
tk.Checkbutton(root, text="Cleanliness", variable=clean_var, bg="#FFF3E0").pack()

# Feedback Text Box
tk.Label(root, text="Additional Comments:", bg="#FFF3E0").pack(pady=5)
feedback_text = tk.Text(root, width=35, height=4)
feedback_text.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit", bg="#4CAF50", fg="white", width=12, command=submit_feedback).pack(pady=10)

root.mainloop()

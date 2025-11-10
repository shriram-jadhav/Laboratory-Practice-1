import tkinter as tk
from tkinter import messagebox

def submit_quiz():
    score = 0
    if q1_var.get() == 1:
        score += 1
    if q2_var.get() == 2:
        score += 1
    if q3_var.get() == 3:
        score += 1

    messagebox.showinfo("Quiz Result", f"🎯 You scored {score}/3")
    clear_quiz()

def clear_quiz():
    q1_var.set(0)
    q2_var.set(0)
    q3_var.set(0)

# Main Window
root = tk.Tk()
root.title("🧠 Online Quiz")
root.geometry("500x500")
root.config(bg="#E8F5E9")

tk.Label(root, text="Welcome to Online Quiz", font=("Arial", 16, "bold"), 
         bg="#E8F5E9", fg="#1B5E20").pack(pady=15)

frame = tk.Frame(root, bg="#E8F5E9")
frame.pack(pady=10)

# Question 1
tk.Label(frame, text="1️ What is the capital of India?", font=("Arial", 11), bg="#E8F5E9").grid(row=0, column=0, sticky="w")
q1_var = tk.IntVar()
tk.Radiobutton(frame, text="Mumbai", variable=q1_var, value=0, bg="#E8F5E9").grid(row=1, column=0, sticky="w")
tk.Radiobutton(frame, text="New Delhi", variable=q1_var, value=1, bg="#E8F5E9").grid(row=2, column=0, sticky="w")
tk.Radiobutton(frame, text="Kolkata", variable=q1_var, value=2, bg="#E8F5E9").grid(row=3, column=0, sticky="w")

# Question 2
tk.Label(frame, text="2️ Which language is used for AI/ML?", font=("Arial", 11), bg="#E8F5E9").grid(row=4, column=0, sticky="w", pady=(10,0))
q2_var = tk.IntVar()
tk.Radiobutton(frame, text="C++", variable=q2_var, value=0, bg="#E8F5E9").grid(row=5, column=0, sticky="w")
tk.Radiobutton(frame, text="Python", variable=q2_var, value=2, bg="#E8F5E9").grid(row=6, column=0, sticky="w")
tk.Radiobutton(frame, text="Java", variable=q2_var, value=1, bg="#E8F5E9").grid(row=7, column=0, sticky="w")

# Question 3
tk.Label(frame, text="3️ Who developed Python?", font=("Arial", 11), bg="#E8F5E9").grid(row=8, column=0, sticky="w", pady=(10,0))
q3_var = tk.IntVar()
tk.Radiobutton(frame, text="Guido van Rossum", variable=q3_var, value=3, bg="#E8F5E9").grid(row=9, column=0, sticky="w")
tk.Radiobutton(frame, text="James Gosling", variable=q3_var, value=1, bg="#E8F5E9").grid(row=10, column=0, sticky="w")
tk.Radiobutton(frame, text="Dennis Ritchie", variable=q3_var, value=2, bg="#E8F5E9").grid(row=11, column=0, sticky="w")

# Buttons
tk.Button(root, text="Submit", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
          width=12, command=submit_quiz).pack(pady=10)
tk.Button(root, text="Clear", bg="#D32F2F", fg="white", font=("Arial", 11, "bold"),
          width=12, command=clear_quiz).pack()

tk.Label(root, text="© 2025 Simple Online Quiz", font=("Arial", 9), bg="#E8F5E9", fg="gray").pack(side="bottom", pady=10)

root.mainloop()

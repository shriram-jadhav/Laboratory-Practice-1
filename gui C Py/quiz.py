import tkinter as tk
from tkinter import messagebox

# Quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which is a programming language?",
        "options": ["Python", "HTML", "CSS", "JSON"],
        "answer": "Python"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", 
                   "Central Program Utility", "Computer Processing Unit"],
        "answer": "Central Processing Unit"
    }
]

current_q = 0
score = 0

def start_quiz():
    global current_q, score
    name = name_entry.get()
    if not name:
        messagebox.showerror("Error", "Please enter your name!")
        return
    
    current_q = 0
    score = 0
    welcome_frame.pack_forget()
    show_question()

def show_question():
    quiz_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
    
    question = questions[current_q]
    question_label.config(text=f"Q{current_q + 1}: {question['question']}")
    
    answer_var.set("")
    for i, option in enumerate(question['options']):
        radio_buttons[i].config(text=option, value=option)

def next_question():
    global current_q, score
    
    if not answer_var.get():
        messagebox.showerror("Error", "Please select an answer!")
        return
    
    # Check answer
    if answer_var.get() == questions[current_q]['answer']:
        score += 1
    
    current_q += 1
    
    if current_q < len(questions):
        show_question()
    else:
        show_results()

def show_results():
    quiz_frame.pack_forget()
    result_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
    
    percentage = (score / len(questions)) * 100
    result_text = f"Quiz Completed!\n\nName: {name_entry.get()}\nScore: {score}/{len(questions)}\nPercentage: {percentage:.1f}%"
    
    if percentage >= 70:
        result_text += "\n\nExcellent! 🎉"
    elif percentage >= 50:
        result_text += "\n\nGood Job! 👍"
    else:
        result_text += "\n\nKeep Practicing! 📚"
    
    result_label.config(text=result_text)

def restart_quiz():
    result_frame.pack_forget()
    name_entry.delete(0, tk.END)
    welcome_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

# Main window
root = tk.Tk()
root.title("Online Quiz")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="ONLINE QUIZ", font=("Arial", 20, "bold"), bg="#2196F3", fg="white", pady=15).pack(fill=tk.X)

# Welcome Frame
welcome_frame = tk.Frame(root, bg="#f0f0f0")
welcome_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

tk.Label(welcome_frame, text="Welcome to the Quiz!", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

tk.Label(welcome_frame, text="Enter Your Name:", font=("Arial", 11), bg="#f0f0f0").pack(pady=5)
name_entry = tk.Entry(welcome_frame, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

info_text = tk.Text(welcome_frame, height=6, width=50, font=("Arial", 10), bg="white", wrap=tk.WORD)
info_text.pack(pady=15)
info_text.insert(tk.END, 
    "Instructions:\n\n"
    "• Total Questions: 3\n"
    "• Each question has 4 options\n"
    "• Select one answer and click Next\n"
    "• Your score will be shown at the end"
)
info_text.config(state=tk.DISABLED)

tk.Button(welcome_frame, text="Start Quiz", command=start_quiz, bg="#4CAF50", 
         fg="white", font=("Arial", 12, "bold"), width=15, cursor="hand2").pack(pady=15)

# Quiz Frame
quiz_frame = tk.Frame(root, bg="white")

question_label = tk.Label(quiz_frame, text="", font=("Arial", 13, "bold"), 
                         bg="white", wraplength=500, justify=tk.LEFT)
question_label.pack(pady=30, padx=20)

answer_var = tk.StringVar()
radio_buttons = []

options_frame = tk.Frame(quiz_frame, bg="white")
options_frame.pack(pady=10)

for i in range(4):
    rb = tk.Radiobutton(options_frame, text="", variable=answer_var, value="", 
                       font=("Arial", 11), bg="white", anchor=tk.W)
    rb.pack(fill=tk.X, pady=8, padx=30)
    radio_buttons.append(rb)

tk.Button(quiz_frame, text="Next Question →", command=next_question, bg="#2196F3", 
         fg="white", font=("Arial", 12, "bold"), width=15, cursor="hand2").pack(pady=30)

# Result Frame
result_frame = tk.Frame(root, bg="white")

result_label = tk.Label(result_frame, text="", font=("Arial", 14), bg="white", justify=tk.CENTER)
result_label.pack(pady=50)

button_frame = tk.Frame(result_frame, bg="white")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Restart Quiz", command=restart_quiz, bg="#2196F3", 
         fg="white", font=("Arial", 11, "bold"), width=12).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Exit", command=root.quit, bg="#f44336", 
         fg="white", font=("Arial", 11, "bold"), width=12).pack(side=tk.LEFT, padx=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def transfer_funds():
    sender = sender_entry.get()
    receiver = receiver_entry.get()
    amount = amount_entry.get()
    mode = mode_var.get()
    note = note_text.get("1.0", "end-1c")

    if not sender or not receiver or not amount:
        messagebox.showwarning("Missing Info", "Please fill all required fields!")
        return
    
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid positive number for amount.")
        return

    messagebox.showinfo("Transaction Successful", 
                        f"✅ Transaction Completed Successfully!\n\n"
                        f"Sender: {sender}\nReceiver: {receiver}\n"
                        f"Amount: ₹{amount:.2f}\nMode: {mode}\nNote: {note if note else 'None'}")

    clear_form()

def clear_form():
    sender_entry.delete(0, tk.END)
    receiver_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    note_text.delete("1.0", tk.END)
    mode_var.set("UPI")

# Main window
root = tk.Tk()
root.title("💰 Fund Transfer Screen")
root.geometry("500x500")
root.config(bg="#E8F0FE")

tk.Label(root, text="Fund Transfer / Transaction", 
         font=("Arial", 18, "bold"), fg="#1A237E", bg="#E8F0FE").pack(pady=15)

# Frame for fields
frame = tk.Frame(root, bg="#E8F0FE")
frame.pack(pady=10)

# Sender Name
tk.Label(frame, text="Sender Name:", font=("Arial", 11), bg="#E8F0FE").grid(row=0, column=0, sticky="e", pady=5)
sender_entry = tk.Entry(frame, width=30)
sender_entry.grid(row=0, column=1, pady=5)

# Receiver Name
tk.Label(frame, text="Receiver Name:", font=("Arial", 11), bg="#E8F0FE").grid(row=1, column=0, sticky="e", pady=5)
receiver_entry = tk.Entry(frame, width=30)
receiver_entry.grid(row=1, column=1, pady=5)

# Amount
tk.Label(frame, text="Amount (₹):", font=("Arial", 11), bg="#E8F0FE").grid(row=2, column=0, sticky="e", pady=5)
amount_entry = tk.Entry(frame, width=20)
amount_entry.grid(row=2, column=1, sticky="w", pady=5)

# Payment Mode (Radiobutton)
tk.Label(frame, text="Payment Mode:", font=("Arial", 11), bg="#E8F0FE").grid(row=3, column=0, sticky="e", pady=5)
mode_var = tk.StringVar(value="UPI")
mode_frame = tk.Frame(frame, bg="#E8F0FE")
mode_frame.grid(row=3, column=1, sticky="w")
tk.Radiobutton(mode_frame, text="UPI", variable=mode_var, value="UPI", bg="#E8F0FE").pack(anchor="w")
tk.Radiobutton(mode_frame, text="Net Banking", variable=mode_var, value="Net Banking", bg="#E8F0FE").pack(anchor="w")
tk.Radiobutton(mode_frame, text="Card", variable=mode_var, value="Card", bg="#E8F0FE").pack(anchor="w")

# Note (Text box)
tk.Label(frame, text="Transaction Note:", font=("Arial", 11), bg="#E8F0FE").grid(row=4, column=0, sticky="ne", pady=5)
note_text = tk.Text(frame, width=30, height=4)
note_text.grid(row=4, column=1, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#E8F0FE")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Transfer", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
          width=12, command=transfer_funds).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", bg="#D32F2F", fg="white", font=("Arial", 11, "bold"),
          width=12, command=clear_form).grid(row=0, column=1, padx=10)

# Footer
tk.Label(root, text="© 2025 EasyPay Transfers", font=("Arial", 9), bg="#E8F0FE", fg="gray").pack(side="bottom", pady=10)

root.mainloop()

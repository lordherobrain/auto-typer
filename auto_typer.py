import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

def start_typing():
    msg = message_entry.get()
    try:
        count = int(count_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Count must be a number")
        return

    messagebox.showinfo("Instructions", 
                        "After clicking OK, you have 5 seconds.\n"
                        "Click on the text box where you want typing to start.")

    time.sleep(5)

    for i in range(count):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")

# GUI
root = tk.Tk()
root.title("Auto Typer ")

tk.Label(root, text="Message").pack()
message_entry = tk.Entry(root, width=40)
message_entry.pack()

tk.Label(root, text="NO").pack()
count_entry = tk.Entry(root, width=10)
count_entry.pack()

tk.Button(root, text="Start", command=start_typing).pack(pady=10)

root.mainloop()

import tkinter as tk
from config import *

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def display_card():
    pass

french_label = tk.Label(text="French", font=(FONT_NAME, 32, "italic"), bg=BACKGROUND_COLOR, fg="white")
french_label.grid(row=0, column=1)

word_label = tk.Label(text="Word...", font=(FONT_NAME, 40, "bold"), bg=BACKGROUND_COLOR, fg="white")
word_label.grid(row=1, column=1)

wrong_button = tk.Button(text="Got it wrong", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR)
wrong_button.grid(row=2, column=0)

show_translation_button = tk.Button(text="Show translation", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR)
show_translation_button.grid(row=2, column=1)

right_button = tk.Button(text="Got it right", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR)
right_button.grid(row=2, column=2)

window.lift()
window.focus_force()
window.mainloop()

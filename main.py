import tkinter as tk
import pandas as pd
from config import *

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

df = pd.read_csv("./data/french_words.csv")
random_row = None

score = 0

def display_foreign_word():
    global random_row
    random_row = df.sample(n=1).iloc[0]
    title.config(text="French")
    french_word = random_row["French"]
    word_label.config(text=french_word)

def display_english_word():
    global random_row
    title.config(text="English")
    english_word = random_row["English"]
    word_label.config(text=english_word)

def record_answer(is_correct):
    global score
    if is_correct:
        score += 1
    else:
        score -= 1
    score_label.config(text=f"Score: {score}")
    display_foreign_word()

score_label = tk.Label(text=f"Score: {score}", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR, fg="white")
score_label.grid(row=3, column=1)

title = tk.Label(text="French", font=(FONT_NAME, 32, "italic"), bg=BACKGROUND_COLOR, fg="white")
title.grid(row=0, column=1)

word_label = tk.Label(text="Word...", font=(FONT_NAME, 40, "bold"), bg=BACKGROUND_COLOR, fg="white", padx=20, pady=20)
word_label.grid(row=1, column=1)

wrong_button = tk.Button(text="Got it wrong", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR, command=lambda: record_answer(False))
wrong_button.grid(row=2, column=0)

show_translation_button = tk.Button(text="Show translation", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR, command=display_english_word)
show_translation_button.grid(row=2, column=1)

right_button = tk.Button(text="Got it right", font=(FONT_NAME, 14), bg=BACKGROUND_COLOR, command=lambda: record_answer(True))
right_button.grid(row=2, column=2)

display_foreign_word()

window.lift()
window.focus_force()
window.mainloop()

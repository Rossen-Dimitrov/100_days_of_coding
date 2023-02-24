import random
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_image)


def is_known():
    to_learn.remove(current_word)
    next_card()
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)



window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_back_image = PhotoImage(file="images/card_back.png")
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=3, command=is_known)
known_button.grid(row=2, column=1)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=3, command=next_card)
unknown_button.grid(row=2, column=0)

next_card()

window.mainloop()

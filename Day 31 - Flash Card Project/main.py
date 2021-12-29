from tkinter import *
from tkinter import messagebox
import pandas
import random
random_word = {}
BACKGROUND_COLOR = "#B1DDC6"
learnt_all = False


try:
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
        word_dict = data.to_dict("records")
    except pandas.errors.EmptyDataError:
        messagebox.showinfo(title="Congrats!", message="You have learnt all words!")
        learnt_all = True
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    word_dict = data.to_dict("records")

def gen_random_French():
    global flip_timer, word_dict, random_word
    # cancel timer countdown when click button continuously (invalidate timer)
    # print(word_dict)
    window.after_cancel(flip_timer)
    canvas.create_image(400, 263, image=card_front)
    title_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill = "black")
    french_word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill = "black")
    try:
        random_word = random.choice(word_dict)
        french_word = random_word["French"]
        eng_word = random_word["English"]
        canvas.itemconfig(french_word_text, text = french_word)
        flip_timer = window.after(3000, flip_card, eng_word)
    except IndexError:
        canvas.itemconfig(title_text, text="Well Done!!")
        canvas.itemconfig(french_word_text, text="You have learnt all words!", font = ("Arial", 40, "normal"))
        right_button["state"] = "disabled"
        wrong_button["state"] = "disabled"


def flip_card(Eng_word):
    canvas.create_image(400, 263, image=card_back)
    canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill = "white")
    eng_word_text = canvas.create_text(400, 263, text= Eng_word, font=("Arial", 60, "bold"), fill = "white")


def learnt():
    global random_word
    # print(random_word)
    word_dict.remove(random_word)
    gen_random_French()

def save_data():
    if messagebox.askokcancel(title="Goodbye", message="Your progress will be saved"):
        df = pandas.DataFrame(word_dict)
        df.to_csv("data/words_to_learn.csv", index = False)
        window.destroy()

window = Tk()
window.title("Flashy")
window.config(width=3000, height=1950, padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=learnt)
right_button.grid(row=1, column=1, sticky="N")

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=gen_random_French)
wrong_button.grid(row=1, column=0, sticky="N")

if not learnt_all:
    gen_random_French()
    window.protocol("WM_DELETE_WINDOW", save_data)
else:
    window.destroy()

window.mainloop()


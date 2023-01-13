from pathlib import Path
import random
from tkinter import Label

import customtkinter
from PIL import Image, ImageTk

BASE_PATH = Path(__file__).parent.resolve()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initialize master widget root
root = customtkinter.CTk()

root.title("Simon Cateau Tkinter - Magic 8 Ball!")
root.iconbitmap(
    Path(__file__).parent.resolve().joinpath("images", "codemy.ico").resolve()
)
root.geometry("500x500")

# Functions
def shake():
    """
    Shake the 8 ball
    """
    answers: dict[str, str] = {
        "It is certain": "green",
        "It is decidedly so": "green",
        "Without a doubt": "green",
        "Yes definitely": "green",
        "You may rely on it": "green",
        "As I see it, yes": "green",
        "Most likely": "green",
        "Outlook good": "green",
        "Yes": "green",
        "Signs point to yes": "green",
        "Reply hazy, try again": "yellow",
        "Ask again later": "yellow",
        "Better not tell you now": "yellow",
        "Cannot predict now": "yellow",
        "Concentrate and ask again": "yellow",
        "Don't count on it!": "red",
        "My reply is no!": "red",
        "My sources say no!": "red",
        "Outlook not so good!": "red",
        "Very doubtful!": "red",
    }

    # Convert dictionary to list
    answer_list = list(answers.items())
    # Shuffle the list
    random.shuffle(answer_list)
    # print(answer_list)
    # Output to the screen
    results.configure(text=answer_list[0][0], fg=answer_list[0][1])   



# Define Images
ball = ImageTk.PhotoImage(
    image=Image.open(Path(BASE_PATH, "images", "8ball.png").resolve())
)
ball_image = Label(master=root, image=ball, bd=0)
ball_image.pack(pady=35)

# Set Results
results = Label(master=root, text="", font=("Helvetica", 28), bg="#1a1a1a")
results.pack(pady=20)

# Define the Button
my_button = customtkinter.CTkButton(
    master=root,
    text="Shake 8-Ball",
    width=190,
    height=40,
    compound="top",
    command=shake,
)
my_button.pack(pady=30)

root.mainloop()

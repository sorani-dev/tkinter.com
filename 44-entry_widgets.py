from pathlib import Path
from tkinter import END

import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Entry Fields!")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico").resolve())
root.geometry("600x350")


def submit():
    """submit Get the results of the Entry"""
    my_label.configure(text=f"Hello {my_entry.get()}")
    my_entry.configure(state="disabled")


def clear():
    """Clear th eEntry box"""
    my_entry.configure(state="normal")
    my_entry.delete(0, END)


my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter Your Name",
    height=50,
    width=200,
    font=("Helvetica", 18),
    corner_radius=50,
    text_color="green",
    placeholder_text_color="darkblue",
    fg_color=("blue", "lightblue"),  # (outer, inner)
)
my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)

root.mainloop()

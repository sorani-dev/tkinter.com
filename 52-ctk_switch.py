from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Switch"
DIMENSIONS = "700x300"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def switcher():
    """switcher Action of my_switch CTKSwitch"""
    my_label.configure(text=switch_var.get())


def toggle():
    """toggle Toggle the switch using the CTKButton my_button"""
    # my_switch.deselect()
    # my_switch.select()
    my_switch.toggle()


# Create a StringVar
switch_var = customtkinter.StringVar(value="on")
# Create Switch
my_switch = customtkinter.CTkSwitch(
    root,
    text="Switch",
    command=switcher,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
    # The two following properties change the area around the switch,
    #   not the switch itself
    # width=200, # Changes the width around the switch
    # height=100, # Changes the height around the switch
    # Change switch dimensions
    switch_width=200,
    switch_height=25,
    corner_radius=10,  # Rounding at the corners: values are the lower, the more square it goes, the height, the rounder it is
    border_color="orange",
    border_width=5,
    fg_color="red",  # "off" switch color of the bar
    progress_color="green",
    button_color="pink",
    button_hover_color="blue",
    font=("Helvetica", 24),
    text_color="lightgreen",
    state="normal",  # "disabled", "normal" (default: "normal")
)
my_switch.pack(pady=40)


# Craete a Label
my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)

# Create a Button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=toggle)
my_button.pack(pady=10)


root.mainloop()

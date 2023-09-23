from pathlib import Path
from tkinter import StringVar, Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Radio Buttons"
DIMENSIONS = "500x550"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def clicker():
    """clicker Validate radio buttons submit"""
    my_label.config(text=f"You Selected: {my_topping.get()}")


# Create Radio Button List
toppings = [
    "Pepperoni",
    "Cheese",
    "Veggie",
]

# Create a Tkinter Variable To Keep Track of Everything
my_topping = StringVar()

# Loop through the list and create radio buttons with validation on Button click
for topping in toppings:
    tb.Radiobutton(
        root, bootstyle="danger", variable=my_topping, text=topping, value=topping
    ).pack(pady=20)

# Create Button
my_button = tb.Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=20)

# Create Label
my_label = tb.Label(root, text="Tou Selected: ")
my_label.pack(pady=20)


# Create actual Radio Button Buttons manually
radiobutton1 = tb.Radiobutton(
    root,
    bootstyle="info toolbutton",
    variable=my_topping,
    text="Radio Button 1",
    value="Radio Button 1",
    command=clicker,
)
radiobutton1.pack(pady=20)

radiobutton2 = tb.Radiobutton(
    root,
    bootstyle="info toolbutton outline",
    variable=my_topping,
    text="Radio Button 2",
    value="Radio Button 2",
    command=clicker,
)
radiobutton2.pack(pady=20)

root.mainloop()

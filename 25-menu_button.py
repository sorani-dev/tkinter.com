from pathlib import Path
from tkinter import StringVar, Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Menu Button!"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def stuff(x: str):
    """stuff Actions  on menu change

    :param x: item menu text
    :type x: str
    """
    # Update Menu based on the current item text passed
    my_menu.config(bootstyle=x)

    # Label text corresponds to current item text passed
    my_label.config(text=f"You selected: {x}")
    print(item_var.get())


# Top menu
my_menu = tb.Menubutton(root, bootstyle="warning", text="Things!")
my_menu.pack(pady=20)


# Basic menu (for sub menu)
inside_menu = tb.Menu(my_menu)

# Add items to inside menu
item_var = StringVar()

# List of items for the inside_menu
for x in [
    "primary",
    "secondary",
    "danger",
    "info",
    "outline primary",
    "outline secondary",
    "outline danger",
    "outline info",
]:
    inside_menu.add_radiobutton(
        label=x, variable=item_var, command=lambda x=x: stuff(x)
    )

# Associate the inside menu with the menubutton
my_menu["menu"] = inside_menu

# Create a label
my_label = tb.Label(root, text="")
my_label.pack(pady=40)

root.mainloop()

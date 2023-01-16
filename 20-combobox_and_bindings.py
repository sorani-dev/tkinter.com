from ctypes.wintypes import PCHAR
from pathlib import Path
from tkinter import Tk, Event
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables 
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE:str = "" 
DIMENSIONS = "500x350"

# Make app
root:Tk = tb.Window(themename="superhero")
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

def on_click()->None:
    """
    Display a messsage on button click
    """
    my_label.config(text=f"You Clicked On {my_combo.get()}!")

def clicker() ->None:
    # Button click 
    on_click()

def click_bind(e) ->None:
    """
    Binding function for the combobox

    Args:
        Event (e): Event passed from the binding handler
    """
    on_click()


# Create Label
my_label = tb.Label(master=root, text="Hello World!", font=("Helvetica0, 18"))
my_label.pack(pady=20)

# Create dropbox options
days = ("Monday", "Tuesday", "Wednesday", "Thirsday", "Friday", "Saturday", "Sunday")

# Create Combobox
my_combo = tb.Combobox(root, bootstyle=SUCCESS, values=days)
my_combo.pack(pady=20)

# Set Combo default value
my_combo.current(0)

# Create a Button
my_button = tb.Button(master=root, text="Click Me!", command=clicker, bootstyle=DANGER)
my_button.pack(pady=20)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)


root.mainloop()

from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Meter!"
DIMENSIONS = "500x700"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Set up a counter
global counter
counter = 20


def clicker():
    """clicker Move the meter up manually"""
    # Create a counter
    global counter

    if counter <= 100:
        my_meter.configure(amountused=counter)
        counter += 5

        my_button.configure(text=f"Click Me {my_meter.amountusedvar.get()}")


def up():
    """up Move meter up"""
    my_meter.step(10)


def down():
    """Move meter down"""
    if my_meter.amountusedvar.get() > 0:
        my_meter.step(-10)


my_meter = tb.Meter(
    root,
    bootstyle="danger",
    subtext="Tkinter Learned",  # Supplemental text that appears below the center text.
    interactive=True,  # Indicates that the user may adjust the meter value with mouse interaction.
    textright="%",
    # textleft="$",
    metertype="full",  # ('full', 'semi'). Default FULL. Displays the meter as a full circle or semi-circle
    stripethickness=10,  # indicator can be displayed as a solid band or as striped wedges around the arc
    metersize=200,  # The meter is square. This represents the size of one side if the square as measured in screen units.
    padding=50,
    amountused=0,  # Current value of the meter (starting value passed to __init__)
    amounttotal=100,  # The maximum value of the meter.
    subtextstyle="light",  # The bootstyle color of the subtext.
)
my_meter.pack(pady=50)

# Move up manually with a counter variable
my_button = tb.Button(root, text="Click Me, +5", command=clicker)
my_button.pack(pady=20)

# Move up
my_button2 = tb.Button(root, text="Step Up", command=up)
my_button2.pack(pady=20)

my_button3 = tb.Button(root, text="Setp Down", command=down)
my_button3.pack(pady=20)

root.mainloop()

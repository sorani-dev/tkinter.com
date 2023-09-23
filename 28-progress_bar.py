import time
from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Progress Bars!"
DIMENSIONS = "500x250"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def increment():
    """increment Increment progress bar by 20 units"""
    # Standard way
    # my_progress.step(20)
    # Alternate way
    my_progress["value"] += 20
    # Get current value of the progress bar and put in label for display
    my_label.config(text=my_progress["value"])


def start():
    """start Start the progress bar"""
    my_progress.start(10)


def stop():
    """stop Stop the progress bar"""
    my_label.config(text=my_progress["value"])
    # Sop progress
    my_progress.stop()


def auto():
    """auto Let the prohress bar move automatically"""
    # For progress bar value: go from 20 to 100, [20, 40, 60, 80, 100]
    for _ in range(5):
        my_progress["value"] += 20
        # Get current value of the progress bar and put in label for display
        my_label.config(text=my_progress["value"])
        # Update the diplay of windows, not the process events called by the user
        # Update one at a time, not all at once
        root.update_idletasks()
        # 1 second per increment at a time
        time.sleep(1)


# Progress Bar
# my_progress = tb.Progressbar(
#     root,
#     bootstyle="danger",
#     maximum=100,  # Maximum number the progress bar can go to
#     mode="determinate",  # determinate, indeterminate
#     length=200,  # How physically big the progress bar is
#     value=20,  # Starting value
# )

# Progress Bar

my_progress = tb.Progressbar(
    root,
    bootstyle="danger",
    maximum=100,  # Maximum number the progress bar can go to
    mode="determinate",  # determinate: goes from left to right (start value to maximum)
    length=300,  # How physically big the progress bar is
    value=0,  # Starting value
)

# my_progress = tb.Progressbar(
#     root,
#     bootstyle="danger striped",
#     maximum=100,  # Maximum number the progress bar can go to
#     mode="indeterminate",  # indeterminate: go from left to right then back to left incresingly
#     length=300,  # How physically big the progress bar is
#     value=0,  # Starting value
# )

my_progress.pack(pady=40)

# Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)


# Buttons
my_button = tb.Button(
    my_frame, text="Increment 20", bootstyle="info", command=increment
)
my_button.grid(column=0, row=0, padx=10)


my_button1 = tb.Button(my_frame, text="Start", bootstyle="info", command=start)
my_button1.grid(column=1, row=0, padx=10)

my_button2 = tb.Button(my_frame, text="Stop", bootstyle="info", command=stop)
my_button2.grid(column=2, row=0, padx=10)

my_button3 = tb.Button(my_frame, text="Auto", bootstyle="info", command=auto)
my_button3.grid(column=3, row=0, padx=10)


# Label to get the current value
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()

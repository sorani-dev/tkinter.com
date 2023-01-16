from pathlib import Path
from tkinter import IntVar, Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "All types of Buttons"
DIMENSIONS = "500x350"


# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# App vars
# Checkbutton
var1 = IntVar()

# Functions
def change_check(checked: int = 1) -> None:
    if checked == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")


def checker_check() -> None:
    change_check(var1.get())


def checker_tool() -> None:
    change_check(var2.get())


# Label
my_label = tb.Label(
    master=root, text="Click the checkbutton below", font=("Helvetica", 18)
)
my_label.pack(pady=(40, 10))

# Check button
my_checkbox = tb.Checkbutton(
    master=root,
    text="Check Me Out!",
    variable=var1,
    bootstyle="primary",
    onvalue=1,
    offvalue=0,
    # command=checker_check,
    command=lambda: change_check(var1.get()),
)
my_checkbox.pack(pady=10)

# Toolbutton
var2 = IntVar()
my_checktool = tb.Checkbutton(
    master=root,
    bootstyle=(DANGER, TOOLBUTTON),
    text="Toolbutton!!",
    variable=var2,
    onvalue=1,
    offvalue=0,
    # command=checker_tool,
    command=lambda: change_check(var2.get()),
)
my_checktool.pack(pady=10)

# Outlines Toolbutton
var3 = IntVar()
my_checkoutlinetool = tb.Checkbutton(
    master=root,
    bootstyle=(DANGER, TOOLBUTTON, OUTLINE),
    text="Outlined Toolbutton!!",
    variable=var3,
    onvalue=1,
    offvalue=0,
    # command=checker_tool,
    command=lambda: change_check(var3.get()),
)
my_checkoutlinetool.pack(pady=10)

# Round Toggle Button
var4 = IntVar()
my_checkroundbutton = tb.Checkbutton(
    master=root,
    bootstyle=(SUCCESS, ROUND, TOGGLE),
    # bootstyle=("success, round-toggle"),
    text="Round Toggle!!",
    variable=var4,
    onvalue=1,
    offvalue=0,
    # command=checker_tool,
    command=lambda: change_check(var4.get()),
)
my_checkroundbutton.pack(pady=10)

# Square Toggle Button
var5 = IntVar()
my_checksquarebutton = tb.Checkbutton(
    master=root,
    bootstyle=(WARNING, SQUARE, TOGGLE),
    # bootstyle=("warning, square-toggle"),
    text="Square Toggle!!",
    variable=var5,
    onvalue=1,
    offvalue=0,
    # command=checker_tool,
    command=lambda: change_check(var5.get()),
)
my_checksquarebutton.pack(pady=10)


root.mainloop()

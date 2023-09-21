from datetime import date
from pathlib import Path
from tkinter import Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

from ttkbootstrap.dialogs import Querybox

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "DateEntry"
DIMENSIONS = "500x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

def get_date():
    """get_date Populate the label from the selected date
    """
    my_label.config(text=f"You picked: {my_date.entry.get()}")


def get_calendar():
    """ Open a calendar in a dialog box and send the selected date to my_label
    """
    cal = Querybox()
    my_label.config(text=f"You picked: {cal.get_date()}")

my_date = tb.DateEntry(master=root, bootstyle=DANGER, startdate=date(2023, 2, 14), firstweekday=0)
my_date.pack(pady=50)



my_button = tb.Button(root, text="Get Date",bootstyle="danger outline", command=get_date)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Calendar",bootstyle="success outline", command=get_calendar)
my_button2.pack(pady=20)


my_label = tb.Label(root, text="You picked: ")
my_label.pack(pady=20)

root.mainloop()

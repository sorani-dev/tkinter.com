from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Message Box"
DIMENSIONS = "700x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
# Main App Icon
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())

root.geometry(DIMENSIONS)

# Message Box Icon
root.iconbitmap(default=Path(BASE_PATH, "images", "codemy.ico").resolve())


def clicker():
    """clicker Open Message Box on button click"""
    # Create a Dialog
    # Returns a str value

    # Methods available:
    # - yesno (returns yes/no),
    # - ok (returns None),
    # - okcancel (returns Ok/Cancel),
    # - show_info (returns None),
    # - show_error (returns None),
    # - show_question (returns yes/No),
    # - show_warning (returns None),
    # - yesnocancel (returns yes/no/cancel),
    # - retrycancel (returns Retry/Cancel)

    # mb = Messagebox.yesno("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.ok("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.okcancel("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.show_info("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.show_error("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.show_question("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.show_warning("Display Some Message Here", title="Here is the Title")
    # mb = Messagebox.yesnocancel("Display Some Message Here", title="Here is the Title")
    mb = Messagebox.retrycancel("Display Some Message Here", title="Here is the Title")

    print("mb result:", mb)

    # Logic based on the result of a yesno message box
    # if mb == "Non":
    #     print("No")
    # else:
    #     print("Yes")

    # Logic based on the result of a ok message box
    # if mb == "None":
    #     print("None")
    # else:
    #     print("Ok")

    # Display result of message box
    my_label.config(text=f"You Clicked: {mb}")


my_button = tb.Button(root, text="Click Me!", bootstyle=DANGER, command=clicker)
my_button.pack(pady=40)

my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)
root.mainloop()

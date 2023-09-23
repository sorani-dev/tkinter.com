from pathlib import Path
from tkinter import Tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Treeview"
DIMENSIONS = "700x350"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Define Colums
columns = ("first_name", "last_name", "email")

# Create Treeview
my_tree = tb.Treeview(root, bootstyle=SUCCESS, columns=columns, show="headings")
my_tree.pack(pady=20)

# Define Headings
my_tree.heading("first_name", text="First Name")
my_tree.heading("last_name", text="Last Name")
my_tree.heading("email", text="Email Address")


# Create Sample Data
contacts = []

for n in range(1, 20):
    contacts.append((f"First {n}", f"Last {n}", f"email{n}@invalid.tld"))

# Add Data to Treeview
for contact in contacts:
    my_tree.insert("", END, values=contact)

root.mainloop()

from pathlib import Path
from tkinter import Tk, ttk

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Style Individual Widgets"
DIMENSIONS = "500x350"

# Make app
root: Tk = Tk()
root.title(f"Simon Cateau Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)

# Define a Style Widget
style = ttk.Style()
style.theme_use("default")

# Widget Style Names
# Almost all widget name for styling start with T and then widget name (e.g.: Button, Label,...)
# examples: TButton, TLabel, ...
"""
Widget Style Names
Button: TButton
Checkbutton: TCheckbutton
Combobox: TCombobox
Entry: TEntry
Frame: TFrame
Label: TLabel
LabelFrame: TLabelFrame
Menubutton: TMenubutton
Notebook: TNotebook
PanedWindow: TPanedwindow
Progressbar:  Horizontal.TProgressbar or Vertical.TProgressbar
Radiobutton: TRadiobutton
Scale: Horizontal.TScale or Vertical.TScale
Scrollbar: Horizontal.TScrollbar or Vertical.TScrollbar
Separator: TSeparator
Sizegrip: TSizegrip
Treeview: Treeview
"""

style.configure(
    "elder.TButton",
    foreground="white",
    background="#003066",
    font=("Helvetica", 24),
    padding=[
        10,
        10,
        10,
        10,
    ],  # padding left, padding right, padding top, padding bottom
)

style.map('elder.TButton', background=[('active', '#004ea5')])

# Create some Buttons
my_button1 = ttk.Button(master=root, text="Login", style="elder.TButton")
my_button1.pack(pady=40)

my_button2 = ttk.Button(master=root, text="Exit", style="elder.TButton")
my_button2.pack(pady=20)

root.mainloop()

from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Segmented Buttons!"
DIMENSIONS = "700x300"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def clicker(value):
    """clicker Action of segmented buton click

    Arguments:
        value -- Value passed to the function by the click of the button
    """
    print(value)
    my_label.configure(text=f"Hello {value}")
    # my_label.configure(text=f"Hello {my_seg_button.get()}")


# Button values
my_values = ["John", "April", "Wess", "Alice"]
# Create the button
my_seg_button = customtkinter.CTkSegmentedButton(
    root,
    values=my_values,
    command=clicker,
    width=300,
    height=100,
    font=("Helvetica", 18),
    corner_radius=3,  # corner_radius = 50: rounds the whole Segment and rounds each buttons
    border_width=5,
    fg_color="magenta",
    selected_color="green",
    selected_hover_color="purple",
    unselected_color="lightgreen",
    unselected_hover_color="maroon",
    text_color="yellow",
    state="normal",  # 'normal' or 'disabled' (default: 'normal')
    text_color_disabled="blue",  # default: greylike
    dynamic_resizing=True,  # True, False (default :True)
)
my_seg_button.pack(pady=40)

# Set  the default Selection
my_seg_button.set("April")

# Label
my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()

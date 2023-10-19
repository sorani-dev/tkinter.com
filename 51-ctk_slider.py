from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Slider"
DIMENSIONS = "700x300"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def sliding(value: float):
    """sliding Manage slider

    Arguments:
        value -- Slider current value
    """
    my_label.configure(text=int(value))


my_slider = customtkinter.CTkSlider(
    root,
    from_=0,
    to=100,
    command=sliding,
    orientation="horizonal",  # "horizonal", "vezrtical" (default: "horizontal")
    number_of_steps=10,  # default: 1
    width=400,
    height=50,
    # border_width=2,
    fg_color="red",
    progress_color="green",
    button_color="yellow",
    button_hover_color="lightblue",
    state="normal",  # "normal", "disabled", (default: "normal")
    hover=True,  # True, False (default: True)
)

my_slider.pack(pady=40)

# Define starting point
my_slider.set(0)

my_label = customtkinter.CTkLabel(root, text=my_slider.get(), font=("Helvetica", 18))
my_label.pack(pady=20)


root.mainloop()

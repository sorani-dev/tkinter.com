from pathlib import Path
from tkinter import DISABLED, W, Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "OptionsMenu"
DIMENSIONS = "750x450"

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def color_picker(choice):
    """Selected color from my_option PptionMenu

    Arguments:
        choice -- Select item
    """
    my_label.configure(text=choice, text_color=choice)


def color_picker2():
    """Selected color from my_option PptionMenu"""
    my_label.configure(text=f"Clicked: {my_option.get()}", text_color=my_option.get())


def yellow():
    """Add a yellow color to the OptionMenu my_option"""
    my_option.set("Yellow")


# Set the options for the OptionsMenu
colors = [
    "Red",
    "Green",
    "Blue",
]

# Create OptionsMenu
my_option = customtkinter.CTkOptionMenu(
    root,
    values=colors,
    height=50,
    width=100,
    font=("Helvetica", 18),
    fg_color="white",
    dropdown_font=("Helvetica", 18),
    corner_radius=50,
    button_color="red",
    button_hover_color="green",
    dropdown_hover_color="green",
    dropdown_fg_color="blue",
    dropdown_text_color="orange",
    text_color="silver",
    hover=True,
    anchor="center",  # n-s-e-w-center
    state="normal",  # "normal" or disabled (default: "normal")
    dynamic_resizing=False,
    command=color_picker,
)
my_option.pack(pady=40)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

pick_button = customtkinter.CTkButton(root, text="Make Choice", command=color_picker2)
pick_button.pack(pady=10)

yellow_button = customtkinter.CTkButton(root, text="Pick Yellow", command=yellow)
yellow_button.pack(pady=10)

root.mainloop()

from pathlib import Path
from tkinter import DISABLED, END, W, Tk
import customtkinter

# Variables
# Mode of the appearance
mode = "dark"
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Light & Dark Modes"
DIMENSIONS = "750x525"

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "themes/red.json"
)  # Themes: blue (default), dark-blue, green

# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def change():
    """Change the appearance of the app"""
    global mode
    # Switch between Light and Dark with the opposite mode the app is in
    if mode == "light":
        mode = "dark"
    else:
        mode = "light"

    # Clear text box
    my_text.delete(0.0, END)
    my_text.insert(END, f"This is {mode.title()} Mode...")
    # Set appearance
    customtkinter.set_appearance_mode(mode)


def change_color(choice):
    # Need to reload the entire app to change the default color theme
    customtkinter.set_default_color_theme(choice)


my_text = customtkinter.CTkTextbox(master=root, width=600, height=300)
my_text.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Change Light/Dark Mode", command=change)
my_button.pack(pady=20)

colors = ["blue", "dark-blue", "green"]
my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_color)
my_option.pack(pady=10)

my_progress = customtkinter.CTkProgressBar(root, orientation="horizontal")
my_progress.pack(pady=20)

root.mainloop()

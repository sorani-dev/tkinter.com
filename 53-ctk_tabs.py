from pathlib import Path
from tkinter import Tk
import customtkinter

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Tabs"
DIMENSIONS = "700x300"


# Make app
root: Tk = customtkinter.CTk()

root.title(f"Custom Tkinter - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def clicker():
    """clicker Manage click on the Tabview tabs"""
    my_button.configure(text="You Clicked The Tab Button")


# Create Tabview
my_tab = customtkinter.CTkTabview(
    root,
    width=600,
    height=250,
    corner_radius=50,
    fg_color="silver",
    segmented_button_fg_color="red",
    segmented_button_selected_color="green",
    segmented_button_selected_hover_color="pink",
    segmented_button_unselected_hover_color="purple",
    segmented_button_unselected_color="yellow",
    text_color="red",
    state="normal",  # "normal" or "disabled" (default: "normal")
    command=clicker,
)
my_tab.pack(pady=10)

# Create Tabs
tab_1 = my_tab.add("Tab 1")
tab_2 = my_tab.add("Tab 2")

# Put stuff in tabs
my_button = customtkinter.CTkButton(tab_1, text="Click Me!")
my_button.pack(pady=40)


root.mainloop()

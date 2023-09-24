from pathlib import Path

import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Custom Tkinter!")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico").resolve())
root.geometry("600x350")


def hello():
    """hello Change the text of the label whenever the button is clicked"""
    my_label.configure(text=my_button.cget("text"))


# Custom Tkinter Button
my_button = customtkinter.CTkButton(
    root,
    text="Hello World!!!",
    command=hello,
    height=100,
    width=200,
    font=("Helvetica", 24),
    text_color="black",
    fg_color="green",
    hover_color="lightblue",
    corner_radius=50,
    bg_color="white",
    border_width=10,
    border_color="yellow",
    state="normal",
)
my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)

root.mainloop()

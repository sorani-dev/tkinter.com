from pathlib import Path

import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Combobox!")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico").resolve())
root.geometry("750x500")


def color_picker(choice):
    """color_picker Output color name and change text color based on the choice

    Arguments:
        choice: str -- Event of combobox which is the color chosen
    """
    output_label.configure(text=choice, text_color=choice)


def color_picker2():
    """
    Output color name and change text color based on the choice
    """
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


def color_pick_yellow():
    """
    Output color name and change text color based on the choice
    """
    # Set the combo box option
    my_combo.set("Yellow")
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


output_label = customtkinter.CTkLabel(root, text="Pick A Color", font=("Helvetica", 18))
output_label.pack(pady=40)

# b Set the options for the combobox
colors = ["Red", "Green", "Blue"]

my_combo = customtkinter.CTkComboBox(
    root,
    values=colors,
    height=50,
    width=200,
    font=("Helvetica", 18),
    dropdown_font=("Helvetica", 18),
    corner_radius=50,
    border_width=2,
    border_color="#949583",  # 949583
    button_color="#949583",
    button_hover_color="forestgreen",
    dropdown_hover_color="forestgreen",
    dropdown_fg_color="blue",
    dropdown_text_color="orange",
    text_color="silver",
    hover=True,
    justify="center",
    state="normal",  # normal or disabled
)
my_combo.pack(pady=20)


# Create a button
my_button = customtkinter.CTkButton(root, text="Pick A Color", command=color_picker2)
my_button.pack(pady=20)


my_button_yellow = customtkinter.CTkButton(
    root, text="Pick Yellow", command=color_pick_yellow
)
my_button_yellow.pack(pady=20)

# Create output label
output_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
output_label.pack(pady=20)

root.mainloop()

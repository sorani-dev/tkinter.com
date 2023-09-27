from pathlib import Path

import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Custom Tkinter Radio Buttons!")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico").resolve())
root.geometry("700x300")


def get_radio() -> None:
    """
    Change the Label output on radio button change
    """
    if radio_var.get() == "other":
        my_label_output.configure(text="Please make a selection.")
    elif radio_var.get().lower() == "yes":
        my_label_output.configure(text="Of course you like pizza!")
    else:
        my_label_output.configure(text="What's wrong with you?")


my_label = customtkinter.CTkLabel(
    root, text="Do You like Pizza?", font=("Helvetica", 18)
)
my_label.pack(pady=40)

# Variable to track the radio buttons value
radio_var = customtkinter.StringVar(value="other")

# Radio button 1: yes
my_radio_btn_1 = customtkinter.CTkRadioButton(
    root,
    text="Yes I do",
    value="yes",
    variable=radio_var,
    # width=50, # Width around the radio button including the text
    # height=50,# Height around the radio button including the text
    radiobutton_width=50,  # Width around the radio button
    radiobutton_height=50,  # Height around the radio button
    corner_radius=1,  # None: radio button shape is a circle (default); 1: radio button shape is a square
    border_width_unchecked=2,
    border_width_checked=5,
    border_color="aquamarine",
    hover_color="yellow",
    fg_color="forestgreen",  # Color when checkbox is clicked
    hover=True,  # Hover works: True, or not: False
    text_color="red",
    font=("Helvetica", 18),
    state="normal",  # normal, disabled
    text_color_disabled="grey",
)
my_radio_btn_1.pack(pady=10)

# Radio button 2: no
my_radio_btn_2 = customtkinter.CTkRadioButton(
    root,
    text="No I don't",
    value="no",
    variable=radio_var,
    # width=50, # Width around the radio button including the text
    # height=50,# Height around the radio button including the text
    radiobutton_width=50,  # Width around the radio button
    radiobutton_height=50,  # Height around the radio button
    corner_radius=1,  # None: radio button shape is a circle (default); 1: radio button shape is a square
    border_width_unchecked=2,
    border_width_checked=5,
    border_color="aquamarine",
    hover_color="yellow",
    fg_color="forestgreen",  # Color when checkbox is clicked
    hover=True,  # Hover works: True, or not: False
    text_color="red",
    font=("Helvetica", 18),
    state="disabled",  # normal, disabled
    text_color_disabled="grey",
)
my_radio_btn_2.pack(pady=10)

# Button
my_button = customtkinter.CTkButton(root, text="Select", command=get_radio)
my_button.pack(pady=10)

# Label foe output
my_label_output = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label_output.pack(pady=10)

root.mainloop()

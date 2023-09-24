from pathlib import Path
import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Custom Tkinter!")
root.iconbitmap(Path(__file__).parent.joinpath( "images", "codemy.ico").resolve())
root.geometry("600x350")

my_button = customtkinter.CTkButton(root, text="Hello World!!")
my_button.pack(pady=80)


root.mainloop()

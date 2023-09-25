from pathlib import Path

import customtkinter

# Set the theme and color options

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

# Make app
root = customtkinter.CTk()

root.title("Tkinter.com - Custom Tkinter ProgressBar!")
root.iconbitmap(Path(__file__).parent.joinpath("images", "codemy.ico").resolve())
root.geometry("700x2250")


def clicker():
    """
    Increment progressbar by 1
    """
    my_progressbar.step()
    my_label.configure(text=int(my_progressbar.get() * 100))


def start():
    """
    Start the Progressbar
    """
    my_progressbar.start()


def stop():
    """
    Stop the Progressbar
    """
    my_progressbar.stop()


my_progressbar = customtkinter.CTkProgressBar(
    root,
    orientation="horizontal",
    # mode="indeterminate",
    mode="determinate",  # determinate or indeterminate
    determinate_speed=0.8,
    # indeterminate_speed=0.5,
    width=300,
    height=50,
    corner_radius=50,
    border_width=2,
    border_color="#334488",
    fg_color="forestgreen",
    progress_color="pink",
)
my_progressbar.pack(pady=40)

# Set the default processbar starting point
my_progressbar.set(0)

my_button = customtkinter.CTkButton(root, text="Click Me", command=clicker)
my_button.pack(pady=10)


start_button = customtkinter.CTkButton(root, text="Start", command=start)
start_button.pack(pady=10)


stop_button = customtkinter.CTkButton(root, text="Stop", command=stop)
stop_button.pack(pady=10)


my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)

root.mainloop()

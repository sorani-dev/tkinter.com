from pathlib import Path
from tkinter import END, Button, Entry, Label, Tk, filedialog
import png
import pyqrcode
from PIL import Image,ImageTk

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "QR Code Generator"
DIMENSIONS = "500x550"

# Make app
root: Tk = Tk()
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def create_code() -> None:
    """
    Genarate and save a QR Code
    """
    # File Dialog where QR code should be saved
    input_path = filedialog.asksaveasfilename(
        title="Save Image", filetypes=(("PNG File", "*.png"), ("All Files", "*.*"))
    )

    if input_path:
        if not input_path.endswith(".png"):
            # Add .png extension to the end of the file name
            input_path = f"{input_path}.png"

        # Create QR Code
        generated_code: pyqrcode.QRCode = pyqrcode.create(my_entry.get())
        # Save as PNG file
        generated_code.png(input_path, scale=5)

        # Put QR code to the screen
        global qr_image
        qr_image = ImageTk.PhotoImage(image=Image.open(input_path))
        # Add image to label
        my_label.config(image=qr_image)
        # Delet eentry box
        my_entry.delete(0, END)
        # Flash up finished QR Code generation message
        my_entry.insert(0, "Finished!")


def clear_all() -> None:
    """
    Clear all output of QR code
    """
    my_entry.delete(0, END)
    my_label.config(image="")



# Create GUI
my_entry = Entry(master=root, font=("Helvetica", 18))
my_entry.pack(pady=20)

create_code_button = Button(master=root, text="Create QR Code", command=create_code)
create_code_button.pack(pady=20)

clear_button = Button(master=root, text="Clear", command=clear_all)
clear_button.pack(pady=20)

my_label = Label(master=root, text="")
my_label.pack(pady=20)


root.mainloop()

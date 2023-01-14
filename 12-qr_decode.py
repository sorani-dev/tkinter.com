from pathlib import Path
from tkinter import END, Button, Entry, Label, Tk, filedialog
import png
import pyqrcode
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "QR Code Generator and Decoder"
DIMENSIONS = "500x550"

# Make app
root: Tk = Tk()
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def show(input_path: str) -> None:
    """
    Show the input image to the screen and add a finished message
    Args:
        input_path (str): Path of the image to display
    """

    # Put QR code to the screen
    global qr_image
    qr_image = ImageTk.PhotoImage(image=Image.open(input_path))
    # Add image to label
    my_label.config(image=qr_image)
    # Delete entry box
    my_entry.delete(0, END)
    # Flash up finished QR Code generation message
    my_entry.insert(0, "Finished!")


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
        show(input_path=input_path)


def clear_all() -> None:
    """
    Clear all output of QR code
    """
    my_entry.delete(0, END)
    my_label.config(image="")
    result_label.config(text="")


def decode_it() -> None:
    """
    Decode an inputted QR Code image
    and display the decoded results on the screen
    """
    # Open a QR Code image
    input_path: str = filedialog.askopenfilename(
        title="Open Image", filetypes=(("PNG File", "*.png"), ("All Files", "*.*"))
    )

    if input_path:
        # Decode QR Code
        decode_QR = decode(Image.open(input_path))
        print(decode_QR)
        # Show on screen
        result_label.config(text=f"QR Decoded: {decode_QR[0].data.decode('ascii')}")

        show(input_path=input_path)


# Create GUI

# QR Code Encoding
my_entry = Entry(master=root, font=("Helvetica", 18))
my_entry.pack(pady=20)

create_code_button = Button(master=root, text="Create QR Code", command=create_code)
create_code_button.pack(pady=20)

clear_button = Button(master=root, text="Clear", command=clear_all)
clear_button.pack(pady=20)

my_label = Label(master=root, text="")
my_label.pack(pady=20)

# QR Code Decoding
result_label = Label(master=root, text="")
result_label.pack(pady=20)

result_button = Button(master=root, text="Decode QR Code", command=decode_it)
result_button.pack(pady=20)

root.mainloop()

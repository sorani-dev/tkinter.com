from pathlib import Path
from tkinter import Button, Label, PhotoImage, Tk, filedialog

from fpdf import FPDF
from PIL import Image, ImageTk

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Save Image as PDF"
DIMENSIONS = "600x600"

IMAGE_SIZE = 500

# Make app
root: Tk = Tk()
root.title(f"{TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def open_image() -> None:
    """
    Open and Image file
    """
    global get_image, image_path

    # Open file
    input_path = filedialog.askopenfilename(
        title="Open Image", filetypes=(("PNG", "*.png"), ("All Files", "*.*"))
    )

    # Set file path global to use it later
    image_path = input_path

    if input_path:
        if not input_path.endswith(".png"):
            #  Add png extension to input path
            input_path = f"{input_path}.png"

        #  Get the selected image
        image = Image.open(input_path)
        # Resize image so everithing show on screen
        image.thumbnail((IMAGE_SIZE, IMAGE_SIZE), resample=Image.Resampling.LANCZOS)
        get_image = ImageTk.PhotoImage(image=image)
        #  Add Image to label
        my_label.config(image=get_image)


def saver() -> None:
    """
    Save image as PDF File
    """
    # Open a file dialog to save to PDF
    output_path:str = filedialog.asksaveasfilename(
        title="Save as PDF", filetypes=(("PDF", "*.pdf"), ("All Files", "*.*"))
    )

    if output_path:
        if not output_path.endswith(".pdf"):
            # Add PDF extension
            output_path += ".pdf"
        
        # Create FPF instance
        pdf:FPDF = FPDF()
        # Create a PDF page
        pdf.add_page()
        # Add Image to page
        pdf.image(image_path)
        # pdf.image(image_path, x=50, y=50, w=50, h=50)
        # Save pdf
        pdf.output(output_path, "F")

        # Update label
        my_label.config(image="", text="DONE!")   



# GUI: Create Widgets
my_label = Label(root, text="Open Image", font=("Helvetica", 28))
my_label.pack(pady=50)

open_button = Button(master=root, text="Open Image", command=open_image)
open_button.pack(pady=10)

save_button = Button(master=root, text="save to PDF", command=saver)
save_button.pack()


root.mainloop()

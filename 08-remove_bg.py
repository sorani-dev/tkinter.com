from pathlib import Path
from tkinter import Button, Label, Tk, filedialog
from PIL import Image, ImageTk
from rembg import remove

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Remove Image Background"
DIMENSIONS = "500x700"


class RemoveBackground:
    ROOT_PATH = Path(__file__).parent.resolve()
    FILE_TYPES = (
        ("PNG File", "*.png"),
        ("Jpeg File", "*.jpg, *.jpeg"),
        ("All Files", "*.*"),
    )

    def __init__(self, master: Tk) -> None:
        super().__init__()
        self.master: Tk = master
        self.input_path:str = ""
        self.my_image:ImageTk.PhotoImage

        # Create GUI
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create and display widgets
        """
        # GUI
        self.pic_label = Label(self.master, text="")
        self.pic_label.pack(pady=20)

        self.open_button = Button(
            self.master, text="Open Image", command=self.open_image_file
        )
        self.open_button.pack(pady=20)

        self.remove_button = Button(
            self.master, text="Remove Background", command=self.remove_background
        )
        self.remove_button.pack(pady=20)

    def run(self) -> None:
        """
        Run the app
        """
        self.master.mainloop()

    def open_image_file(self) -> None:
        """
        Open an image file
        """
        self.input_path = filedialog.askopenfilename(
            title="Open Image", filetypes=self.FILE_TYPES, initialdir=BASE_PATH
        )
        if self.input_path:
            self.my_image = ImageTk.PhotoImage(image=Image.open(self.input_path))
            self.pic_label.config(image=self.my_image, bg="black")

    def remove_background(self) -> None:
        """
        Remove background from an image file
        """
        # Get file path to save file
        output_file = filedialog.asksaveasfilename(
            title="Save As...", filetypes=self.FILE_TYPES
        )

        # Get file name
        input_name = Image.open(self.input_path)
        # Remove the background
        output:Image.Image = remove(input_name)
        print(type(output))
        
        # Sasve the file
        output.save(output_file, 'png')

        # Put new image on the screen
        self.my_image = ImageTk.PhotoImage(image=Image.open(output_file))

        # Update label
        self.pic_label.config(image=self.my_image)



def main() -> None:
    # Make app
    root: Tk = Tk()
    root.title(f"Simon Cateau Tkinter - {TITLE}")
    root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
    root.geometry(DIMENSIONS)
    app = RemoveBackground(master=root)
    app.run()


if __name__ == "__main__":
    main()

from pathlib import Path
from tkinter import Tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# Variables
# Global Constants
BASE_PATH: Path = Path(__file__).parent.resolve()
TITLE: str = "Floodgauge"
DIMENSIONS = "500x550"

# Make app
root: Tk = tb.Window(themename="superhero")
root.title(f"TTk Bootstrap - {TITLE}")
root.iconbitmap(Path(BASE_PATH, "images", "codemy.ico").resolve())
root.geometry(DIMENSIONS)


def starter():
    """Start the gauge
    """
    my_gauge.start()

def stopper():
    """Stop the gauge
    """
    my_gauge.stop()

def incrementer():
    """Increment the gauge
    """
    my_gauge.step(10)
    
    # Update the label each time the position changes
    my_label.config(text=f"Position: {my_gauge.variable.get()}")

# Floodgauge
my_gauge = tb.Floodgauge(root, bootstyle="success", 
                        font=("Helvatica", 18),
                        mask="Pos: {}%", # To keep track of what it's doing
                        maximum=80, # Maximun value of the widget
                        orient="horizontal", # Orientation: default: "horizontal", other value: "vertical"
                        value=0, # The current value of the progressbar; default: 0
                        mode=DETERMINATE,# DETERMINATE (keep on going) or INDETERMINATE (pings back and fourth between start and finish); default DETERMINATE
                        )
my_gauge.pack(pady=50, fill=X, padx=20)



# Buttons to manage my_gauge

start_button = tb.Button(root,  text="Start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)


stop_button = tb.Button(root,  text="Stop", bootstyle="danger outline", command=stopper)
stop_button.pack(pady=20)


inc_button = tb.Button(root,  text="Increment", bootstyle="danger outline", command=incrementer)
inc_button.pack(pady=20)

# Label
my_label = tb.Label(root, text="Position: ")
my_label.pack(pady=20)







root.mainloop()

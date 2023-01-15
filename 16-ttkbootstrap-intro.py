import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import LEFT

root = tk.Tk()

b1 = ttkb.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttkb.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
from tkinter import *

root = Tk()
root.geometry('500x350')


def clicker():
    button.config(text="You Clicked the Button!")
    button.config(state="disabled")
    button.config(state="normal")
    button.config(width=15)


# Define an Image
login = PhotoImage(file='images/login.png')

button = Button(master=root, text="Click Me",
                activebackground="black",
                activeforeground="red",
                anchor="center",
                bg="SystemButtonFace",
                bd="20",
                command=clicker,
                default="disabled",
                disabledforeground="green",
                font=("Helvetica", 20),
                fg="blue",
                # height="50",
                highlightbackground="blue",
                # highlightthickness="",
                highlightcolor="green",
                # image="",
                justify="center",
                overrelief="raised",
                relief="raised",
                state="active",
                takefocus=TRUE,
                underline=0,
                width=40,
                wraplength=100 # Number of characters before wrapping line
                )
button.pack()

button2 = Button(master=root, text="Click Me",
                activebackground="black",
                activeforeground="red",
                anchor="center",
                bg="SystemButtonFace",
                bd="0",
                command=clicker,
                default="disabled",
                disabledforeground="green",
                font=("Helvetica", 32),
                fg="blue",
                # height="50",
                highlightbackground="blue",
                # highlightthickness="",
                highlightcolor="green",
                image=login,
                # justify="",
                # overrelief="",
                # relief="",
                state="active",
                # takefocus=""

                )
button2.pack(pady=20)

root.mainloop()

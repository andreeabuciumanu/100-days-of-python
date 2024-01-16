# import tkinter
from tkinter import *
# import turtle

# Create a window
window = Tk()
window.title("My First GUI Project")
window.minsize(width=500, height=300)
# add space around the widgets
window.config(padx=10, pady=10)

# Create a label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label["text"] = "New text"
my_label.grid(column=0, row=0)


def button_clicked():
     my_label["text"] = input.get()


# Create a button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


# Create an input
input = Entry(width=10)
user_text = str(input.get())
input.grid(column=3, row=2)

# New button
my_button = Button(text="I' a new button")
my_button.grid(column=3, row=0)

# tim = turtle.Turtle()
# tim.write("this is a text")

window.mainloop()

import tkinter
# import turtle

window = tkinter.Tk()
window.title("My First GUI Project")
window.minsize(width=500, height=300)

# Create a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack(side="left")


# tim = turtle.Turtle()
# tim.write("this is a text")

window.mainloop()

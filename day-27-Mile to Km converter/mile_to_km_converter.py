from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    converted_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to km converter")
window.minsize(width=600, height=300)
window.config(pady=150, padx=180)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

is_equal_to_label = Label(text="is equal to", font=("Arial", 10))
is_equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

converted_result_label = Label(text="0")
converted_result_label.grid(column=1, row=1)



window.mainloop()
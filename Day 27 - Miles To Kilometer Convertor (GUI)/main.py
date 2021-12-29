from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# no define will auto fit all the widgets in window
# window.minsize(250, 100)
window.config(padx = 50)

equal = Label(text = "is equal to")
equal.grid(row = 1, column = 0)

input = Entry(width = 10)
input.grid(row= 0, column = 1)
input.insert(0, "0")

zero = 0
output = Label(text= zero)
output.grid(row=1, column=1)

km_unit = Label(text = "Km")
km_unit.grid(row = 1, column = 2)

miles_unit = Label(text = "Miles")
miles_unit.grid(row = 0, column = 2)

def calculate():
    input_value = float(input.get())
    output_value = input_value * 1.60934
    output = Label(text = output_value)
    output.grid(row = 1, column = 1)


button = Button(width = 8, text = "Calculate", command = calculate)
button.grid(row = 2, column = 1)


window.mainloop()



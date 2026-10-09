from tkinter import *

def convert():
    m = int(input_entry.get())
    km = round(m*1.60934)
    label_output.config( text=f"{km}")
    return km

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(200, 100)

label_miles = Label(text="miles")
label_miles.grid(column=2, row=0)

input_entry = Entry()
input_entry.grid(column=1, row=0)

label_equal = Label(text="is equals to")
label_equal.grid(column=0, row=1)

label_output = Label(text=0)
label_output.grid(column=1, row=1)

label_km = Label(text="kilometers")
label_km.grid(column=2, row=1)

calculate_button = Button(text="Calculate",command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
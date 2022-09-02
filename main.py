from tkinter import *


def button_clicked():
    nr_miles = int(input_val.get())
    nr_km = "{:.2f}".format(nr_miles * 1.609)
    label_km_calculated = Label(text=str(nr_km))
    label_km_calculated.grid(row=1, column=1)


# Window

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

# Entry

input_val = Entry()
input_val.config(width=10)
input_val.grid(row=0, column=1)

# Labels

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_eq = Label(text="is equal to")
label_is_eq.grid(row=1, column=0)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

# Button

button = Button(text="Calculate")
button.grid(row=2, column=1)
button.config(command=button_clicked)

window.mainloop()

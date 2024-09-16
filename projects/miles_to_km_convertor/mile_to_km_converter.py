from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=100, pady=100)

window.minsize(width=500, height=500)


def action():
    mile_val = float(mile_input.get())
    res = mile_val * 1.609344
    output.config(text=f"{res}")


mile_input = Entry(width=30)
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=action)
calculate.grid(column=1, row=2)

window.mainloop()

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result.config(text=km)


window = Tk()
window.title("My First GUI Prog")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)
print(miles_input.get())

miles_label = Label(text="miles", font=("Arial", 14))
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to:", font=("Arial", 14))
is_equal_label.grid(row=1, column=0)

km_label = Label(text="km", font=("Arial", 14))
km_label.grid(row=1, column=2)

result = Label(text="0", font=("Arial", 14))
result.grid(row=1, column=1)

calc_button = Button(text="Calculate", command=miles_to_km, font=("Arial", 14))
calc_button.grid(row=2, column=1)

window.mainloop()

from tkinter import *


def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Prog")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

my_label = Label(text="I am a label", font=("Arial", 14, "bold"))
my_label.grid(row=0, column=0)
my_label.config(pady=20, padx=20)


button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New button", command=button_clicked)
new_button.grid(row=0, column=2)

user_input = Entry(width=15)
user_input.grid(row=2, column=3)
print(user_input.get())

window.mainloop()

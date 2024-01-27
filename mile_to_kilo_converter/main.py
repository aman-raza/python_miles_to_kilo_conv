from tkinter import *

# Creating a window
window = Tk()
window.title("mile to kilo converter")
window.config(padx=20, pady=20)


def miles_to_kilo():
    miles = miles_input.get()
    km = float(miles) * 1.609
    kilo_result_label.config(text=f"{km}")


miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="KM")
kilo_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilo)
calculate_button.grid(column=1, row=2)

window.mainloop()

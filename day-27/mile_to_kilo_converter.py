from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,  row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()

# window = Tk()
# window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
# converted = 0
#
#
# my_label = Label(text=f"is equal to {converted} miles",font=("Arial", 24, "bold"))
# my_label.grid(column=0, row = 1)
# input = Entry(width=10)
# input.grid(column=1,row=0)
#
# def button_clicked():
#     input_value = input.get()
#     to_miles = float(input_value)*1.6
#     my_label.config(text=f"is equal to {to_miles} miles")
#
#
# button = Button(text="Calculate", command=button_clicked)
# button.grid(column=1,row=2)
#
# window.mainloop()

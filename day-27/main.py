from tkinter import *
from playground import add

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I Am a Label",font=("Arial", 24, "bold"))
my_label.pack()

print(add(1,2,3,4,5,6))

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0,row=0)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Button

button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

button = Button(text="Click me", command=button_clicked)
button.grid(column=0,row=2)# button.pack()
#Entry
input = Entry(width=10)
input.grid(column=3,row=3)
# input.pack()
print(input.get())




window.mainloop()

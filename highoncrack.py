from tkinter import *

window = Tk()

foods = ["Pizza", "Hamburger", "Hotdog", "Pasta", "Soup", "Salad"]

window.title("fav food")
x = IntVar()

try:
    for i in range(len(foods)):
        radiobutton = Radiobutton(window, text = foods[i] , variable = x , value = i)
        radiobutton.pack(anchor=W)
except Exception as e:
    print("error")

window.geometry("400x400")

window.mainloop()
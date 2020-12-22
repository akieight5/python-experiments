'''
Created on 22 Nov 2020

@author: aki
'''

import tkinter as tk
from bokeh.layouts import column

def button_click(number):
    current = e.get()
    e.delete(0, "end")
    e.insert(0, str(current) + str(number))
    
def button_add():
    global func, f_num
    first_number=e.get()
    func = "add"
    f_num = int(first_number)
    e.delete(0, "end")
    
def button_subtract():
    global func, f_num
    first_number=e.get()
    func = "subtract"
    f_num = int(first_number)
    e.delete(0, "end")

def button_multiply():
    global func, f_num
    first_number=e.get()
    func = "multiply"
    f_num = int(first_number)
    e.delete(0, "end")

def button_divide():
    global func, f_num
    first_number=e.get()
    func = "divide"
    f_num = int(first_number)
    e.delete(0, "end")

def button_equal():
    second_number=e.get()
    e.delete(0, "end")
    if func == "add":
        e.insert(0, f_num + int(second_number))
    elif func =="subtract":
        e.insert(0, f_num - int(second_number))
    elif func =="multiply":
        e.insert(0, f_num * int(second_number))
    else:
        e.insert(0, int(f_num / int(second_number)))
    
def button_clear():
    e.delete(0, "end")

root = tk.Tk()
root.title("calculator")

# user entry window
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# button definition

b1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
b2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
b3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
b4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
b5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
b6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
b7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
b8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
b9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
b0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
clear = tk.Button(root, text="Clear", padx=75, pady=20, command= button_clear)
add = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
subtract = tk.Button(root, text="-", padx=40, pady=20, command=button_subtract)
multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
divide = tk.Button(root, text="/", padx=40, pady=20, command=button_divide)
equal = tk.Button(root, text="=", padx=75, pady=20, command=button_equal)

# button positioning

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b0.grid(row=4, column=0)
clear.grid(row=4, column=1, columnspan=2)

add.grid(row=5, column=0)
subtract.grid(row=5, column=1)
multiply.grid(row=5, column=2)

divide.grid(row=6, column=0)
equal.grid(row=6, column=1, columnspan=2)

root.mainloop()  # Keep the window open
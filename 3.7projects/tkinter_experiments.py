'''
Created on 15 Oct 2020

@author: aki
'''

def my_upd():
    #my_w.destroy()
    myLabel = tk.Label(my_w, text="I clicked a button")
    myLabel.grid(row = 3, column=3)
    
def userEntry():
    userInfo = tk.Label(my_w, text="Hello " + uE.get())
    userInfo.grid(row=8, column=3)

import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_font=('times', 8, 'bold')

b1 = tk.Button(my_w, text='Hi  Welcome', width=20,bg='yellow',font=my_font,fg='green', command=my_upd)
b1.grid(row=2,column=2)
b2 = tk.Button(my_w, text="I am enabled", width=20, bg="blue", font=my_font, fg="white", command=lambda: my_upd())
b2.grid(row=5, column=3)
b3 = tk.Button(my_w, text="Enter your name", command=userEntry)
b3.grid(row=6, column=0)
uE = tk.Entry(my_w, width=50)
uE.grid(row=7, column=1)


"""
for i in range(5):
    myLabel = tk.Label(my_w, text=i)
    myLabel2 = tk.Label(my_w, text="hello world")
    myLabel.pack()
    myLabel2.pack()
"""
my_w.mainloop()  # Keep the window open
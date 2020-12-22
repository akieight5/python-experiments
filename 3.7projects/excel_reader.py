'''
Created on 6 Oct 2020

@author: aki
'''

import pandas as pd
#import numpy as np
import tkinter as tk

#lambda function
def func(disp, c):
    button_func = tk.Label(text=disp)
    info = c.grid_info()
    print(info["row"], info["column"])
    button_func.grid(row=(info["row"])+1, column=info["column"], pady=2)


df_excel = pd.read_excel("//home//aki//Documents//example_spreadsheet.xlsx")

cols = df_excel.columns.ravel()
#print(cols)

top = tk.Tk()
#widgets go here

#excel_headers = tk.Label(text = cols)
#excel_headers.pack()

for a in range(1):
    for b in range(len(cols)):
        c = tk.Button(text=cols[b], bg="blue", fg="yellow", command=lambda x=cols[b]: func(x))
        c.grid(row=a, column=b, pady=2)


#this line included to ensure the Tkinter app runs
top.mainloop()
'''
Created on 25 Nov 2020

@author: aki
'''
"""
import tkinter as tk

root = tk.Tk()
root.title("image demonstration")

#iconbitmap only works with black and white images
# root.iconbitmap("/home/aki/Downloads/icons/antenna.xbm")

img = tk.PhotoImage(file='/home/aki/Downloads/icons/antenna.png')
root.tk.call('wm', 'iconphoto', root._w, img)
"""
"""
This is an old question, and there is lots of stuff written about it on the web, 
but all of it is either incorrect or incomplete, so having gotten it to work I 
thought it would be good to record my actual working code here.

First, you'll need to create an icon and save it in two formats: Windows "ico" 
and Unix "xbm". 64 x 64 is a good size. XBM is a 1-bit format--pixels just on or 
off, so no colors, no grays. Linux implementations of tkinter only accept XBM 
even though every Linux desktop supports real icons, so you're just out of luck 
there. Also, the XBM spec is ambiguous about whether "on" bits represent black or 
white, so you may have to invert the XBM for some desktops. Gimp is good for creating these.

Then to put the icon in your titlebar, use this code (Python 3):
"""
#"""
import os, sys
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("My Application")
if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "myicon.ico")
else:
    root.wm_iconbitmap(bitmap = "/home/aki/Downloads/icons/antenna.xbm")

root.mainloop()
#"""
"""
#something else to try
import sys, os
from tkinter import *
root = Tk()
root.title("My Application")
program_directory="/home/aki/Downloads/icons"
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "antenna.png")))
"""


root.mainloop()
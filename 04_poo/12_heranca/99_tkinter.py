#! python3.11

from tkinter import *

"""
    Código da wikipédia
    
    https://en.wikipedia.org/wiki/Tkinter#:~:text=It%20is%20the%20standard%20Python,and%20macOS%20installs%20of%20Python.
"""

root = Tk() 							# Create the root (base) window 
w = Label(root, text="Hello, world!") 	# Create a label with words
w.pack() 								# Put the label into the window
root.mainloop() 
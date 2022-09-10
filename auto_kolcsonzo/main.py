from tkinter import *
import sqlite3

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()

        self.title("Pycar kolcsonzo")
        self.minsize(500,400)

root = Root()
root.mainloop()
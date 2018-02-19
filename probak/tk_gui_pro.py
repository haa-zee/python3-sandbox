#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
#from tkinter.ttk import Frame, Button

class Application:

    def __init__(self, p_root):
        self.root_window = p_root
        self.initUI()

    def initUI(self):
        self.fr = Frame(self.root_window, height=600, width=800 )
        self.fr.grid(padx=10, pady=10)
        self.b1 = Button(self.fr, text="Exit")
        self.b1.grid(column=5, row=0)
        self.b2 = Button(self.fr, text="Start")
        self.b2.grid(column=0, row=0)
        self.canv = Canvas(self.fr, width=800, height=600, borderwidth=5, bg="#ffffe0")
        self.canv.grid(column=0, row=2)


if __name__ == "__main__":
    root = Tk()
    app=Application(root)
    root.mainloop()
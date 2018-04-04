#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tkinter-t használó alkalmazás, tanulási céllal"""

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.parent_window = root
        self.label = None
        self.setup_ui()

    def setup_ui(self):
        self.config(padx=4, pady=5, relief=tk.GROOVE)
        self.grid(ipadx=3, ipady=3)
        self.label = tk.Label(text="App Címke", background="green", foreground="blue")
        self.label.grid(row=1, column=2, columnspan=3)
        tk.Label(text="Left>>").grid(row=2, column=1)
        self.b1 = tk.Button(text="Press Me!")
        self.b1.grid(row=2, column=2)


if __name__ == "__main__":
    rootWindow = tk.Tk()
    rootWindow.geometry("800x600")
    app = Application(rootWindow)
    rootWindow.mainloop()

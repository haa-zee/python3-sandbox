#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class Osztaly:
	
	def __init__(self,root):
		frame=tk.Frame(root)
		frame.pack()
		self.button=tk.Button(frame, text="Quit", command=frame.quit)
		self.button.pack(side=tk.LEFT)
		
		self.hi_there=tk.Button(frame, text="HELLO!", command=self.metodus)
		self.hi_there.pack(side=tk.LEFT)
		
		
	def metodus(self):
		print("Hello world!")
		
if __name__=="__main__":
	root=tk.Tk()
	o=Osztaly(root)
	root.mainloop()
	root.destroy()
	

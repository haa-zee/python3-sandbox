#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from random import randint
import time

def start():
	top=tk.Tk()	# root window
	
	canvas=tk.Canvas(top, width=1000, height=800)
	canvas.pack()
	print("Started")
	time.sleep(2)
	canvas.create_line(0,400,1,700)
	time.sleep(2)
	canvas.create_line(1,700,2,200)
	time.sleep(2)
	canvas.create_line(2,200,5,500)
	canvas.pack()
	top.mainloop()
	
	

if __name__ == "__main__":
	start()
	

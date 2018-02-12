#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from random import randint
import time

def start():
	top=tk.Tk()	# root window
	
	canvas=tk.Canvas(top, width=1000, height=800)
	canvas.pack()
	top.update()
	print("Started")
	time.sleep(2)
	canvas.create_line(0,400,10,700,width=4,fill="#0000ff")
	canvas.update()
	time.sleep(2)
	canvas.create_line(10,700,20,200,width=4,fill="#00ff00")
	canvas.update()
	time.sleep(2)
	canvas.create_line(20,200,50,500,width=4,fill="#ff0000")
	canvas.update()
	top.mainloop()
	
	

if __name__ == "__main__":
	start()
	

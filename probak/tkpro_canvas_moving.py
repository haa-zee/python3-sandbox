#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from random import randint
import time


		
		
		

def start(top):
	
	a=[ randint(0,800) for n in range(100) ]
	
	canvas=tk.Canvas(top, width=1000, height=800, xscrollincrement=1)
	canvas.pack()
	top.update()
	print("Started")

	prev=400
	for j in range(100):
		canvas.delete("all")
		for i in range(0,99):
			s=i*10
			e=s+9
			canvas.create_line(s,prev,e,a[i],width=3)
			prev=a[i]

		canvas.update()
		a.pop(0)
		a.append(randint(0,800))
		
		for i in range(10):
			canvas.move("all",-1,0)
			canvas.update()
			time.sleep(.01)

if __name__ == "__main__":
	top=tk.Tk()
	start(top)
	top.mainloop()
	

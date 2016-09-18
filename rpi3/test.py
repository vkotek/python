#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 23:20:25 2016

@author: prometheus
"""
res = "320x240"

from tkinter import *

class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        print("Initialized window")
    
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label="exit", command=self.client_exit)
        menu.add_cascade(label="file", menu=file)
        
        quitButton = Button(self, text = "Quit", command=self.client_exit)
        quitButton.place(x=260,y=200)
        
        toggleButton = Button(self, text = "DO", command=self.client_toggle)
        toggleButton.place(x=20,y=20)
    
    def client_exit(self):
        print("Exiting")
        exit()
    
    def client_toggle(self):
        print("Toggle but exit")
        

root = Tk()
w = Label(root, text="MyScript")
root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.geometry(res.format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()

app = Window(root)

root.mainloop()


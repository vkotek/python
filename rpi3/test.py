# -*- coding: utf-8 -*-

res = "320x480"

from tkinter import *
import time

class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.state = 0
        print(format(time.ctime()))
    
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        #file = Menu(menu)
        #file.add_command(label="exit", command=self.client_exit)
        #menu.add_cascade(label="file", menu=file)
        
        self.quitButton = Button(self, text = "Quit", padx="20", command=self.client_exit)
        self.quitButton.config(bg='blue')
        self.quitButton.place(x=400,y=280)
        
        self.toggleButton = Button(self, text = "ON", padx="20", command=self.client_toggle)
        self.toggleButton.place(x=20,y=20)
        
    def client_exit(self):
        print("Exiting")
        exit()
    
    def client_toggle(self):
        print("Toggle but exit")
        if self.state == 0:
            self.toggleButton.config(text="OFF")
            self.state = 1
        else:
            self.toggleButton.config(text="ON")
            self.state = 0
        

root = Tk()
#w = Label(root, text="MyScript")
root.configure(bg='gray')
root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.geometry("480x320")
root.focus_set()

app = Window(root)
root.mainloop()


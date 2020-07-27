#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import RubicsCubeOOP as rc
import os, json

class Pencere(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Window Options
        self.title("cacaleno/Rubik's Cube")
        self.wm_resizable(0,0)
        #Logic
        self.surface = 0
        self.save = None
        #Menubar
        self.menubar =tk.Menu()
        self.cubemenu = tk.Menu(self.menubar)
        self.cubemenu.add_command(label="New", command=self.new_file)
        self.cubemenu.add_command(label="Save", command=self.save_current_file)
        self.cubemenu.add_command(label="Save as", command=self.save_as_file)
        self.cubemenu.add_command(label="Load", command=self.load_file)
        self.cubemenu.add_separator()
        self.cubemenu.add_command(label="Settings", command=self.Settings)
        self.cubemenu.add_separator()
        self.cubemenu.add_command(label="Exit", command = self.quit)
        self.menubar.add_cascade(menu=self.cubemenu, label="Cube")
        self.helpmenu = tk.Menu(self.menubar)
        self.helpmenu.add_command(label="About")
        self.helpmenu.add_command(label="Document")
        self.helpmenu.add_command(label="Contact")
        self.menubar.add_cascade(menu=self.helpmenu, label="Help")
        self.config(menu=self.menubar)        
        #Frames
        self.buttonframe = ttk.Frame(self, padding=(34,10,36,10), relief="groove")
        self.buttonframe.pack()
        self.surfaceframe= tk.Frame(self)
        self.surfaceframe.pack()
        self.totalframe = tk.Frame(self)
        self.totalframe.pack()
        #ButtonFrame Buttons
        self.button1 = ttk.Button(self.buttonframe, text="FRONT", command=lambda :self.surface_select(0))
        self.button1.grid(column=0, row=1)
        self.button2 = ttk.Button(self.buttonframe, text="RIGHT", command=lambda :self.surface_select(1))
        self.button2.grid(column=1, row=1)
        self.button3 = ttk.Button(self.buttonframe, text="BEHIND", command=lambda :self.surface_select(2))
        self.button3.grid(column=2, row=1)
        self.button4 = ttk.Button(self.buttonframe, text="LEFT", command=lambda :self.surface_select(3))
        self.button4.grid(column=3, row=1)
        self.button5 = ttk.Button(self.buttonframe, text="TOP", command=lambda :self.surface_select(4))
        self.button5.grid(column=4, row=1)
        self.button6 = ttk.Button(self.buttonframe, text="BOTTOM", command=lambda :self.surface_select(5))
        self.button6.grid(column=5, row=1)
        self.reset = ttk.Button(self.buttonframe, text="RESET", command=lambda :self.resetter())
        self.reset.grid(column=0, row=2)
        self.mixbutton = ttk.Button(self.buttonframe, text="MIX", command=lambda :self.mixer())
        self.mixbutton.grid(column=1, row=2)
        #SurfaceFrame Button Pics
        self.left = tk.PhotoImage(file=os.getcwd()+"/buttons/left.png")
        self.right = tk.PhotoImage(file=os.getcwd()+"/buttons/right.png")
        self.up = tk.PhotoImage(file=os.getcwd()+"/buttons/up.png")
        self.down = tk.PhotoImage(file=os.getcwd()+"/buttons/down.png")
        #SurfaceFrame
        self.canvasframe = tk.Frame(self.surfaceframe)
        self.canvasframe.grid(row = 2, column = 2)
        self.verticalframe = tk.Frame(self.surfaceframe)
        self.verticalframe.grid(row = 1, column = 2)
        self.leftframe = tk.Frame(self.surfaceframe)
        self.leftframe.grid(row = 2, column= 1)
        self.rightframe = tk.Frame(self.surfaceframe)
        self.rightframe.grid(row = 2, column = 3)
        self.bottomframe = tk.Frame(self.surfaceframe)
        self.bottomframe.grid(row = 3, column = 2)
        self.button1 = tk.Button(self.verticalframe, image=self.up, command=lambda : self.vertical_call(0, -1))
        self.button1.grid(row = 0, column = 0)
        self.button2 = tk.Button(self.verticalframe, image=self.up, command=lambda : self.vertical_call(2, -1))
        self.button2.grid(row= 0, column = 2)
        self.label1 = tk.Label(self.verticalframe)
        self.label1.grid(row= 0, column = 1, padx = 40)
        self.button3 = tk.Button(self.leftframe, image=self.left, command=lambda: self.horizontal_call(0, -1) )
        self.button3.grid(row = 1)
        self.label2 = tk.Label(self.leftframe)
        self.label2.grid(pady = 40, row = 2)
        self.button4 = tk.Button(self.leftframe, image=self.left, command=lambda: self.horizontal_call(2, -1))
        self.button4.grid(row = 3)
        self.button5 = tk.Button(self.rightframe, image=self.right, command=lambda: self.horizontal_call(0, 1))
        self.button5.grid()
        self.label3 = tk.Label(self.rightframe)
        self.label3.grid(pady = 40)
        self.button6 = tk.Button(self.rightframe, image=self.right, command=lambda: self.horizontal_call(2, 1))
        self.button6.grid()
        self.button7 = tk.Button(self.bottomframe, image = self.down, command=lambda : self.vertical_call(0, 1))
        self.button7.grid(row = 0, column = 0)
        self.label4 = tk.Label(self.bottomframe)
        self.label4.grid(padx = 40, row = 0, column = 1)
        self.button8 = tk.Button(self.bottomframe, image = self.down, command=lambda : self.vertical_call(2, 1) )
        self.button8.grid(row = 0, column = 2)
        self.canvas = tk.Canvas(self.canvasframe, height=250, width=250)
        self.canvas.pack()
        self.rectangles = []
        for row in range(3):
            self.rectangles.append([])
            for column in range(3) :
                self.rectangle = self.canvas.create_rectangle(5+80*column, 5+80*row, 85+80*column, 85+80*row, fill=cube.Rubiks_Cube[self.surface][row][column])
                self.rectangles[row].append(self.rectangle)
        #TotalFrame
        self.surface1 = tk.Frame(self.totalframe)
        self.surface1.grid(row = 1, column = 1)
        self.surface2 = tk.Frame(self.totalframe)
        self.surface2.grid(row = 1, column = 2)
        self.surface3 = tk.Frame(self.totalframe)
        self.surface3.grid(row = 1, column = 3)
        self.surface4 = tk.Frame(self.totalframe)
        self.surface4.grid(row = 1, column= 0)
        self.surface5 = tk.Frame(self.totalframe)
        self.surface5.grid(row = 0, column = 1)
        self.surface6 = tk.Frame(self.totalframe)
        self.surface6.grid(row = 2, column = 1)
        self.surfacecanvas1 = tk.Canvas(self.surface1, height=50, width=50)
        self.surfacecanvas1.pack()
        self.surfacecanvas2 = tk.Canvas(self.surface2, height=50, width=50)
        self.surfacecanvas2.pack()
        self.surfacecanvas3 = tk.Canvas(self.surface3, height=50, width=50)
        self.surfacecanvas3.pack()
        self.surfacecanvas4 = tk.Canvas(self.surface4, height=50, width=50)
        self.surfacecanvas4.pack()
        self.surfacecanvas5 = tk.Canvas(self.surface5, height=50, width=50)
        self.surfacecanvas5.pack()
        self.surfacecanvas6 = tk.Canvas(self.surface6, height=50, width=50)
        self.surfacecanvas6.pack()
        self.surfacecanvas = [self.surfacecanvas1, self.surfacecanvas2, self.surfacecanvas3, self.surfacecanvas4, self.surfacecanvas5, self.surfacecanvas6]
        self.surfacecanvaslist = []
        num = -1
        for canvas in self.surfacecanvas:
            num += 1 
            self.surfacecanvaslist.append([])
            for row in range(3):
                self.surfacecanvaslist[num].append([])
                for column in range(3):
                    self.totalrectangle= canvas.create_rectangle(5+15*column, 5+15*row, 20+15*column, 20+15*row, fill=cube.Rubiks_Cube[self.surfacecanvas.index(canvas)][row][column])
                    self.surfacecanvaslist[num][row].append(self.totalrectangle)
        self.mainloop()

    def vertical_call(self, column, rotation) : 
        cube.vertical(column, rotation)
        self.surface_select(cube.surface)
        self.total_action()  

    def horizontal_call(self, row, rotation) : 
        cube.horizontal(row, rotation)
        self.surface_select(cube.surface)
        self.total_action()    

    def surface_select(self, surface):
        self.surface = surface
        for row in range(3):
            for column in range(3):
                self.canvas.itemconfig(self.rectangles[row][column], fill=cube.Rubiks_Cube[surface][row][column]) 

    def total_action(self):
        for canvas in self.surfacecanvas:
            for row in range(3):
                for column in range(3):
                    canvas.itemconfig(self.surfacecanvaslist[self.surfacecanvas.index(canvas)][row][column], fill=cube.Rubiks_Cube[self.surfacecanvas.index(canvas)][row][column] )

    def resetter(self):
        cube.reset()
        self.surface_select(self.surface)
        self.total_action()

    def mixer(self) :
        cube.mix()
        self.surface_select(cube.surface)
        self.total_action()    
    
    def Settings(self):
        top = tk.Toplevel()
        top.title("Settings")
        top.geometry("250x250")
        button = tk.Button(top, text="OK", command=lambda : top.destroy())
        button.pack()
        top.mainloop()

    def load_file(self):
        loadfilename = filedialog.askopenfilename(initialdir=os.getcwd, title="Select", filetypes=(("JavaScript Object Notation",  "*.json*"), ("all files", "*.*"))) 
        load_cube = open(loadfilename, "r")
        jsoncube = json.load(load_cube)
        print(jsoncube["cube"])
        for i in range(6) :
            cube.Rubiks_Cube[i] = jsoncube["cube"][i]
        print(cube.Rubiks_Cube)
        self.surface_select(self.surface)
        self.total_action()

    def save_as_file(self):
        cubedict = {"cube" : cube.Rubiks_Cube, "Settings": None}
        savefilename = filedialog.asksaveasfilename(initialdir=os.getcwd, title="Select", filetypes=(("JavaScript Object Notation",  "*.json*"), ("all files", "*.*")))
        print(type(savefilename))
        print(savefilename)
        if savefilename == () :
            return
        self.save = savefilename
        with open(savefilename+".json", "w") as write_cube:
            json.dump(cubedict, write_cube)
        #except:
            #pass

    def save_current_file(self):
        cubedict = {"cube" : cube.Rubiks_Cube, "Settings": None}
        if self.save == None : 
            self.save_as_file()
            return
        with open(savefilename+".json", "w") as write_cube:
            json.dump(cubedict, write_cube)
    
    def new_file(self):
        self.resetter()
        self.save = None
        self.surface_select(self.surface)
        self.total_action()
        

cube = rc.Cube()

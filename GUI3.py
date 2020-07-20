#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import RubicsCubeOOP as rc
import os

class Pencere(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.surface = 0
        #Frames
        self.buttonframe = ttk.Frame(self, padding=(34,10,36,10), relief="groove")
        self.buttonframe.pack()
        self.surfaceframe= tk.Frame(self)
        self.surfaceframe.pack()
        self.totalframe = tk.Frame(self)
        self.totalframe.pack()
        #ButtonFrame Buttons
        self.button1 = ttk.Button(self.buttonframe, text="FRONT", command=lambda :self.surface_select(0))
        self.button1.grid(column=0, row=0)
        self.button2 = ttk.Button(self.buttonframe, text="RIGHT", command=lambda :self.surface_select(1))
        self.button2.grid(column=1, row=0)
        self.button3 = ttk.Button(self.buttonframe, text="BEHIND", command=lambda :self.surface_select(2))
        self.button3.grid(column=2, row=0)
        self.button4 = ttk.Button(self.buttonframe, text="LEFT", command=lambda :self.surface_select(3))
        self.button4.grid(column=3, row=0)
        self.button5 = ttk.Button(self.buttonframe, text="TOP", command=lambda :self.surface_select(4))
        self.button5.grid(column=4, row=0)
        self.button6 = ttk.Button(self.buttonframe, text="BOTTOM", command=lambda :self.surface_select(5))
        self.button6.grid(column=5, row=0)
        self.reset = ttk.Button(self.buttonframe, text="RESET", command=lambda :self.resetter())
        self.reset.grid(column=6, row=0)
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
        self.button1 = tk.Button(self.verticalframe, image=self.up, command=lambda : self.vertical(0, -1))
        self.button1.grid(row = 0, column = 0)
        self.button2 = tk.Button(self.verticalframe, image=self.up, command=lambda : self.vertical(2, -1))
        self.button2.grid(row= 0, column = 2)
        self.label1 = tk.Label(self.verticalframe)
        self.label1.grid(row= 0, column = 1, padx = 40)
        self.button3 = tk.Button(self.leftframe, image=self.left, command=lambda: self.horizontal(0, -1) )
        self.button3.grid(row = 1)
        self.label2 = tk.Label(self.leftframe)
        self.label2.grid(pady = 40, row = 2)
        self.button4 = tk.Button(self.leftframe, image=self.left, command=lambda: self.horizontal(2, -1))
        self.button4.grid(row = 3)
        self.button5 = tk.Button(self.rightframe, image=self.right, command=lambda: self.horizontal(0, 1))
        self.button5.grid()
        self.label3 = tk.Label(self.rightframe)
        self.label3.grid(pady = 40)
        self.button6 = tk.Button(self.rightframe, image=self.right, command=lambda: self.horizontal(2, 1))
        self.button6.grid()
        self.button7 = tk.Button(self.bottomframe, image = self.down, command=lambda : self.vertical(0, 1))
        self.button7.grid(row = 0, column = 0)
        self.label4 = tk.Label(self.bottomframe)
        self.label4.grid(padx = 40, row = 0, column = 1)
        self.button8 = tk.Button(self.bottomframe, image = self.down, command=lambda : self.vertical(2, 1) )
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

    def vertical(self, column, rotation):  # look = 0 acef rotation , look = 1 bdef rotation
                                        # rotation -1 --> up       1 --> down
        if self.surface == 0 or self.surface == 4 or self.surface == 5  :
            cube.mirrorx(cube.mirror(cube.c))
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_left(cube.d)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_right(cube.d)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_right(cube.b)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_left(cube.b)
            cube.mirrorx(cube.mirror(cube.c))
        if self.surface == 1 :
            cube.mirrorx(cube.mirror(cube.d))
            cube.rotate90_right(cube.e)
            cube.rotate90_left(cube.f)
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)
                    cube.rotate90_left(cube.a)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)                        
                    cube.rotate90_right(cube.a)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)                        
                    cube.rotate90_right(cube.c)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)
                    cube.rotate90_left(cube.c)
            cube.rotate90_right(cube.f)
            cube.rotate90_left(cube.e)
            cube.mirrorx(cube.mirror(cube.d))
        if self.surface == 2 :
            cube.mirrorx(cube.mirror(cube.c))
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(2, cube.vertical_rotation_a, 1)
                    cube.rotate90_left(cube.b)
                elif rotation == 1 :
                    cube.scrolly(2, cube.vertical_rotation_a, -1)
                    cube.rotate90_right(cube.b)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(0, cube.vertical_rotation_a, 1)
                    cube.rotate90_right(cube.d)
                elif rotation == 1 :
                    cube.scrolly(0, cube.vertical_rotation_a, -1)
                    cube.rotate90_left(cube.d)
            cube.mirrorx(cube.mirror(cube.c))
        if self.surface == 3 :
            cube.mirrorx(cube.mirror(cube.d))
            cube.rotate90_right(cube.e)
            cube.rotate90_left(cube.f)
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(2, cube.vertical_rotation_b, 1)
                    cube.rotate90_left(cube.c)
                elif rotation == 1 :
                    cube.scrolly(2, cube.vertical_rotation_b, -1)                        
                    cube.rotate90_right(cube.c)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(0, cube.vertical_rotation_b, 1)                        
                    cube.rotate90_right(cube.a)
                elif rotation == 1 :
                    cube.scrolly(0, cube.vertical_rotation_b, -1)
                    cube.rotate90_left(cube.a)
            cube.rotate90_right(cube.f)
            cube.rotate90_left(cube.e)
            cube.mirrorx(cube.mirror(cube.d))
        self.surface_select(self.surface)
        self.total_action()  

    def horizontal(self, row, rotation):  # direction ----> 1 = left -1 = right    
        if self.surface == 4 :
            cube.mirrorx(cube.mirror(cube.d))
            cube.rotate90_right(cube.e)
            cube.rotate90_left(cube.f)
            if row == 0:
                if rotation == -1 :
                    cube.scrolly(2, cube.vertical_rotation_b, -1)
                    cube.rotate90_right(cube.c)
                elif rotation == 1 :
                    cube.scrolly(2, cube.vertical_rotation_b, 1)                        
                    cube.rotate90_left(cube.c)
            elif row == 2 :
                if rotation == -1 :
                    cube.scrolly(0, cube.vertical_rotation_b, -1)                        
                    cube.rotate90_left(cube.a)
                elif rotation == 1 :
                    cube.scrolly(0, cube.vertical_rotation_b, 1)
                    cube.rotate90_right(cube.a)
            cube.rotate90_right(cube.f)
            cube.rotate90_left(cube.e)
            cube.mirrorx(cube.mirror(cube.d))
        elif self.surface == 5 :
            cube.mirrorx(cube.mirror(cube.d))
            cube.rotate90_right(cube.e)
            cube.rotate90_left(cube.f)
            if row == 0:
                if rotation == -1 :
                    cube.scrolly(row, cube.vertical_rotation_b, 1)
                    cube.rotate90_right(cube.a)
                elif rotation == 1 :
                    cube.scrolly(row, cube.vertical_rotation_b, -1)                        
                    cube.rotate90_left(cube.a)
            elif row == 2 :
                if rotation == -1 :
                    cube.scrolly(row, cube.vertical_rotation_b, 1)                        
                    cube.rotate90_left(cube.c)
                elif rotation == 1 :
                    cube.scrolly(row, cube.vertical_rotation_b, -1)
                    cube.rotate90_right(cube.c)
            cube.rotate90_right(cube.f)
            cube.rotate90_left(cube.e)
            cube.mirrorx(cube.mirror(cube.d))
        else :
            if row == 0  : 
                if rotation == -1 :
                    cube.scrollx(row, cube.horizontal_rotation , rotation)     
                    cube.rotate90_right(cube.e)
                elif rotation == 1 :
                    cube.scrollx(row, cube.horizontal_rotation , rotation)
                    cube.rotate90_left(cube.e)
            if row == 2  :
                if rotation == -1:
                    cube.scrollx(row, cube.horizontal_rotation , rotation)
                    cube.rotate90_left(cube.f)
                elif rotation == 1 :
                    cube.scrollx(row, cube.horizontal_rotation , rotation)
                    cube.rotate90_right(cube.f)
        self.surface_select(self.surface)
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
       
cube = rc.Cube()

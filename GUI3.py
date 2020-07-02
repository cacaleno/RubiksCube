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
        #Window Options
        #self.geometry("525x570")
        self.title("Rubik's Cube")
        self.wm_resizable(0,0)

        #logic
        self.intvar = tk.IntVar()
        self.intvar.set(0)
        
        #menubar(coming soon)

        #Cube Surface Buttons for Selection
        self.freym = ttk.Frame(self, padding=(34,10,36,10), relief="groove")
        self.freym.grid(row=0,column=1)
        
        self.butonyuzey1 = ttk.Button(self.freym, text="FRONT", command=lambda :self.destroy2(0))
        self.butonyuzey1.grid(column=0, row=0)
        self.butonyuzey2 = ttk.Button(self.freym, text="RIGHT", command=lambda :self.destroy2(1))
        self.butonyuzey2.grid(column=1, row=0)
        self.butonyuzey3 = ttk.Button(self.freym, text="BEHIND", command=lambda :self.destroy2(2))
        self.butonyuzey3.grid(column=2, row=0)
        self.butonyuzey4 = ttk.Button(self.freym, text="LEFT", command=lambda :self.destroy2(3))
        self.butonyuzey4.grid(column=3, row=0)
        self.butonyuzey5 = ttk.Button(self.freym, text="TOP", command=lambda :self.destroy2(4))
        self.butonyuzey5.grid(column=4, row=0)
        self.butonyuzey6 = ttk.Button(self.freym, text="BOTTOM", command=lambda :self.destroy2(5))
        self.butonyuzey6.grid(column=5, row=0)
        #self.reset = ttk.Button(self.freym, text="RESET", command=lambda :self.resetter())
        #self.reset.grid(column=6, row=0)
        self.left = tk.PhotoImage(file=os.getcwd()+"/buttons/left.png")
        self.right = tk.PhotoImage(file=os.getcwd()+"/buttons/right.png")
        self.up = tk.PhotoImage(file=os.getcwd()+"/buttons/up.png")
        self.down = tk.PhotoImage(file=os.getcwd()+"/buttons/down.png")
        self.frameselect()
        #messagebox.showinfo("UYARI", "Lütfen ÜST ve ALT yüzeylerde vertikal ve horizontal hareket kullanmayınız.Sadece diğer yüzey hareketlerini kontrol amaçlı bakınız. Yüzey 5 ve Yüzey 6 harektleri yapım aşamasındadır..") 
        self.mainloop()

    def frameselect(self):
        self.freym2 = tk.Frame(self, background="#ccffcc" )
        self.freym2.grid(column=1,row=1)
        for row in range(3) :
            for column in range(3) :
                self.label = tk.Label(self.freym2, background= cube.Rubiks_Cube[self.intvar.get()][row][column], width=12 , height=6  )
                self.label.grid(column=column+1, row=row+1 , padx=5, pady=5)
        #Buttons
        self.label2 = ttk.Button(self.freym2, image=self.left, command=lambda: self.horizontal(0, -1))
        self.label2.grid(column=0, row=1)
        self.label2 = ttk.Button(self.freym2, image=self.left, command=lambda: self.horizontal(2, -1))
        self.label2.grid(column=0, row=3)
        self.label3 = ttk.Button(self.freym2, image=self.right, command=lambda: self.horizontal(0, 1))
        self.label3.grid(column=4, row=1)
        self.label3 = ttk.Button(self.freym2, image=self.right, command=lambda: self.horizontal(2, 1))
        self.label3.grid(column=4, row=3)
        #Vertical Scrolls
        self.label14 = ttk.Button(self.freym2, image=self.up, command=lambda : self.vertical(0, -1))
        self.label14.grid(column=1, row=0)
        self.label15 = ttk.Button(self.freym2, image=self.down, command=lambda : self.vertical(0, 1))
        self.label15.grid(column=1, row=4)
        self.label16 = ttk.Button(self.freym2, image=self.up, command=lambda : self.vertical(2, -1))
        self.label16.grid(column=3, row=0)
        self.label17 = ttk.Button(self.freym2, image=self.down, command=lambda : self.vertical(2, 1))
        self.label17.grid(column=3, row=4)
        #Labels
        self.label_a = []
        self.label_b = []
        self.label_c = []
        self.label_d = []
        self.label_e = []
        self.label_f = []
        #All Surfaces
        self.frame0 = tk.Frame(self, background="#ccffcc" )
        self.frame0.grid(column=1,row=2)
        self.frame1 = ttk.Frame(self.frame0)
        self.frame1.grid(row=2,column=2)
        self.frame2 = ttk.Frame(self.frame0)
        self.frame2.grid(row=2,column=3)
        self.frame3 = ttk.Frame(self.frame0)
        self.frame3.grid(row=2,column=4)
        self.frame4 = ttk.Frame(self.frame0)
        self.frame4.grid(row=2,column=1)
        self.frame5 = ttk.Frame(self.frame0)
        self.frame5.grid(row=1,column=2)
        self.frame6 = ttk.Frame(self.frame0)
        self.frame6.grid(row=3,column=2)
        self.frames = [self.frame4, self.frame1, self.frame2, self.frame3, self.frame5, self.frame6]
        #Labels
        for frame in range(6):
            for row in range(3) :
                for col in range(3) :
                    self.label = tk.Label(self.frames[frame], background= cube.Rubiks_Cube_gui[frame][row][col],width=2 , height=1  )                    
                    self.label.grid(column=col+1, row=row, padx= 1, pady= 1)
    def destroy2(self,variable):
        self.freym2.destroy()
        self.intvar.set(variable)
        self.frameselect()

    def vertical(self, column, rotation):  # look = 0 acef rotation , look = 1 bdef rotation
                                            # rotation -1 --> up       1 --> down
        if self.intvar.get() == 0 or self.intvar.get() == 4 or self.intvar.get() == 5  :
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
        if self.intvar.get() == 1 :
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
        if self.intvar.get() == 2 :
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
        if self.intvar.get() == 3 :
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
        self.freym2.destroy()
        self.frameselect()

    def horizontal(self, row, rotation):  # direction ----> 1 = left -1 = right       
        if self.intvar.get() == 4 :
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
        elif self.intvar.get() == 5 :
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
        self.freym2.destroy()
        self.frameselect()

"""    def resetter(self):
        cube.reset()
        self.frameselect()"""
cube = rc.Cube()





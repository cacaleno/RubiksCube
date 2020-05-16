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
        self.geometry("525x570")
        self.title("Rubik's Cube")
        self.wm_resizable(0,0)

        #logic
        self.intvar = tk.IntVar()
        self.intvar.set(0)
        
        #menubar(coming soon)

        #Cube Surface Buttons for Selection
        self.freym = ttk.Frame(self, padding=(34,10,36,10), relief="groove")
        self.freym.grid()
        
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
        self.left = tk.PhotoImage(file=os.getcwd()+"/buttons/left.png")
        self.right = tk.PhotoImage(file=os.getcwd()+"/buttons/right.png")
        self.up = tk.PhotoImage(file=os.getcwd()+"/buttons/up.png")
        self.down = tk.PhotoImage(file=os.getcwd()+"/buttons/down.png")
        self.frameselect()
        messagebox.showinfo("UYARI", "Lütfen ÜST ve ALT yüzeylerde vertikal ve horizontal hareket kullanmayınız.Sadece diğer yüzey hareketlerini kontrol amaçlı bakınız. Yüzey 5 ve Yüzey 6 harektleri yapım aşamasındadır..") 
        self.mainloop()

    def frameselect(self):
        self.freym2 = tk.Frame(self , background="#ccffcc" )
        self.freym2.grid()
        for satır in range(3) :
            for sutun in range(3) :
                self.label1 = tk.Label(self.freym2, background= cube.Rubiks_Cube[self.intvar.get()][satır][sutun], width=12 , height=6  )
                self.label1.grid(column=sutun+1, row=satır+1 , padx=23, pady=20)
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
        self.label14 = ttk.Button(self.freym2, image=self.up, command=lambda : self.vertical(0, 1))
        self.label14.grid(column=1, row=0)
        self.label15 = ttk.Button(self.freym2, image=self.down, command=lambda : self.vertical(0, -1))
        self.label15.grid(column=1, row=4)
        self.label16 = ttk.Button(self.freym2, image=self.up, command=lambda : self.vertical(2, 1))
        self.label16.grid(column=3, row=0)
        self.label17 = ttk.Button(self.freym2, image=self.down, command=lambda : self.vertical(2, -1))
        self.label17.grid(column=3, row=4)
        
    def destroy2(self,variable):
        self.freym2.destroy()
        self.intvar.set(variable)
        self.frameselect()

    def vertical(self, column, rotation):  # look = 0 acef rotation , look = 1 bdef rotation
                                            # rotation -1 --> up       1 --> down
        if self.intvar.get() == 0 :
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_left(cube.d)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_rıght(cube.d)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_rıght(cube.b)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_left(cube.b)
        if self.intvar.get() == 1 :
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)
                    cube.rotate90_left(cube.a)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)                        
                    cube.rotate90_rıght(cube.a)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)                        
                    cube.rotate90_rıght(cube.c)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)
                    cube.rotate90_left(cube.c)
        if self.intvar.get() == 2 :
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_left(cube.b)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_right(cube.b)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_rıght(cube.d)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_a, rotation)
                    cube.rotate90_left(cube.d)
        if self.intvar.get() == 3 :
            if column == 0:
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)
                    cube.rotate90_left(cube.c)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)                        
                    cube.rotate90_rıght(cube.c)
            elif column == 2 :
                if rotation == -1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)                        
                    cube.rotate90_rıght(cube.a)
                elif rotation == 1 :
                    cube.scrolly(column, cube.vertical_rotation_b, rotation)
                    cube.rotate90_left(cube.a)
        if self.intvar.get() == 4 :
            if column == 0:
                pass
            elif column == 2 :
                pass
        if self.intvar.get() == 5 :
            if column == 0:
                pass
            elif column == 2 :
                pass
        self.freym2.destroy()
        self.frameselect()

    def horizontal(self, row, rotation):  # direction ----> 1 = left -1 = right       
        if self.intvar.get() == 4 or self.intvar.get() == 5 :
            pass
        else :
            if row == 0  : 
                if rotation == -1 :
                    cube.scrollx(row, cube.horizontal_rotation , rotation)     
                    cube.rotate90_rıght(cube.e)
                elif rotation == 1 :
                    cube.scrollx(row, cube.horizontal_rotation , rotation)
                    cube.rotate90_rıght(cube.e)
            if row == 2  :
                if rotation == -1:
                    cube.scrollx(row, cube.horizontal_rotation , rotation)
                    cube.rotate90_left(cube.f)
                elif rotation == 1 :
                    cube.scrollx(row, cube.horizontal_rotation , rotation)
                    cube.rotate90_rıght(cube.f)
        self.freym2.destroy()
        self.frameselect()

cube = rc.Cube()
pencere = Pencere()

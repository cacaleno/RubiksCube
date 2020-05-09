import tkinter as tk
from tkinter import ttk
import RubicsCubeOOP as rc


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
        self.look = tk.IntVar()   #acef or bdef 0(default)-> acef 1->bdef
        self.look.set(0)
        #menubar(coming soon)

        #Cube Surface Buttons for Selection
        self.freym = ttk.Frame(self, padding=(34,10,36,10), relief="groove")
        self.freym.grid()
        
        self.butonyuzey1 = ttk.Button(self.freym, text=f"Yüzey 1", command=lambda :self.destroy2(0))
        self.butonyuzey1.grid(column=0, row=0)
        self.butonyuzey2 = ttk.Button(self.freym, text=f"Yüzey 2", command=lambda :self.destroy2(1))
        self.butonyuzey2.grid(column=1, row=0)
        self.butonyuzey3 = ttk.Button(self.freym, text=f"Yüzey 3", command=lambda :self.destroy2(2))
        self.butonyuzey3.grid(column=2, row=0)
        self.butonyuzey4 = ttk.Button(self.freym, text=f"Yüzey 4", command=lambda :self.destroy2(3))
        self.butonyuzey4.grid(column=3, row=0)
        self.butonyuzey5 = ttk.Button(self.freym, text=f"Yüzey 5", command=lambda :self.destroy2(4))
        self.butonyuzey5.grid(column=4, row=0)
        self.butonyuzey6 = ttk.Button(self.freym, text=f"Yüzey 6", command=lambda :self.destroy2(5))
        self.butonyuzey6.grid(column=5, row=0)
        self.left = tk.PhotoImage(file="RUBIKS_CUBE/buttons/left.png")
        self.right = tk.PhotoImage(file="RUBIKS_CUBE/buttons/right.png")
        self.up = tk.PhotoImage(file="RUBIKS_CUBE/buttons/up.png")
        self.down = tk.PhotoImage(file="RUBIKS_CUBE/buttons/down.png")
        self.frameselect() 
        self.mainloop()

    def frameselect(self):
        self.freym2 = tk.Frame(self , background="#ccffcc" )
        self.freym2.grid()
        for satır in range(3) :
            for sutun in range(3) :
                self.label1 = tk.Label(self.freym2, background= cube.Rubiks_Cube[int(self.intvar.get())][satır][sutun], width=12 , height=6  )
                self.label1.grid(column=sutun+1, row=satır+1 , padx=23, pady=20)
        #Buttons
        
        self.label2 = ttk.Button(self.freym2, image=self.left, command=lambda: self.horizontal(1, 1))
        self.label2.grid(column=0, row=1)
        self.label2 = ttk.Button(self.freym2, image=self.left, command=lambda: self.horizontal(3, 1))
        self.label2.grid(column=0, row=3)
        self.label3 = ttk.Button(self.freym2, image=self.right, command=lambda: self.horizontal(1, -1))
        self.label3.grid(column=4, row=1)
        self.label3 = ttk.Button(self.freym2, image=self.right, command=lambda: self.horizontal(3, -1))
        self.label3.grid(column=4, row=3)
        #Vertical Scrolls
        self.label14 = ttk.Button(self.freym2, image=self.up, command=lambda : self.vertical(1, 1))
        self.label14.grid(column=1, row=0)
        self.label15 = ttk.Button(self.freym2, image=self.down, command=lambda : self.vertical(1, -1))
        self.label15.grid(column=1, row=4)
        self.label16 = ttk.Button(self.freym2, image=self.up, command=lambda : self.vertical(3, 1))
        self.label16.grid(column=3, row=0)
        self.label17 = ttk.Button(self.freym2, image=self.down, command=lambda : self.vertical(3, -1))
        self.label17.grid(column=3, row=4)

    def destroy2(self,variable):
        self.freym2.destroy()
        self.intvar.set(variable)
        self.frameselect()

    def vertical(self, column, rotation):  # look = 0 acef rotation , look = 1 bdef rotation
        if self.look.get() == 0 :          # rotation 1 --> up       -1 --> down
            if column == 1 :
                if rotation == 1 :
                    cube.scroll_column1_up_acef()
                    print(cube.Rubiks_Cube)
                elif rotation == -1 :
                    cube.scroll_column1_down_acef()
            elif column == 3 :
                if rotation == 1 :
                    cube.scroll_column3_up_acef()
                elif rotation == -1 :
                    cube.scroll_column3_down_acef()
        elif self.look.get() == 1 :
            if column == 1 :
                if rotation == 1 :
                    cube.scroll_column1_up_bedf()
                elif rotation == -1 :
                    cube.scroll_column1_down_bedf()
            elif column == 3 :
                if rotation == 1 :
                    cube.scroll_column3_up_bedf()
                elif rotation == -1 :
                    cube.scroll_column3_down_bedf()
        self.freym2.destroy()
        self.frameselect()

    def horizontal(self, row, direction): # direction ----> 1 = left -1 = right       
        if direction == 1 :
            cube.scroll_line_left(row)
        elif direction == -1 :
            cube.scroll_line_right(row)
        self.freym2.destroy()
        self.frameselect()

cube =rc.Cube()
pencere = Pencere()


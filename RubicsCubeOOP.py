#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Cube() :
    def __init__(self):
        super().__init__()
        self.a1 = ["#00ccff", "#00ccff", "#00ccff"]
        self.a2 = ["#00ccff", "#00ccff", "#00ccff"]
        self.a3 = ["#00ccff", "#00ccff", "#00ccff"]
        self.a =  [self.a1, self.a2, self.a3]
        self.b1 = ["white", "white", "white"]
        self.b2 = ["white", "white", "white"]
        self.b3 = ["white", "white", "white"]
        self.b  = [self.b1, self.b2, self.b3]
        self.c1 = ["green", "green", "green"]
        self.c2 = ["green", "green", "green"]
        self.c3 = ["green", "green", "green"]
        self.c  = [self.c1, self.c2, self.c3]
        self.d1 = ["yellow", "yellow", "yellow"]
        self.d2 = ["yellow", "yellow", "yellow"]
        self.d3 = ["yellow", "yellow", "yellow"]
        self.d  = [self.d1, self.d2, self.d3]
        self.e1 = ["red", "red", "red"]
        self.e2 = ["red", "red", "red"]
        self.e3 = ["red", "red", "red"]
        self.e  = [self.e1, self.e2, self.e3]
        self.f1 = ["orange", "orange", "orange"]
        self.f2 = ["orange", "orange", "orange"]
        self.f3 = ["orange", "orange", "orange"]
        self.f  = [self.f1, self.f2, self.f3]    
        self.Rubiks_Cube = [self.a, self.b, self.c, self.d, self.e, self.f]
        self.vertical_rotation_a = [self.a, self.f, self.c, self.e]
        self.vertical_rotation_b = [self.b, self.f, self.d, self.e]
        self.horizontal_rotation = [self.a, self.b, self.c, self.d]
        self.surface = 0

    def rotate90_left(self,matrix):
        new_matrix = []
        for i in range(len(matrix[0]), 0, -1):
            new_matrix.append(list(map(lambda x: x[i-1], matrix)))
        matrix[:] = new_matrix[:]
        return matrix

    def rotate90_right(self,matrix):
        rotated = [list(reversed(col)) for col in zip(*matrix)]
        matrix[:] = rotated[:]
        return matrix

    def scrolly(self, column, matrixes, rotation):
        y = len(matrixes)
        sütunlar = []
        for m in matrixes:
            sütun = []
            for i in m:
                sütun.append(i[column])
            sütunlar.append(sütun)
        rotation %= y
        if rotation < 0:
            rotation += y
        for i in range(rotation):
            sütunlar.insert(0, sütunlar.pop())
        for m, s in zip(matrixes, sütunlar):
            for i, j in zip(m, s):
                i[column] = j
        return matrixes

    def scrollx(self, line, matrixes, rotation):
        uzunluk = len(matrixes)
        satırlar = []
        for matris in matrixes:
            satırlar.append(matris[line])
        rotation %= uzunluk
        if rotation < 0:
            rotation += uzunluk
        for i in range(rotation):
            satırlar.insert(0, satırlar.pop())
        for a , b in zip(satırlar, matrixes) :
            b[line] = a
        return matrixes

    def mirror(self, matrix):
        for row in matrix:
            row.reverse()
        return matrix

    def mirrorx(self, matrix):
        matrix.reverse()
        return matrix    
    
    def reset(self):
        for surface in self.Rubiks_Cube :
            for row in surface:
                for column in row :
                    surface[surface.index(row)][row.index(column)] = surface[1][1]

    def vertical(self, column, rotation):  # look = 0 acef rotation , look = 1 bdef rotation
                                        # rotation -1 --> up       1 --> down
        if self.surface == 0 or self.surface == 4 or self.surface == 5  :
            self.mirrorx(self.mirror(self.c))
            if column == 0:
                if rotation == -1 :
                    self.scrolly(column, self.vertical_rotation_a, rotation)
                    self.rotate90_left(self.d)
                elif rotation == 1 :
                    self.scrolly(column, self.vertical_rotation_a, rotation)
                    self.rotate90_right(self.d)
            elif column == 2 :
                if rotation == -1 :
                    self.scrolly(column, self.vertical_rotation_a, rotation)
                    self.rotate90_right(self.b)
                elif rotation == 1 :
                    self.scrolly(column, self.vertical_rotation_a, rotation)
                    self.rotate90_left(self.b)
            self.mirrorx(self.mirror(self.c))
        if self.surface == 1 :
            self.mirrorx(self.mirror(self.d))
            self.rotate90_right(self.e)
            self.rotate90_left(self.f)
            if column == 0:
                if rotation == -1 :
                    self.scrolly(column, self.vertical_rotation_b, rotation)
                    self.rotate90_left(self.a)
                elif rotation == 1 :
                    self.scrolly(column, self.vertical_rotation_b, rotation)                        
                    self.rotate90_right(self.a)
            elif column == 2 :
                if rotation == -1 :
                    self.scrolly(column, self.vertical_rotation_b, rotation)                        
                    self.rotate90_right(self.c)
                elif rotation == 1 :
                    self.scrolly(column, self.vertical_rotation_b, rotation)
                    self.rotate90_left(self.c)
            self.rotate90_right(self.f)
            self.rotate90_left(self.e)
            self.mirrorx(self.mirror(self.d))
        if self.surface == 2 :
            self.mirrorx(self.mirror(self.c))
            if column == 0:
                if rotation == -1 :
                    self.scrolly(2, self.vertical_rotation_a, 1)
                    self.rotate90_left(self.b)
                elif rotation == 1 :
                    self.scrolly(2, self.vertical_rotation_a, -1)
                    self.rotate90_right(self.b)
            elif column == 2 :
                if rotation == -1 :
                    self.scrolly(0, self.vertical_rotation_a, 1)
                    self.rotate90_right(self.d)
                elif rotation == 1 :
                    self.scrolly(0, self.vertical_rotation_a, -1)
                    self.rotate90_left(self.d)
            self.mirrorx(self.mirror(self.c))
        if self.surface == 3 :
            self.mirrorx(self.mirror(self.d))
            self.rotate90_right(self.e)
            self.rotate90_left(self.f)
            if column == 0:
                if rotation == -1 :
                    self.scrolly(2, self.vertical_rotation_b, 1)
                    self.rotate90_left(self.c)
                elif rotation == 1 :
                    self.scrolly(2, self.vertical_rotation_b, -1)                        
                    self.rotate90_right(self.c)
            elif column == 2 :
                if rotation == -1 :
                    self.scrolly(0, self.vertical_rotation_b, 1)                        
                    self.rotate90_right(self.a)
                elif rotation == 1 :
                    self.scrolly(0, self.vertical_rotation_b, -1)
                    self.rotate90_left(self.a)
            self.rotate90_right(self.f)
            self.rotate90_left(self.e)
            self.mirrorx(self.mirror(self.d))

    def horizontal(self, row, rotation):  # direction ----> 1 = left -1 = right    
        if self.surface == 4 :
            self.mirrorx(self.mirror(self.d))
            self.rotate90_right(self.e)
            self.rotate90_left(self.f)
            if row == 0:
                if rotation == -1 :
                    self.scrolly(2, self.vertical_rotation_b, -1)
                    self.rotate90_right(self.c)
                elif rotation == 1 :
                    self.scrolly(2, self.vertical_rotation_b, 1)                        
                    self.rotate90_left(self.c)
            elif row == 2 :
                if rotation == -1 :
                    self.scrolly(0, self.vertical_rotation_b, -1)                        
                    self.rotate90_left(self.a)
                elif rotation == 1 :
                    self.scrolly(0, self.vertical_rotation_b, 1)
                    self.rotate90_right(self.a)
            self.rotate90_right(self.f)
            self.rotate90_left(self.e)
            self.mirrorx(self.mirror(self.d))
        elif self.surface == 5 :
            self.mirrorx(self.mirror(self.d))
            self.rotate90_right(self.e)
            self.rotate90_left(self.f)
            if row == 0:
                if rotation == -1 :
                    self.scrolly(row, self.vertical_rotation_b, 1)
                    self.rotate90_right(self.a)
                elif rotation == 1 :
                    self.scrolly(row, self.vertical_rotation_b, -1)                        
                    self.rotate90_left(self.a)
            elif row == 2 :
                if rotation == -1 :
                    self.scrolly(row, self.vertical_rotation_b, 1)                        
                    self.rotate90_left(self.c)
                elif rotation == 1 :
                    self.scrolly(row, self.vertical_rotation_b, -1)
                    self.rotate90_right(self.c)
            self.rotate90_right(self.f)
            self.rotate90_left(self.e)
            self.mirrorx(self.mirror(self.d))
        else :
            if row == 0  : 
                if rotation == -1 :
                    self.scrollx(row, self.horizontal_rotation , rotation)     
                    self.rotate90_right(self.e)
                elif rotation == 1 :
                    self.scrollx(row, self.horizontal_rotation , rotation)
                    self.rotate90_left(self.e)
            if row == 2  :
                if rotation == -1:
                    self.scrollx(row, self.horizontal_rotation , rotation)
                    self.rotate90_left(self.f)
                elif rotation == 1 :
                    self.scrollx(row, self.horizontal_rotation , rotation)
                    self.rotate90_right(self.f)

    def mix(self, mix_count = 1):
        rotation_axis = [-1, 1]
        row_column = [0, 2]
        moves = [0, 1, 2, 3, 4, 5]
        for i in range(mix_count):
            a =random.choice(moves)
            b = random.choice(row_column)
            c = random.choice(rotation_axis)
            self.surface = a
            mov_type = ["vertical","horizontal"]
            d = random.choice(mov_type)
            if d == "vertical" : 
                e = f"Vertikal{b, c}"
                self.vertical(b, c)
                #print("Yüzey:",a,"Hareket:",e)
            elif d == "horizontal":
                e = f"Horizontal{b, c}"
                self.horizontal(b, c)
                #print("Yüzey:",a,"Hareket:",e)

    def undo(self,mov_type, row_or_column, rotation):
        pass

    def mov_registry(self):
        pass
    
    def save(self):
        pass

    def load(self):
        pass

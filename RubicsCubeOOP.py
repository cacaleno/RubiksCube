

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
        self.c1 = ["red", "red", "red"]
        self.c2 = ["red", "red", "red"]
        self.c3 = ["red", "red", "red"]
        self.c  = [self.c1, self.c2, self.c3]
        self.d1 = ["green", "green", "green"]
        self.d2 = ["green", "green", "green"]
        self.d3 = ["green", "green", "green"]
        self.d  = [self.d1, self.d2, self.d3]
        self.e1 = ["yellow", "yellow", "yellow"]
        self.e2 = ["yellow", "yellow", "yellow"]
        self.e3 = ["yellow", "yellow", "yellow"]
        self.e  = [self.e1, self.e2, self.e3]
        self.f1 = ["orange", "orange", "orange"]
        self.f2 = ["orange", "orange", "orange"]
        self.f3 = ["orange", "orange", "orange"]
        self.f  = [self.f1, self.f2, self.f3]    
        self.Rubiks_Cube = [self.a, self.b, self.c, self.d, self.e, self.f]
        self.vertical_rotation_a = [self.a, self.e, self.c, self.f]
        self.vertical_rotation_b = [self.b, self.e, self.d, self.f]
        self.horizontal_rotation = [self.a, self.b, self.c, self.d]
    def rotate90_left(self,matrix):
        new_matrix = []
        for i in range(len(matrix[0]), 0, -1):
            new_matrix.append(list(map(lambda x: x[i-1], matrix)))
        matrix[:] = new_matrix[:]
        return matrix

    def rotate90_rıght(self,matrix):
        rotated = [list(reversed(col)) for col in zip(*matrix)]
        matrix[:] = rotated[:]
        return matrix
    
    def scroll_line1_left(self) :
        a4 = self.a1.copy()
        self.a1[0:] = self.b1[0:]
        self.b1[0:] = self.c1[0:]
        self.c1[0:] = self.d1[0:]
        self.d1[0:] = a4[0:]
        self.rotate90_rıght(self.e)        
        print(self.Rubiks_Cube)

    def scroll_line3_left(self) :
        a4 = self.a3.copy()
        self.a3[0:] = self.b3[0:]
        self.b3[0:] = self.c3[0:]
        self.c3[0:] = self.d3[0:]
        self.d3[0:] = a4[0:]
        self.rotate90_left(self.f)
        print(self.Rubiks_Cube)

    def scroll_line1_right(self) :
        a4 = self.a1.copy()
        self.a1[0:] = self.d1[0:]
        self.d1[0:] = self.c1[0:]
        self.c1[0:] = self.b1[0:]
        self.b1[0:] = a4[0:]
        self.rotate90_left(self.e)
        print(self.Rubiks_Cube)

    def scroll_line3_right(self) :
        a4 = self.a3.copy()
        self.a3[0:] = self.d3[0:]
        self.d3[0:] = self.c3[0:]
        self.c3[0:] = self.b3[0:]
        self.b3[0:] = a4[0:]
        self.rotate90_rıght(self.f)
        print(self.Rubiks_Cube)

    def scroll_line_left(self,x):
        if x == 1:
            self.scroll_line1_left()
        elif x == 3 :
            self.scroll_line3_left()

    def scroll_line_right(self,x):
        if x == 1:
            self.scroll_line1_right()
        elif x == 3 :
            self.scroll_line3_right()

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

    def scrollx(self, line, matrixes, rotation):
        uzunluk = len(matrixes)
        satırlar = []
        for matris in matrixes:
            satır = []
            satır.append(matris[line])
            satırlar.append(satır)
        rotation %= uzunluk
        if rotation < 0:
            rotation += uzunluk
        for i in range(rotation):
            satırlar.insert(0, satırlar.pop())
        for a , b in zip(satırlar, matrixes) :
            b[line] = a
          
cube = Cube()
print(cube.a1)



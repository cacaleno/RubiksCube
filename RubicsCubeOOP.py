
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

    def scroll_column1_up_acef(self) :
        a4 = self.a1[0] + self.a2[0] + self.a3[0]
        self.a1[0], self.a2[0], self.a3[0] = self.f1[0], self.f2[0], self.f3[0]
        self.f1[0], self.f2[0], self.f3[0] = self.c1[0], self.c2[0], self.c3[0]
        self.c1[0], self.c2[0], self.c3[0] = self.e1[0], self.e2[0], self.e3[0]
        self.e1[0], self.e2[0], self.e3[0] = a4[0], a4[1], a4[2]
        self.rotate90_left(self.d)
    
    def scroll_column3_up_acef(self) :
        a4 = self.a1[0] + self.a2[0] + self.a3[0]
        self.a1[2], self.a2[2], self.a3[2] = self.f1[2], self.f2[2], self.f3[2]
        self.f1[2], self.f2[2], self.f3[2] = self.c1[2], self.c2[2], self.c3[2]
        self.c1[2], self.c2[2], self.c3[2] = self.e1[2], self.e2[2], self.e3[2]
        self.e1[2], self.e2[2], self.e3[2] = a4[0], a4[1], a4[2]
        self.rotate90_rıght(self.b)

    def scroll_column1_down_acef(self) :
        a4 = self.a1[0] + self.a2[0] + self.a3[0]
        self.a1[0], self.a2[0], self.a3[0] = self.e1[0], self.e2[0], self.e3[0]
        self.c1[0], self.c2[0], self.c3[0] = self.f1[0], self.f2[0], self.f3[0]
        self.e1[0], self.e2[0], self.e3[0] = self.c1[0], self.c2[0], self.c3[0]
        self.f1[0], self.f2[0], self.f3[0] = a4[0], a4[1], a4[2]
        self.rotate90_rıght(self.d)

    def scroll_column3_down_acef(self) :
        a4 = self.a1[0] + self.a2[0] + self.a3[0]
        self.a1[2], self.a2[2], self.a3[2] = self.e1[2], self.e2[2], self.e3[2]
        self.c1[2], self.c2[2], self.c3[2] = self.f1[2], self.f2[2], self.f3[2]
        self.e1[2], self.e2[2], self.e3[2] = self.c1[2], self.c2[2], self.c3[2]
        self.f1[2], self.f2[2], self.f3[2] = a4[0], a4[1], a4[2]
        self.rotate90_left(self.b)
        
    def scroll_column1_up_bedf(self) :
        b4 = self.b1[0] + self.b2[0] + self.b3[0]
        self.b1[0], self.b2[0], self.b3[0] = self.f1[0], self.f2[0], self.f3[0]
        self.f1[0], self.f2[0], self.f3[0] = self.d1[0], self.d2[0], self.d3[0]
        self.d1[0], self.d2[0], self.d3[0] = self.e1[0], self.e2[0], self.e3[0]
        self.e1[0], self.e2[0], self.e3[0] = b4[0], b4[1], b4[2]
        rotate90_left(self.a)

    def scroll_column3_up_bedf(self) :
        b4 = self.b1[2] + self.b2[2] + self.b3[2]
        self.b1[2], self.b2[2], self.b3[2] = self.f1[2], self.f2[2], self.f3[2]
        self.f1[2], self.f2[2], self.f3[2] = self.d1[2], self.d2[2], self.d3[2]
        self.d1[2], self.d2[2], self.d3[2] = self.e1[2], self.e2[2], self.e3[2]
        self.e1[2], self.e2[2], self.e3[2] = b4[0], b4[1], b4[2]
        rotate90_rıght(self.c)

    def scroll_column1_down_bedf(self) :
        b4 = self.b1[0] + self.b2[0] + self.b3[2]
        self.b1[0], self.b2[0], self.b3[0] = self.e1[0], self.e2[0], self.e3[0]
        self.e1[0], self.e2[0], self.e3[0] = self.d1[0], self.d2[0], self.d3[0]
        self.d1[0], self.d2[0], self.d3[0] = self.f1[0], self.f2[0], self.f3[0]
        self.f1[0], self.f2[0], self.f3[0] = b4[0], b4[1], b4[2]
        rotate90_rıght(self.a)

    def scroll_column3_down_bedf(self) :
        b4 = self.b1[2] + self.b2[2] + self.b3[2]
        self.b1[2], self.b2[2], self.b3[2] = self.e1[2], self.e2[2], self.e3[2]
        self.e1[2], self.e2[2], self.e3[2] = self.d1[2], self.d2[2], self.d3[2]
        self.d1[2], self.d2[2], self.d3[2] = self.f1[2], self.f2[2], self.f3[2]
        self.f1[2], self.f2[2], self.f3[2] = b4[0], b4[1], b4[2]
        rotate90_left(self.c)

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
          
cube = Cube()
print(cube.a1)


from math import sqrt

class puntos_planos:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def mostrarC(self,x1,y1):
        print(f"{self.x} es la coordenada {x1}, {self.y} es la coordenada {y1}")
        
       
    def nuevasC(self,x2,y2):
        print(f"{self.x} tiene una nueva coordenada {x2}, {self.y} tiene una nueva coordenada {y2}")

    def calculoC(self,x1,y1,x2,y2):
         d=sqrt((x2-x1)**2+(y2-y1)**2)
         print(d)
        




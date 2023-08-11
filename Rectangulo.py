class rectangulo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def perimetro(self,base,h):
        p=2*(base+h)
        print("El perimero es: ",p)
     
    
    def area(self,base,h):
        a=base*h
        print("La base es: ",a)

    def pertenece(self,base,h):
        if base==h:
            print("el rectangulo es cuadrado")
        else:
            print("el rectangulo no es cuadrado")

rectanguloo=rectangulo("punto 1","punto 2")
rectanguloo.perimetro(2,3)
rectanguloo.area(2,3)
rectanguloo.pertenece(3,3)
rectanguloo.pertenece(5,3)
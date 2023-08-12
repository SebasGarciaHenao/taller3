class Circulo:

    def __init__(self,centro,radio):
        self.centro=centro
        self.radio=radio
       

    def areaC(self):
        pi=3.1416
        area=pi*self.radio**2
        print(area)
    
    def perimetroC(self):
        pi=3.1416
        perimetro=2*pi*self.radio
        print(perimetro)

  
  
      



circulo=Circulo(0,10)
circulo.areaC()
circulo.perimetroC()




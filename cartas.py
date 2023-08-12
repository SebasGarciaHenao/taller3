# Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas 
# solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que 
# representan los nombres de las 4 pintas que puede tener una carta.


class Cartas:

    def __init__(self,valor,pinta):
        self.valor=valor
        self.pinta=pinta
        
   

    def picas(self):
        print(f"la carta {self.valor} tiene la pinta de {self.pinta} ")
    
    def corazones(self):
        print(f"la carta {self.valor} tiene la pinta de {self.pinta} ")

    def rombos(self):
        print(f"la carta {self.valor} tiene la pinta de {self.pinta} ")

    def tréboless(self):
        print(f"la carta {self.valor} tiene la pinta de {self.pinta} ")


    




from Vehiculo import vehiculo

velocidad=120

kilometro=50000

print(vehiculo(velocidad,kilometro))



from punto import punto_pano
paraX=int(input("ingrese una cordenada: "))
paraY=int(input("ingrese una cordenada: "))

print(punto_pano(paraX,paraY))
        
from punto_mover import puntos_planos


coordenadas=puntos_planos("x","y")

coordenadas.mostrarC(4,8)

coordenadas.nuevasC(6,1)

coordenadas.calculoC(4,8,6,1)


from Rectangulo import rectangulo

rectanguloo=rectangulo("punto 1","punto 2")
rectanguloo.perimetro(2,3)
rectanguloo.area(2,3)
rectanguloo.pertenece(3,3)
rectanguloo.pertenece(5,3)

from circulo import Circulo

circulo=Circulo(0,10)
circulo.areaC()
circulo.perimetroC()


from cartas import Cartas

carta=Cartas(5,"picas")
carta.picas()
carta=Cartas(5,"corazones")
carta.corazones()
carta=Cartas(5,"rombos")
carta.rombos()
carta=Cartas(5,"tréboles")
carta.tréboless()
        
from CuentaBancaria import CuentaBancaria
cuenta=CuentaBancaria("CO12 1234 1234 12 0123456789","austin",1000000)

from CuentaBancaria import CuentaBancaria
cuenta1=CuentaBancaria("CO12 1234 1234 12 0123456789","austin",100000)
cuenta1.depositar()
cuenta1.retiro()
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()


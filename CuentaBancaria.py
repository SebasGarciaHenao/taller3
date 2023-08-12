class CuentaBancaria:
    
    def __init__(self,numero_cuenta,propietarios,balance):
        self.numero_cuenta=numero_cuenta
        self.propietarios=propietarios
        self.balance=balance
        print(f"la cuenta de {self.propietarios} tiene un balance de {self.balance} y su numero de cuenta es {self.numero_cuenta}")

    def depositar(self):
        valor=int(input("ingrese cantidad de dinero que desea depositrar: "))
        self.balance+=valor
        print("balance actual ",self.balance)

    def retiro(self):
        valor=int(input("ingrese cantidad de dinero que desea retirar: "))
        self.balance-=valor
        print("balance actual ",self.balance)

    def aplicar_cuota_manejo(self):
       cuota=self.balance*0.02
       print("el balance quedo en: ",cuota)
    
    def  mostrar_detalles(self):
        print("el propieratio es: ",self.propietarios)
        print("su numero de cuenta es: ",self.numero_cuenta)
        print("su dinero final fue de: ",self.balance)



        

       
        


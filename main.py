from Classes.Cliente import Cliente
from Classes.Cuenta import Cuenta


opt=1


print("*************************")
print("Bancolombia")
print("1. Registrar Cliente")
print("0. Salir")
print("*************************")

while(opt !=0):

    opt=int(input("Digita una opción: "))

    if(opt==1):
        name=input("Digite el nombre del usuario: ")
        lastName=input("Digite el apellido del usuario: ")
        id=input("Digite la cedula del usuario: ")
        balance=0
        accountNumber=input("Digite el número: ")

    cuenta=Cuenta(accountNumber,balance)   
    cliente=Cliente(name,lastName,id,accountNumber) 
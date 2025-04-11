import random

numero_secreto = random.randint(1,10)

while(True):
    numero_usuario = int(input("Dime un número del 1 al 10: "))

    if(numero_secreto == numero_usuario):
        print("Felicidades, adivinaste el número secreto")
        break
    else: 
        print("Sigue intentando")
    
    if(numero_secreto>numero_usuario):
        print("El número secreto es mayor")
    else:
        print("El número es menor")
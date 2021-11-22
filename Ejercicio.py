# Ejercicio 4: Escribir un programa que pregunte el nombre del
# usuario en la consola y un número entero e imprima por pantalla en 
# líneas distintas el nombre del usuario tantas veces como el número 
# introducido.
nombre = input("¿Cual es su nombre?\n")
numero = int(input("Ingrese un numero:\n"))
veces = 0
while(veces < numero):
    print(nombre)
    veces +=1


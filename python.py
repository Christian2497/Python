# Programa que muestre Hola Mundo

print("¡Hola Mundo!")

# Programa que almacene una variable con Hola Mundo y lo muestre

variable = "¡Hola Mundo!"

print(variable)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input("¿Cual es tu nombre?")
print("¡Hola " + nombre + "!")

# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

nombre = input("¿Cual es tu nombre? ")
numero = input("Introduce un numero ")

print((numero + "\n") * int(numero))

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
# <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre = input("¿Cual es tu nombre?")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

# Escribir un programa que realice la siguiente operación aritmética 

print(((3+2)/(2*5)) **2)

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla 
# la paga que le corresponde.

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))




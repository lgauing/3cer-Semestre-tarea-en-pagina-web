#Ejemplo 1:
# Calcular el factorial de N números enteros leídos de teclado.
# El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.
# El pseudocódigo es el siguiente:

# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1

class Tarea8:
    def _init_(self):
        pass
    def Factorial(self):
        n=int(input("ingrese la cantidad de numeros: "))
        for i in range(n):
            numero=int(input("ingrese numero: "))
            acu=1
            for num in range(numero,1,-1):
                acu=acu*num
            print("numero= {} factorial={}".format(numero,acu))

tarea=Tarea8()
tarea.Factorial()
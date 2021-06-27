#EJEMPLO 2.
# Leer tres números enteros diferentes entre sí
# y determinar el número mayor de los tres.
# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1

class numero_mayor():
    
    def numeroenteromayor(self):
        n1 = int(input("ingrese número 1: "))
        n2 = int(input("ingrese número 2: "))
        n3 = int(input("ingrese número 3: "))
        if n1 > n2 and n1 > n3:
             print("El número mayor es: ",n1)
        elif n2 > n1 and n2 > n3:
             print("El número mayor es: ",n2)
        else:
             print("El número mayor es: ",n3)
numero=numero_mayor()
numero.numeroenteromayor()

       
#EJEMPLO
# Calcular la suma de los cuadrados de los primeros
# 100 enteros y escribir el resultado.

# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1

class numero():

    def numcuadrados(self):
        num,sum=0,0
        num=int(input("ingrese el limite de cuadrado:"))
        print("---------------")
        for i in range(1,num+1):
            print(i,"^2")
            print("+")
            sum = sum+(i**2)
            print("La suma de los cuadrados es: ",sum)       
numero=numero()
numero.numcuadrados()  
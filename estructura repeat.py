#EJEMPLO
# Aplicar los pasos de la metodología para la solución de un problema
# para leer un número entero N y calcular el resultado de la siguiente serie:
# 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle
# Repeat controlado por contador y usando banderas.

class serie():
    def numentero(self):
        
        serie=0
        p=1
        num=int(input("Ingrese un numero entero: "))
        bandera = True
        while p<=num:
            if bandera==True:
                serie = serie+1/p
                bandera = False
            else:
                serie = serie-1/p
                bandera = True
            p=p+1
            print("La suma de la serie es: ",serie)
serie=serie()
serie.numentero()                            
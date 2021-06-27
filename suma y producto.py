#EJEMPLO
# Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
# utilizando un bucle controlado por el usuario.

class producto():
    
    def suma_producto(self):

        prod=1
        suma=0
        resp=input(str("Usted quiere ingresar numeros? (S/N)? : "))
        while resp!="N" and resp!="n":
            num=int(input("Dijite un numero: "))
            suma=suma+num
            prod = prod * num  
            resp=input(str("Desea continuar (S / N)?): "))
        print ("Total de la suma es:"  , suma)
        print ("Total de producto es:", prod)    
producto=producto()
producto.suma_producto()                

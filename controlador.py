class sumayproducto():
    def __init__ (self):
        pass
    def centinela(self):
        
        prod=1
        suma=0
        num=int(input("Dijite un numero entero que no sea negativo: "))
        while num != -1 :
            num=int(input("Ingrese un numero: "))
            suma=suma+num
            prod=prod*num
        print("""Total de la suma es:""",suma,
              """Total del producto es: """,prod)
suma=sumayproducto()
suma.centinela()       
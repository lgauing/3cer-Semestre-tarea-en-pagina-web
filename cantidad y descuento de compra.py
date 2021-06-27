#En una tienda se ofrece un descuento del 15% 
# sobre el total de la compra y un cliente desea 
# saber cuánto deberá pagar finalmente por su compra.
# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1

class descuento():
    def cantidaddescuento(self):
     Tc= float(input("Ingrese el valor del total de compra : "))
     D= Tc*0.15
     Cp= Tc-D
     print("El descuento de la compra es : ",D)
     print("La cantidad a pagar es: $ ",Cp)
descuento=descuento()
descuento.cantidaddescuento()
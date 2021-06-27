#En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie
# de un círculo para un radio cualquiera.
# El Flujograma que representa a dicho ejemplo es el siguiente:
# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1

# Ejericio 1 
#deber de la página web

import os,math
radio = float(input("Ingrese el valor del radio del circulo: "))
S=math.pi*pow(radio, 2)
print("Valor de la superficie del radio es : " + repr(S))
print()
os.system('pause')
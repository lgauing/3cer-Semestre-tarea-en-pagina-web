
# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1
class nota():
    def Calificaciones(self):
        cal=float(input("Ingrese calificación : "))
        if cal>=7:
            print("Aprobado")
        else:
            print("Reprobado")        
    print() 
nota=nota()
nota.Calificaciones()     
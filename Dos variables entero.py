class variable():
    
    def variables_tipoentero(self):
        
        Num= int(input("Ingrese la primera variable: "))
        V= int(input("Ingrese la segunda Variable: "))
        if Num== 1:
            Resp=100*V
        elif Num==2:
            Resp=pow(100,V)
        elif Num==3:
            Resp=100/V
        else:
            Resp=0
        print("Su Resultado es:",Resp)
variable=variable()
variable.variables_tipoentero()   
        
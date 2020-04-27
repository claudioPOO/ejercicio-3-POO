
class Cosecha:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def crearbi(self):
        for i in range(3):
            self.__lista.append([])
            for j in range(10):
                self.__lista[i].append(0)
     
    def mostrar(self):
        for fila in range(self.__lista):
            print(fila)
    def agregar(self,xcam,xdia,kg):
        self.__lista[xcam-1][xdia-1]+=kg
    def total(self,cam):
        tot=0
        for i in range(3):
            tot+=self.__lista[cam-1][i]
        return tot
    def comp(self,cam,dia):
        print('                                {}'.format(self.__lista[cam][dia-1]))
    
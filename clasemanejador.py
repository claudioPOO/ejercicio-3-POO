import csv
from clasecamion import Camion
class Manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def Testing(self):
        arc=open('Camion.csv')
        r=csv.reader(arc,delimiter=',')
        for fila in r:
             camion=Camion(fila[0],fila[1],fila[2],fila[3],fila[4])
             self.agregar(camion)
        arc.close()     
    def agregar(self,camion):
        self.__lista.append(camion) 
    def buscac(self,num):
        bandera=0
        while bandera!=100:
            i=0
            band=0
            while(i<3)and(band==0):
                if(num==self.__lista[i].getId()):
                    tara=self.__lista[i].getTara()
                    band=1
                    bandera=100
                i=i+1    
            if band==0:
                num=input('Id no encontrado ingrese nuevamente ')
                i=0
            else:
                return tara
                    
    def __str__(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i].mostrardatos())
    def condypat(self,ind):
        print('{}    {}   '.format(self.__lista[ind].getpatente(),self.__lista[ind].getNombre()))     
                

class Camion:
    __iden=''
    __NombreC=''
    __patente=''
    __Marca=''
    __tara=''
    def __init__(self,iden,nom,pat,marca,tara):
        self.__iden=int(iden)
        self.__NombreC=nom
        self.__patente=pat
        self.__Marca=marca
        self.__tara=tara
    def getTara(self):
        return self.__tara
    def getId(self):
        return self.__iden
    def getNombre(self):
        return  self.__NombreC
    def getpatente(self):
        return  self.__patente
    def mostrardatos(self):
        print(self.__iden,self.__NombreC,self.__patente,self.__Marca,self.__tara)
        
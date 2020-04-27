from clasemanejador import Manejador
from clasecosecha import Cosecha        

def  opcion0 (lista,listbi):
    print( "Adiós" )

def  opcion1 (lista,listbi):
   iden=int(input('Camion: '))
   total=listbi.total(iden)
   print('Total de kg= {}'.format(total))
def  opcion2 (lista,listbi):
    dia=int(input('Dia'))
    print('PATENTE  CONDUCTOR  CANTIDAD DE KILOS')
    for i in range(3):
        print('{}           {}'.format(lista.condypat(i),listbi.comp(i,dia)))   
switcher = {
    0 : opcion0,
    1 : opcion1,
    2 : opcion2,  
}

def switch (argumento,lista,listbi):
    func  =  switcher.get ( argumento , lambda : print ( "Opción incorrecta" ))
    func (lista,listabi)


if __name__=='__main__':
    lista=Manejador()
    lista.Testing()
    print('')
    lista.__str__()
    listabi=Cosecha()
    listabi.crearbi()
    idc=(input('Identificador de camion (Finalizar con fin): '))
    while(idc!='fin'):
        dia=int(input('Dia: '))
        peso=float(input('Peso camion cargado: '))
        xidc=int(idc)
        tarac=float(lista.buscac(xidc))
        pesoc=peso-tarac
        listabi.agregar(xidc,dia,pesoc)
        idc=(input('Identificador de camion (Finalizar con fin): '))
    bandera='falso'
    while bandera=='falso':
        
        print ( "      Menu" )
        print ( " 0 Salir" )
        print ( " 1 Identificador de camion para mostrar total de kg" )
        print ( " 2 Dia para conocer listado" )
        opcion =  int ( input ( "Ingrese una opción:" ))
        switch ( opcion,lista,listabi)
        op=(input('Desea Continuar? '))
        if(op=='no'):
            bandera='verdadero'
            
    
    

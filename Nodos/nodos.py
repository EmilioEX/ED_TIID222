#Creamos clase para los nodos
class Nodo:
    #Definimos constructor
    def __init__(self,numero):
        #Estructura de un nodo [numero][referencia]
        self.numero=numero
        self.siguiente=None


#Clase que administra los nodos de una lista Enlazada 
class ListaEnlazada:

    def __init__(self):
        self.cabeza=None

    def InsertarNodoAlInicio(self,numero):
        nuevo_nodo=Nodo(numero)
        #Comprobamos si la lsita esta vacía
        if (self.cabeza is None):
            #Convertimos el nuevo nodo en nuestra cabeza
            self.cabeza=Nodo(numero)
            return
        #Si la lista ya tenía nodos, el nuevo nodo apunta al que era la cabeza
        nuevo_nodo.siguiente=self.cabeza
        #actualizamos nuestra nueva cabeza para que apunte al nuevo nodo
        self.cabeza=nuevo_nodo
    def InsertarNodoAlFinal(self,numero):
        #Creamos el nodo con el número que recibe
        nuevo_nodo=Nodo(numero)
        #Comprobar si la lista está vacía
        if(self.cabeza==None):
            #Si la cabeza está vacía, el nodo será el primero (cabeza)
            self.cabeza=nuevo_nodo

            return
        #referencia temporal al primer nodo
        actual=self.cabeza
        #Cambiamos referncias de manera secuancial al agregar un nodo

        #avanzas mientras exista un nodo siguiente actual.siguiente
        while(actual.siguiente):
            #mi actual ahora pasa a ser mi actual.siguiente
            actual=actual.siguiente
        #cuando ya no hay actual siguiente es ahpi cuando conecta al nuevo nodo
        actual.siguiente=nuevo_nodo
    #método para imprimir nuestra lista enlazada
    def Imprimir_ListaEnlazada(self):
        
        #definimos el actual
        actual=self.cabeza
        #Repetimos ciclo por cada actual (true)
        while(actual):
            print(actual.numero, " → ", end=" ")
            #actual ahora se pasa al siguiente 
            actual=actual.siguiente
            
        #Al final tiene que apuntar a None
        print("None")



        
MiLista=ListaEnlazada()
MiLista.InsertarNodoAlInicio(2)
MiLista.InsertarNodoAlInicio(1)
MiLista.InsertarNodoAlFinal(56)
MiLista.Imprimir_ListaEnlazada()


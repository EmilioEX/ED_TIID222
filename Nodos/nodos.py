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

    def insertar_nodo_al_inicio(self,numero):
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
    def insertar_nodo_al_final(self,numero):
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
    def imprimir_lista_enlazada(self):
        
        #definimos el actual
        actual=self.cabeza
        #Repetimos ciclo por cada actual (true)
        while(actual):
            print(actual.numero, " → ", end=" ")
            #actual ahora se pasa al siguiente 
            actual=actual.siguiente
            
        #Al final tiene que apuntar a None
        print("None")
    #método para eliminar nodo el inicio
    def eliminar_nodo_al_inicio(self):
        #en caso de que no tenga elementos la lista, no hacemos nada
        if self.cabeza is None:
            print("La lista está vacía")
            return
        #la cabeza la "recorremos" uno hacia en frente
        self.cabeza=self.cabeza.siguiente
    def eliminar_nodo_al_final(self):
        #en caso de que no tenga elementos la lista, no hacemos nada
        if self.cabeza is None:
            print("La lista está vacía")
            return
        #en caso de que no exita un nodo siguiente (una lista de un solo nodo)
        if self.cabeza.siguiente is None:
            #"eliminamos" ese nodo y salimos del método
            self.cabeza=None
            return
        #variable temporal para recorrer la lista hasta llegar a un nodo que no apunte a nada (la cola)
        actual=self.cabeza
        #se utilizan dos "siguientes" porque es el siguiente caso (los primeros dos son los if's de arriba)
        while actual.siguiente.siguiente is not None:
            actual=actual.siguiente
        #en el momento en que llegemos a la "cola", le quitamos la referencia a ↓ 
        # un nodo antes de la "cola" para que sea la nueva cola
        actual.siguiente=None

        
MiLista=ListaEnlazada()
MiLista.insertar_nodo_al_inicio(4)
MiLista.insertar_nodo_al_inicio(3)
MiLista.insertar_nodo_al_inicio(2)
MiLista.insertar_nodo_al_inicio(1)
MiLista.insertar_nodo_al_final(56)
MiLista.imprimir_lista_enlazada()
MiLista.eliminar_nodo_al_final()
MiLista.imprimir_lista_enlazada()
MiLista.eliminar_nodo_al_inicio()
MiLista.imprimir_lista_enlazada()



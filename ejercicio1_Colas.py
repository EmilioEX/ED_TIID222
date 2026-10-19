from collections import deque

def imprimirMenu():
    print("========================")
    print("Menú de Python")
    print("\t1.- Insertar cola")
    print("\t2.- Borrar en cola")
    print("\t3.- Listar en cola")
    print("\t4.- Salir")

def encolar(cola):
    valor=int(input("Ingrese el valor que desea agregar a la cola: "))
    cola.append(valor)

def desencolar(cola):
    print("Se ha eliminado el primer valor en la cola\t")
    cola.popleft()

def listarCola(cola):
    print("---- Lista ----")
    if len(cola) == 0:
        print("La cola está vacía\t")
    else:
        for i, objetoLista in enumerate(cola):
            print(f"Posición {i}: {objetoLista}\t")


cola=deque()

while True:
    imprimirMenu()
    response=int(input("Escoge una opción: "))
    print("========================\t")
    if response == 1:
        encolar(cola)
    if response == 2:
        desencolar(cola)
    if response == 3:
        listarCola(cola)
    if response == 4:
        print("Ha salido exitosamente del programa")
        break
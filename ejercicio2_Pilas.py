from collections import deque

def imprimirMenu():
    print("========================")
    print("Menú de Pila")
    print("\t1.- Insertar en pila")
    print("\t2.- Borrar en pila")
    print("\t3.- Listar pila")
    print("\t4.- Salir")

def apilar(pila):
    valor = int(input("Ingrese el valor que desea agregar a la pila: "))
    pila.append(valor)

def desapilar(pila):
    print("Se ha eliminado el último valor en la pila\t")
    pila.pop()

def listarPila(pila):
    print("---- Lista ----")
    if len(pila)==0:
        print("La pila está vacía")
    else:
        for i, objetoLista in enumerate(reversed(pila)):
            print(f"Posición {i}: {objetoLista}")

pila = deque()

while True:
    imprimirMenu()
    response = int(input("Escoge una opción: "))
    print("========================")
    if response == 1:
        apilar(pila)
    if response == 2:
        desapilar(pila)
    if response == 3:
        listarPila(pila)
    if response == 4:
        print("Ha salido exitosamente del programa")
        break

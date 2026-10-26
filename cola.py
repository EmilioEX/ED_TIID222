from collections import deque
import time

cola = deque()

cola.append("Ana")
cola.append("Carlos")
cola.append("Elena")

print("Cola inicial: ", list(cola))

atendido = cola.popleft()
time.sleep(2)

print("Se atendió a ", atendido)
time.sleep(2)

print("Siguiente en la fila: ", cola[0])
time.sleep(2)
print("Cola restante: ", list(cola))

for i in range(n):
    dato= int(input("Ingrese un número: "))
    array.append(dato)
print("Arreglo original")

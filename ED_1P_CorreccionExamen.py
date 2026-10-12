matriz=[
    [73,12,89,34],
    [5,61,27,94],
    [46,18,80,3]
]

matriz.append([26,93,14,33])

print(matriz)

print(matriz[1])

for i in matriz:
    if 27 in i:
        print(f"27 encontrado en la fila {i}")
        break


for filas in matriz:
    for columna in filas:
        if columna == 3:
            print(f"3 encontrado en la fila {filas}")
            break
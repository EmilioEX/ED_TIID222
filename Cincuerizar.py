#ERG - Cincuerizar
#Declaro el arreglo
array=[]
#DEclaro y asigno tamaño del arreglo
n=15
#Solicito al usuario que ingrese datos con respecto al tamaño del arreglo
for i in range(n):
    dato= int(input("Ingrese un numero: "))
    array.append(dato)

print("\nArreglo Original: ")
print(array)

for i in range(n):
    residuo=array[i]%5

    if(residuo==1):
        array[i]+=4
    if(residuo==2):
        array[i]+=3
    if(residuo==3):
        array[i]+=2
    if(residuo==4):
        array[i]+=1
print("Arreglo Cincuarizado: ")
print(array)
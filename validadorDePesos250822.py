peso = 99;
acumulador1 = 0
acumulador2 = 0
contador1 = 0;
contador2 = 0;

while(peso != 0):

    peso = int(input("Ingrese el peso de la pieza o cero para salir: "))

    if(peso >= 5):
        print("El peso es mayor o igual a 5. El peso ingresado fue de: " + str(peso))
        acumulador1 = acumulador1 + peso
        contador1 += 1

    elif(peso < 5 and peso >= 1):
        print("El peso es menor a 5. El peso ingresado fue de: "  + str(peso))
        acumulador2 = acumulador2 + peso
        contador2 += 1


promedio1 = acumulador1/contador1
print("El acumulador 1 acumuló: "+ str(acumulador1) + " Kg.")
print("El acumulador 2 acumuló: "+ str(acumulador2) + " Kg.")
print(promedio1)

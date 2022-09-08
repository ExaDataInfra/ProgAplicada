def calculosEstadisticos(*tupla):
    total = 0
    for i in tupla:
        total +=i
    media = total / len(tupla)
    total = 0
    for i in tupla:
        total += (i-media)**2
    desvioStadard = (total / len(tupla)) ** 0.5
    return media, desvioStadard

media, desvio_Stadard = calculosEstadisticos(3, 4, 5, 7, 8, 10, 13, 16, 17, 18, 19, 20, 22, 24, 26, 27, 28, 33, 35, 36, 39, 41, 42, 44, 45, 46, 47, 50, 53, 59, 60, 63, 64, 66, 67, 68, 74, 78, 79, 80, 81, 82, 84, 85, 89, 91, 92, 95, 97, 99)
    
print(f"Dados los datos que anteceden, la media es de {media} y el desvío estándard es de {desvio_Stadard}") 

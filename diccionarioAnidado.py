clientesActivos = {
    0: {'DNI': '9999999', 'NombreApellido': 'Jerry', 'ValorCuota':50000},
    1: {'DNI': '9999998', 'NombreApellido': 'Tom', 'ValorCuota':32000}

}

indice = 2

clientesActivos[2] = {'DNI': '9999997', 'NombreApellido': 'Pinky', 'ValorCuota':17800}

valorCuotaFinal = (clientesActivos[indice]['ValorCuota'] * 1.2) + 500

print('El valor que deberá abonar ' +clientesActivos[indice]['NombreApellido']+ ' es de: ' + str(valorCuotaFinal))

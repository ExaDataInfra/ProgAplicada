def getUsuario(nombre, apellido, **infoAPI):
    print("Nombre del usuario: ",nombre)
    print("Apellido: ", apellido)
    for k in infoAPI:
        print("{0}: {1}".format(k, infoAPI[k]))
    
getUsuario("Juan", "Carlos", Profesion='Rey de Inglaterra', Edad='NaN', Nacionalidad='Británica')

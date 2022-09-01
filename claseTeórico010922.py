# Identificador de Clase
class Auto:
    
    ruedas = 4 #Atributo de clase
    
    #Constructor
    def __init__(self, marcaP, colorP, modeloP):
        #Atributos de instancia
        self.marca = marcaP
        self.color = colorP
        self.modelo = modeloP
        self.anio = 2022
        
    
    #Método
    def mostrarColor(self):
        return self.color
        
    
    def mostrarModelo(self):
        return self.modelo
        
        
    def cambiarColor(self, colorP):
        self.color = colorP
    
    
    def frenar(self, estadoDelFreno):
        if estadoDelFreno:
            return "El vehiculo está detenido"
        else:
            return "El vehiculo esta en marcha"
        
        
    def medidorVelocidadMaxima(self, velocidadActualP):
        if(velocidadActualP < 130):
            return True
            
      

#Cuando creamos un objeto de una clase, es decir, la "instanciamos" usamos el nombre de la clase
#y a continuación, le agregamos los atributos al contructor

vehiculo1 = Auto('BMW', 'Rojo', 'TT3')


print(vehiculo1.mostrarColor())

#Una vez que instanciamos, debemos hacer uso de los métodos con el operador "."
vehiculo1.cambiarColor('Verde')

print(vehiculo1.mostrarColor())


print(vehiculo1.frenar(True))

if(vehiculo1.medidorVelocidadMaxima(180)):
    print ("Dentro del permitido")
else:
    print ("Antención peligro de fotomulta! INFRACTOR!")
    

#GET: "Dame...el color..."
#SET: "Establecé determinado estado"

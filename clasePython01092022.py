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
    def getColor(self):
        return self.color
        
    
    def getModelo(self):
        return self.modelo
        

    def setColor(self, colorP):
        self.color = colorP
        
    
    def frenar(self, estadoDelFreno):
        if estadoDelFreno:
            return "El vehiculo está detenido"
        else:
            return "El vehiculo esta en marcha"
        
        
    def medidorVelocidadMaxima(self, velocidadActualP):
        if(velocidadActualP < 130):
            return True

   
    def calulaMultaPorExceso(self, velocidadMaximaP, velocidadActualIP):
        base = 1000
        
        if(velocidadMaximaP < velocidadActualIP < velocidadMaximaP*2):
            return base * 1.3
        
        elif(velocidadMaximaP*2 < velocidadActualIP < velocidadMaximaP*3):
            return base * 1.6
            
        elif(velocidadMaximaP*3 < velocidadActualIP < velocidadMaximaP*4):
            return base * 1.75
            
        
#Cuando creamos un objeto de una clase, es decir, la "instanciamos" usamos el nombre de la clase
#y a continuación, le agregamos los atributos al contructor

vehiculo1 = Auto('BMW', 'Rojo', 'TT3')

print(vehiculo1.getColor())

#Una vez que instanciamos, debemos hacer uso de los métodos con el operador "."
vehiculo1.setColor('Verde')

print(vehiculo1.getColor())


print(vehiculo1.frenar(True))

if(vehiculo1.medidorVelocidadMaxima(180)):
    print ("Dentro del permitido")
else:
    print ("Antención peligro de fotomulta! INFRACTOR!")
    
    
print("La multa es de: " + str(vehiculo1.calulaMultaPorExceso(90, 295)))

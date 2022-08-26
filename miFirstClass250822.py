class Animal:
    
    def __init__(self, edad, nombre, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    
    def obtenerNombre(self):
        return self.nombre
    
    def definirNombre(nombre):
        self.nombre = nombre
        
    
instanciaPatoNiato = Animal(2, 'Ringo', 1)
instanciaRatonPerez = Animal(70, 'Raton Perez', 350)

print("El nombre del pato es: " + instanciaPatoNiato.obtenerNombre())
print("El nombre del ratón de los dientes es: " + instanciaRatonPerez.obtenerNombre())

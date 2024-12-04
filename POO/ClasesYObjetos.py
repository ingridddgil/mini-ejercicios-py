class Celular:
    def __init__(self, marca, modelo, camara): #constructor 
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


samsung_s23 = Celular("Samsung", "S23", "24MP") # Estas son variables de instancia o propiedades de instancia porque se lo pasamos al crear el objeto
iphone14 = Celular("Iphone", "14", "96MP")
print(samsung_s23.modelo)
print(iphone14.modelo)
     
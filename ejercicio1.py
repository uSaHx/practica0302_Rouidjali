class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        return
    def cambiar_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    def get_datos(self):
        return self.codigo, self.nombre, self.precio
    def calcular_total(self, unidades):
        return unidades * self.precio

huevos = Producto(32, "huevos", 1.20)
print(huevos.get_datos())
huevos.cambiar_precio(3.50)
print(huevos.get_datos())
print(huevos.calcular_total(10))
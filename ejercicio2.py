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
class Pedido:
    def __init__(self, lista_productos, lista_cantidades):
        self.lista_productos = lista_productos
        self.lista_cantidades = lista_cantidades
        return
    def mostrar_productos(self):
        for x in self.lista_productos:
            print(x[1])
        return
    def total_pedido(self):
        total = 0
        for x in range(0, len(self.lista_productos)):
            total += self.lista_cantidades[x] * self.lista_productos[x][2]
        return total
huevos = Producto(32, "huevos", 1.20)
leche = Producto(6453, "leche", 0.93)
pan = Producto(68972, "pan", 1.15)
pedido1 = Pedido([huevos.get_datos(), leche.get_datos(), pan.get_datos()], [1, 2, 3])
pedido1.mostrar_productos()
print(pedido1.total_pedido())
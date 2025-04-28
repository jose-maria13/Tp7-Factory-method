# Producto
class Helado:
    def comer(self):
        pass

# Productos concretos
class HeladoChocolate(Helado):
    def comer(self):
        return "Estás comiendo un helado de Chocolate 🍫"

class HeladoVainilla(Helado):
    def comer(self):
        return "Estás comiendo un helado de Vainilla 🍦"

# Creador (Factory Method)
class FabricaHelados:
    def crear_helado(self):
        pass

# Fábricas concretas
class FabricaChocolate(FabricaHelados):
    def crear_helado(self):
        return HeladoChocolate()

class FabricaVainilla(FabricaHelados):
    def crear_helado(self):
        return HeladoVainilla()

# Cliente
def pedir_helado(fabrica):
    helado = fabrica.crear_helado()
    print(helado.comer())

# Ejecución
if __name__ == "__main__":
    print("Pedido 1:")
    pedir_helado(FabricaChocolate())

    print("\nPedido 2:")
    pedir_helado(FabricaVainilla())


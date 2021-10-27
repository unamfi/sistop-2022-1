#from CODE.Tienda import Tienda
class Proveedor(object):
    def __init__(self,id,tienda):
        self.id = id
        self.tienda=tienda
    def run(self):
        print("Proveedor listo y esperando llamada...")
    def suministrar(tienda):
        print("El proveedor ha despachado a la tienda")
        tienda.estante=100
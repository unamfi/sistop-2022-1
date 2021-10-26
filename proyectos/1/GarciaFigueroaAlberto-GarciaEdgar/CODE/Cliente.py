


class Cliente(object):
    def __init__(self, id):
        self.numero = id

    def entrar(self):
        print("El cliente "+str(self.numero)+" ha entrado a la tienda")
    
    def pagar(self):
        print("El cliente "+str(self.numero)+" ha pagado sus productos")
    
    def salir(self):
        print("El cliente"+str(self.numero)+" abandona la tienda")
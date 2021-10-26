


class Cliente:
    def __init__(self, id):
        self.id = id

    def entrar(self):
        print("El cliente "+self.numero+" ha entrado a la tienda")
    
    def pagar(self):
        print("El cliente "+self.numero+" ha pagado sus productos")
    
    def salir(self):
        print("El cliente"+self.numero+" abandona la tienda")
#from CODE.Empleado import Empleado

class Cliente(object):
    def __init__(self,id,tienda):
        self.numero = id
        self.tienda = tienda
        #self.empleado = empleado

    def entrar(self):
        print("El cliente "+str(self.numero)+" ha entrado a la tienda")
        self.agarra()

    def agarra(self):
        if self.tienda.estante <15:
            print("El cliente"+str(self.numero)+"notifica que se acaban los productos...")
            self.empleado.checarEstante()
        print("El cliente"+str(self.numero)+" agarra los productos")
        self.pagar()
    
    def pagar(self):
        print("El cliente "+str(self.numero)+" ha pagado sus productos")
        self.salir()
    
    def salir(self):
        print("El cliente"+str(self.numero)+" abandona la tienda")
        self.tienda.aforo=self.tienda.aforo-1
class Proceso:
    def __init__(self,tiempo_de_llegada,t,id):
        self.t=t
        self.tiempo_de_llegada=tiempo_de_llegada
        self.id=id
        self.inicio=0
        self.fin=0
        self.T=0
        self.E=0
        self.P=0
        self.tRestantes = t

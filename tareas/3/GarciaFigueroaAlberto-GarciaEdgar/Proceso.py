class Proceso:
    def __init__(self,t,tiempo_de_llegada,id):
        self.t=t
        self.tiempo_de_llegada=tiempo_de_llegada
        self.id=id
        self.inicio=0
        self.fin=0
        self.T=0
        self.E=0
        self.P=0

    def getTiempoLlegada(self):
        return self.tiempo_de_llegada
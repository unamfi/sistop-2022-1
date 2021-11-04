class SRR():
    def __init__(self,pato,a,b):###a = nuevos , b =aceptados
        super().__init__(pato)
        self.a = a
        self.b=b
        self.top_new = 0
        self.top_acc = 0
        self.new = []
        ###cola == self.acc

    def siguiente_proceso(self,procesos_a_ejecutar):
        to_add = []
        if procesos_a_ejecutar:
            self.new.extend([[x,0] for x in procesos_a_ejecutar]) ## new[proceso,valor_new]
        if self.top_acc<=self.top_new or  (not self.cola and not self.anterior):
            if not self.cola and not self.anterior:
                self.top_acc=self.top_new
            to_add = [ i[0] for i in filter(lambda x: x[1]>=self.top_acc,self.new)] ##Se agregan solo aquellos que cumplan con uno de los dos criterios
            self.new = list(filter(lambda x: x[1]<self.top_acc,self.new))
        #letra,tiempo = RR.siguiente_proceso(self,to_add)###ejecutamos la RR
        if self.new:
            self.new = [ [x,y+self.a] for x,y in self.new] ### sumamos al de new
            self.top_new = self.new[0][1]
        else:
            self.top_new = 0
        self.top_acc+=self.b
        #return letra,tiempo

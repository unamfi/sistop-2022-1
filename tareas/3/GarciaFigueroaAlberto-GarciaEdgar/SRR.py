from collections import deque
import operator
class SRR:
    def __init__(self,ProcesoA,ProcesoB,ProcesoC,ProcesoD,ProcesoE): #Tiempos en donde entran al sistema
        self.A=ProcesoA
        self.B=ProcesoB
        self.C=ProcesoC
        self.E=ProcesoE
        self.D=ProcesoD
        self.T_total=0
        self.P_total=0
        self.E_total=0
        self.TiempoTotal=0
        self.Final = []

    def run(self, a = 1, b = 2): 
        procesos=[self.A,self.B,self.C,self.D,self.E]
        procesosBase=[self.A,self.B,self.C,self.D,self.E]

        sortedProcesses=sorted(procesos, key=operator.attrgetter("tiempo_de_llegada"))
        terminados=[]
        queueAceptados = []
        prioridadAceptados = 0 
        queueNuevos = []    
        queueAceptados.append(sortedProcesses.pop(0))
        while queueAceptados:
            proc = queueAceptados.pop(0)
            print(str(proc.id)+''+str(proc.tRestantes))
            if proc.tRestantes == proc.t:
                proc.inicio = self.TiempoTotal
            self.TiempoTotal += 1
            self.Final += proc.id
            proc.tRestantes -= 1 
            prioridadAceptados += a 
            for x in procesosBase: 
                if(x.tiempo_de_llegada == self.TiempoTotal):
                    procNuevo= (sortedProcesses.pop(0))
                    print("Encontre a "+str(procNuevo.id))
            if(procNuevo):
                queueNuevos.append(procNuevo)
                
            if (queueNuevos and (b/prioridadAceptados == 0)):
                queueAceptados.append(queueNuevos.pop(0))
            if proc.tRestantes:
                
                queueAceptados.append(proc)
                
            else:
                
                proc.fin = self.TiempoTotal
                terminados.append(proc)

            if not queueAceptados and queueNuevos:
                
                queueAceptados.append(queueNuevos.pop(0))
    
    def listDiaf(self):
        for i in self.Final:
            print(str(i) , end = '')























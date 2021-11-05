from collections import deque
import operator
class SPN:
    def __init__(self,ProcesoA,ProcesoB,ProcesoC,ProcesoD,ProcesoE):
        self.A=ProcesoA
        self.B=ProcesoB
        self.C=ProcesoC
        self.E=ProcesoE
        self.D=ProcesoD
        self.T_total=0
        self.P_total=0
        self.E_total=0
        self.TiempoTotal=0
        self.Final=[]
        

    def run(self):
        procesos=[self.A,self.B,self.C,self.D,self.E]
        procesosBase=[self.A,self.B,self.C,self.D,self.E]
        sortedProcesses=sorted(procesos, key=operator.attrgetter("tiempo_de_llegada")) 
        queueProcesos = []
        for i in sortedProcesses:
            queueProcesos.append(i)
        primero = True        
        waiting=[]
        waiting.append(sortedProcesses.pop(0))
        terminados=[]
        while waiting:
            proc = waiting.pop(0)
            if(primero==True):
                proc.inicio = proc.tiempo_de_llegada
                primero = False
            while (proc.tRestantes > 0):
                self.TiempoTotal += 1
                proc.tRestantes-=1
                self.Final += proc.id
                for x in procesosBase:
                    if(x.tiempo_de_llegada == self.TiempoTotal):
                        waiting.append(sortedProcesses.pop(0))
            proc.fin= self.TiempoTotal
            terminados.append(proc)
            waiting = sorted(waiting, key=operator.attrgetter("t")) 

        for i in terminados:
            i.T =i.fin - i.tiempo_de_llegada
            i.E = i.T -i.t
            i.P =i.T /i.t
            #print(i.id +"  "+str(i.tiempo_de_llegada)+"  "+str(i.t)+"  "+str(i.inicio)+"  "+str(i.fin)+"  " +str(i.T)+"  " + str(i.E)+"  " + str(i.P))
            self.T_total= self.T_total + i.T
            self.E_total= self.E_total + i.E
            self.P_total= self.P_total + i.P 
        self.T_total=self.T_total / len(terminados) 
        self.E_total=self.E_total / len(terminados) 
        self.P_total=self.P_total / len(terminados) 
    
    def listDiaf(self):
        for i in self.Final:
            print(str(i) , end = '')
        print("")
        print("\nEL valor de T:"+str(self.T_total))
        print("EL valor de E:"+str(self.E_total))
        print("EL valor de P:"+str(round((self.P_total),2)))


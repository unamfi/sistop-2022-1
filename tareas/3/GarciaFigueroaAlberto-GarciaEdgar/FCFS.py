from collections import deque
import operator

class FCFS:
    def __init__(self,ProcesoA,ProcesoB,ProcesoC,ProcesoD,ProcesoE): #Tiempos en donde entran al sistema
        self.A=ProcesoA
        self.B=ProcesoB
        self.C=ProcesoC
        self.E=ProcesoE
        self.D=ProcesoD
        self.T_total=0
        self.P_total=0
        self.E_total=0

    def run(self):
        procesos = deque()
        fin_anterior=0
        primero = True
        procesos=[self.A,self.B,self.C,self.D,self.E]
        sortedProcesses=sorted(procesos, key=operator.attrgetter("tiempo_de_llegada"))
        for proc in sortedProcesses:
            if(primero):
                proc.inicio = proc.tiempo_de_llegada
                proc.fin = proc.t
                proc.T = proc.t
                proc.E = proc.tiempo_de_llegada
                primero = False
                fin_anterior = proc.fin
                proc.P = proc.T / proc.t
            else:
                proc.inicio= fin_anterior
                proc.fin = proc.inicio + proc.t
                proc.T = proc.inicio - proc.tiempo_de_llegada + proc.t
                proc.E =  proc.inicio - proc.tiempo_de_llegada
                fin_anterior = proc.fin
                proc.P = proc.T / proc.t
            self.T_total= self.T_total + proc.T
            self.E_total= self.E_total + proc.E
            self.P_total= self.P_total + proc.P
            print(proc.id * proc.t , end = '')
        print("\nEL valor de T:"+str(self.T_total/len(procesos)))
        print("EL valor de E:"+str(self.E_total/len(procesos)))
        print("EL valor de P:"+str(round((self.P_total/len(procesos)),2)))
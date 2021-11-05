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
        T=0
        E=0
        fin_anterior=0
        primero = True
        procesos=[self.A,self.B,self.C,self.D,self.E]
        sortedProcesses=sorted(procesos, key=operator.attrgetter("tiempo_de_llegada"))
        for i in sortedProcesses:
            if(primero):
                i.inicio = i.tiempo_de_llegada
                i.fin = i.t
                i.T = i.t
                i.E = i.tiempo_de_llegada
                primero = False
                fin_anterior = i.fin
                i.P = i.T / i.t
            else:
                i.inicio= fin_anterior
                i.fin = i.inicio + i.t
                i.T = i.inicio - i.tiempo_de_llegada + i.t
                i.E =  i.inicio - i.tiempo_de_llegada
                fin_anterior = i.fin
                i.P = i.T / i.t
            self.T_total= self.T_total + i.T
            self.E_total= self.E_total + i.E
            self.P_total= self.P_total + i.P
            print(i.id * i.t , end = '')
        print("\nEL valor de T"+str(self.T_total/len(procesos)))
        print("EL valor de E"+str(self.E_total/len(procesos)))
        print("EL valor de P"+str(self.P_total/len(procesos)))
from collections import deque
class FCFS:
    def __init__(self,A,B,C,D,E): #Tiempos en donde entran al sistema
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        self.E=E

    def run(self):
        cola= deque()
        procesos=[self.A,self.B,self.C,self.D,self.E]
        procesos.sort()
        
        for i in procesos:
            for j in i:
                if(i==self.A):
                    print("A")
                elif(i==self.B):
                    print("B")
                elif(i==self.C):
                    print("C")
                elif(i==self.D):
                    print("D")
                elif(i==self.E):
                     print("E")
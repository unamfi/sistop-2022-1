from collections import deque
import numpy as np

class RoundRobin:
    def __init__(self,quantum,procesos=[]):
        self.rr_queue=deque([procesos[0]])
        self.ejecutados_visual = ""
        self.ejecutados = []
        self.t = self.rr_queue[0].arrvl_time
        self.quantum = quantum
        self.procesos = procesos[1:]
    
    def check_for_new_process(self):
        for i in self.procesos:
            if i.arrvl_time <= self.t:
                self.rr_queue.append(i)
                self.procesos.remove(i)

    def execute(self):
        while len(self.rr_queue)>0:
            if self.rr_queue[0].arrvl_time > self.t:
                self.ejecutados_visual+='='     
                self.t += 1
            else:
                ejecutando = self.rr_queue.popleft()
                timeLeft = ejecutando.timeLeft
                if ejecutando.execute(self.quantum):
                    self.ejecutados_visual += timeLeft*ejecutando.id
                    self.t += timeLeft
                    ejecutando.compl_time = self.t
                    self.ejecutados.append(ejecutando)
                else:
                    self.ejecutados_visual += self.quantum*ejecutando.id
                    self.t+=self.quantum
                    self.procesos.append(ejecutando)
                self.check_for_new_process()                

    def results(self):
        T=0
        for i in self.ejecutados:
            T+= (i.compl_time - i.arrvl_time)
        T = np.mean(T)/len(self.ejecutados)
        print(T)

        print(self.ejecutados_visual)
    
from process import Process
from collections import deque
import numpy as np

class Fcfs:
    def __init__(self,procesos=[]):
        self.fcfs_queue = deque(procesos)
        self.ejecutados_visual = ""
        self.ejecutados = []
        self.t = self.fcfs_queue[0].arrvl_time

    def execute(self):
        while len(self.fcfs_queue)>0:
            if self.fcfs_queue[0].arrvl_time > self.t:
                self.ejecutados_visual+='='     
                self.t += 1
            else:
                ejecutando = self.fcfs_queue.popleft()
                while ejecutando.timeLeft > 0 : 
                    self.ejecutados_visual+=ejecutando.id     
                    ejecutando.execute(1)
                    self.t +=1
                ejecutando.compl_time = self.t
                self.ejecutados.append(ejecutando)

    def results(self):
        T=0
        for i in self.ejecutados:
            T+= (i.compl_time - i.arrvl_time)
        T = np.mean(T)/len(self.ejecutados)
        print(T)

        print(self.ejecutados_visual)

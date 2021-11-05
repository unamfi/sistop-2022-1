from scheduler import Scheduler
from collections import deque

class RoundRobin(Scheduler):
    name = "Round Robin (RR)"
    def __init__(self,procesos=[],quantum=1):
        self.ejecutados = []
        self.ejecutados_visual = ""
        self.getMaxT(procesos)
        self.rr_queue=deque([procesos[0]])
        self.t = self.rr_queue[0].arrvl_time
        self.quantum = quantum
        self.name+=" con quantum = "+str(self.quantum)
        self.procesos = procesos[1:]
        
    
    def check_for_new_process(self):
        for i in self.procesos:
            if i.arrvl_time <= self.t:
                self.rr_queue.append(i)
                self.procesos.remove(i)

    def execute(self):
        while self.t < self.max_t:
            if self.rr_queue:
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
            else:
                self.emptyExec()
            self.check_for_new_process()
                               
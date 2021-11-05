from scheduler import Scheduler
from collections import deque

class Spn(Scheduler):
    name = "Shortest Process Next (SPN)"
    ejecutados = []
    ejecutados_visual = ""
    def __init__(self,procesos=[]):
        self.spn_queue = deque()
        self.t = procesos[0].arrvl_time
        self.procesos = procesos
        self.getMaxT(procesos)
        self.check_for_new_process()
        
    def check_for_new_process(self):
        list=[]
        for i in self.procesos:
            #print(i.id+" "+str(i.exec_time))
            if i.arrvl_time <= self.t:
                list.append(i)
            #    self.procesos.remove(i)
        list.sort(key=lambda Process: Process.exec_time)
        for i in list:
            self.spn_queue.append(i)
            self.procesos.remove(i)
    

    def execute(self):
        while self.t < self.max_t:
            if self.spn_queue:
                ejecutando = self.spn_queue.popleft()
                self.ejecutados_visual+=ejecutando.id
                self.t +=1
                while not ejecutando.execute(1) : 
                    self.ejecutados_visual+=ejecutando.id
                    self.t +=1
                ejecutando.compl_time = self.t
                self.ejecutados.append(ejecutando)
            else:
                self.emptyExec()
            self.check_for_new_process()
                
            #print(self.t)
from scheduler import Scheduler
from collections import deque

class Fcfs(Scheduler):
    name = "First Come First Serve (FCFS)"
    def __init__(self,procesos):
      self.ejecutados = []
      self.ejecutados_visual = ""
      self.fcfs_queue = deque(procesos)
      self.t = self.fcfs_queue[0].arrvl_time

    def execute(self):
        while len(self.fcfs_queue)>0:
            if self.fcfs_queue[0].arrvl_time > self.t:
                self.emptyExec()
            else:
                ejecutando = self.fcfs_queue.popleft()
                while ejecutando.timeLeft > 0 : 
                    self.ejecutados_visual+=ejecutando.id     
                    ejecutando.execute(1)
                    self.t +=1
                ejecutando.compl_time = self.t
                self.ejecutados.append(ejecutando)

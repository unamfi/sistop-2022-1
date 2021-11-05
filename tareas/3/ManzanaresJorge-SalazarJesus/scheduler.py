
import numpy as np

class Scheduler:
  procesos = []
  max_t = 0

  def results(self):
      T=self.getT()
      E=self.getE()
      P=self.getP()
      print("T: " ,T)
      print("E: " ,E)
      print("P: " ,P)
      print("Esquema de ejecución:")
      print(self.ejecutados_visual)


  def getT(self):
    T=0
    for i in self.ejecutados:
      T+= (i.compl_time - i.arrvl_time)
    T = round(np.mean(T)/len(self.ejecutados), 2)
    return T


  def getE(self):
    T = 0
    E = 0
    for i in self.ejecutados:
      T = (i.compl_time - i.arrvl_time)
      E += (T - i.exec_time)
    E = round(np.mean(E)/len(self.ejecutados), 2)
    return E


  def getP(self):
    T = 0
    P = 0
    for i in self.ejecutados:
      T = (i.compl_time - i.arrvl_time)
      P += (T/i.exec_time)
    P = round(np.mean(P)/len(self.ejecutados), 2)
    return P

  def getMaxT(self,procesos=[]):
    for proceso in procesos:
      self.max_t += proceso.exec_time
  
  def emptyExec(self):
      self.ejecutados_visual+='_'     
      self.t += 1
      self.max_t += 1

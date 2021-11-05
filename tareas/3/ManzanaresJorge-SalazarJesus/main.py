#!/usr/bin/python3
from process import Process
from fcfs import Fcfs #, Rr, Spn, Utilities, Fb
from roundrobin import RoundRobin
from spn import Spn
import random, copy

proc_list = []
error = 1

#Método para crear procesos con datos predeterminados
def create_default_load():
  proc_list.append(Process("A", 0, 3)) 
  proc_list.append(Process("B", 1, 5))
  proc_list.append(Process("C", 3, 2))
  proc_list.append(Process("D", 9, 5))
  proc_list.append(Process("E", 12, 5))

  sorted_list = sorted(proc_list, key=lambda Process: Process.arrvl_time)
  run(sorted_list)

#Método para crear procesos con datos aleatorios  
def create_random_load():
  proc_list.append(Process("A", random.randint(0, 10), random.randint(1, 10))) 
  proc_list.append(Process("B", random.randint(0, 10), random.randint(1, 10)))
  proc_list.append(Process("C", random.randint(0, 10), random.randint(1, 10)))
  proc_list.append(Process("D", random.randint(0, 10), random.randint(1, 10)))
  proc_list.append(Process("E", random.randint(0, 10), random.randint(1, 10)))
  sorted_list = sorted(proc_list, key=lambda Process: Process.arrvl_time)
  if sorted_list[0].arrvl_time != 0:
      diff = sorted_list[0].arrvl_time
      for process in sorted_list:
          process.arrvl_time-=diff
  run(sorted_list)

#Método para ejecutar los algoritmos con una lista previamente ordenada
def run(list=[]):
  print("Los procesos son:")
  for i in list:
    print("ID: ",i.id, ", Tiempo de llegada: ", i.arrvl_time,", Tiempo de ejecución: ", i.exec_time)

  fcfs = Fcfs(copy.deepcopy(list))
  rr = RoundRobin(copy.deepcopy(list))
  rr4 = RoundRobin(copy.deepcopy(list),4)
  spn = Spn(copy.deepcopy(list))


  schedulers = [fcfs,rr,rr4,spn]

  for schdlr in schedulers:
      schdlr.execute()
      print('================================================================')
      print(schdlr.name)
      schdlr.results()
      

print("¡Bienvenido!")
print("Selecciona una opción")
while(error == 1):
  try:
    option = int(input("Ejecución con carga de procesos por defecto (1) o aleatoria (2) "))
    print("")
    if option == 1:
      create_default_load()
      error = 0
    elif option == 2:
      create_random_load()
      error = 0
    else:
      print("Ese número no es una opción válida, ingrese el valor de nuevo por favor")
  except ValueError as e1:
    print("Tipo de dato equivocado, ingrese el valor de nuevo por favor")

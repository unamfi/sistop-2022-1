from Proceso import Proceso
from FCFS import FCFS
def main():
    procesoA=Proceso(3,0,"A")
    procesoB=Proceso(5,1,"B")
    procesoC=Proceso(2,3,"C")
    procesoD=Proceso(5,9,"D")
    procesoE=Proceso(5,12,"E")
    AlgoritmoCola=FCFS(procesoA,procesoB,procesoC,procesoD,procesoE)
    AlgoritmoCola.run()
main()

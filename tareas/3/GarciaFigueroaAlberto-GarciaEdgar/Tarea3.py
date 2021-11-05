from Proceso import Proceso
from FCFS import FCFS
from RR import RR
from SPN import SPN
def main():
    procesoA=Proceso(0,3,"A")
    procesoB=Proceso(1,5,"B")
    procesoC=Proceso(3,2,"C")
    procesoD=Proceso(9,5,"D")
    procesoE=Proceso(12,5,"E")
    print("ALGORITMO FCFS")
    AlgoritmoCola=FCFS(procesoA,procesoB,procesoC,procesoD,procesoE)
    AlgoritmoCola.run()
    print("ALGORIMO RR")
    AlgorDos=RR(procesoA,procesoB,procesoC,procesoD,procesoE,1)
    AlgorDos.runRR()
    AlgorDos.listDiaf()
    print("ALGORIMO SPN")
    Algortres=SPN(procesoA,procesoB,procesoC,procesoD,procesoE)
    Algortres.run()
    Algortres.listDiaf()
main()

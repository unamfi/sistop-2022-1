import threading 
import sys
import random
import time
import Cliente, Empleado, Tienda, Proveedor

def main():
    tienda = Tienda("Tienda CU",10)
    prov  = Proveedor(1)
    emp1= Empleado(1)
    emp2= Empleado(2)
    emp3= Empleado(3)
    cliente1= Cliente(1)
    cliente2= Cliente(2)
    cliente3=Cliente(3)
    cliente4= Cliente(4)
    cliente3.pagar()
main()

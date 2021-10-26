import threading 
import sys
import random
import time
from CODE.Cliente import Cliente
from CODE.Empleado import Empleado
from CODE.Tienda import Tienda
from CODE.Proveedor import Proveedor
##import Cliente, Empleado, Tienda, Proveedor

def main():
    tienda = Tienda("Tienda CU",10)
    prov  = Proveedor(1)
    emp1= Empleado(1,tienda)
    emp2= Empleado(2,tienda)
    emp3= Empleado(3,tienda)
    cliente1= Cliente(1,tienda,emp2)
    cliente2= Cliente(2,tienda,emp2)
    cliente3=Cliente(3,tienda,emp2)
    cliente4= Cliente(4,tienda,emp2)
    cliente3.entrar()
main()

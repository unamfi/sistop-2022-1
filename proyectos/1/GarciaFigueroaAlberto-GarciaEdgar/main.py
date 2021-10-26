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
    tienda.abrir()
main()

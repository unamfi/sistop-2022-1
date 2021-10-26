import threading
import sys
import time
import random

class Tienda(object):
    #Declaramos los productos que se venden en la tienda
    productos = {1:["disfraz de Dracula","Disfraz de zombie","disfraz de hombre lobo","disfraz de momia"], 2:["chocolate","caramelo","milkyway","pikafresas"]}
    def __init__(self,nombre,aforo):
        self.nombre = nombre
        self.aforo = aforo

    #Dejamos pasar al cliente en cola
    def pass_client(self, cliente):
        if self.aforo<11:
            print("Bienvenido a la tienda cliente numero"+self.visita+" a la tienda")
            aforo =  self.aforo + 1
    


    
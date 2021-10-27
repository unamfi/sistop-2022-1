import threading
import time
import random

class Estacion:
    def __init__(self, nombre):
        self.e_adelante = None
        self.e_atras = None
        self.nombre = nombre
        self.estado_ida = threading.Semaphore(1) #Ocupado o no ocupado
        self.estado_regreso = threading.Semaphore(1) 

    def no_disponible(self, direccion): #1 ida 0 regreso
        if(direccion):
            self.estado_ida.acquire()
        else:
            self.estado_regreso.acquire()
            
    def disponible(self, direccion): #1 ida 0 regreso
        if(direccion):
            self.estado_ida.release()
        else:
            self.estado_regreso.release()
      
    def set_e_adelante(self,estacion_adelante):
        self.e_adelante = estacion_adelante
    
    def set_e_atras(self,estacion_atras):
        self.e_atras = estacion_atras
            
class Terminal:
    def __init__(self, nombre, e_adyasente): #Una terminal solo estara conectado con una estacion 
        self.nombre = "Terminal" 
        self.e_adyasente = e_adyasente
        
class Trenes(threading.Thread):
    def __init__(self, numero, direccion, estado, inicio_ruta):
        super().__init__(target=self.en_ruta, args=[])
        self.estado = estado
        self.funcionamiento = threading.Semaphore(1) #Arreglado o estropeado 
        self.numero = numero
        self.direccion = direccion
        self.ubicacion = inicio_ruta
    
    def en_ruta(self)->None:
        i = 0
        while(self.ubicacion.nombre != "Terminal"):
            self.ubicacion.no_disponible(self.direccion)
            print("Estoy en la estacion " + self.ubicacion.nombre, "\nSoy el tren numero: ", self.numero)
            time.sleep(random.random())
            # self.ubicacion.e_adelante.estado_ida.acquire()
            print("Siguiente estacion disponible, avanza tren", self.numero,"\n")
            #Se colocan despues de que hayamos pasado a la siguiente estacion 
            self.ubicacion.disponible(self.direccion)
            if(self.direccion):
                self.ubicacion = self.ubicacion.e_adelante
            else:
                self.ubicacion = self.ubicacion.e_atras
            
    def cambiar_direccion(self, direccion):
        self.direccion = direccion
          
    def print_tren(self):
        print("Tren numero: " + str(self.numero) + "\nDireccion: " + self.direccion + "\n¿Funciona? " + self.estado)
        print(type(self.numero), type(self.direccion), type(self.estado), type(self.funcionamiento))
          
          
class Menu:
    Estacion_1_L1 = Estacion("Periferico Norte")
    Terminal_1 = Terminal("T_L1_2",Estacion_1_L1)

    Estacion_2_L1 = Estacion("Dermatológico")
    Estacion_3_L1 = Estacion("Atemajac")
    Estacion_4_L1 = Estacion("Division del norte") 
    Estacion_5_L1 = Estacion("Avila Camacho")
    Estacion_6_L1 = Estacion("Mezquitan")
    Estacion_7_L1 = Estacion("Refugio")
    Estacion_8_L1 = Estacion("JUAREZ")
    Estacion_9_L1 = Estacion("Mexicaltzingo")
    Estacion_10_L1 = Estacion("Washinton")
    Estacion_11_L1 = Estacion("Santa Filomena")
    Estacion_12_L1 = Estacion("Unidad Deportiva")
    Estacion_13_L1 = Estacion("Urdaneta")
    Estacion_14_L1 = Estacion("18 de Marzo")
    Estacion_15_L1 = Estacion("Isla Raza")
    Estacion_16_L1 = Estacion("Patria sur")
    Estacion_17_L1 = Estacion("España")
    Estacion_18_L1 = Estacion("Tesoro")
    Estacion_19_L1 = Estacion("Periferico sur")
    Terminal_2 = Terminal("T_L1_2",Estacion_18_L1)

    Estacion_1_L1.set_e_adelante(Estacion_2_L1)
    Estacion_1_L1.set_e_atras(Terminal_1)

    Estacion_2_L1.set_e_adelante(Estacion_3_L1)
    Estacion_2_L1.set_e_atras(Estacion_1_L1)

    Estacion_3_L1.set_e_adelante(Estacion_4_L1)
    Estacion_3_L1.set_e_atras(Estacion_2_L1)

    Estacion_4_L1.set_e_adelante(Estacion_5_L1)
    Estacion_4_L1.set_e_atras(Estacion_3_L1)

    Estacion_5_L1.set_e_adelante(Estacion_6_L1)
    Estacion_5_L1.set_e_atras(Estacion_4_L1)

    Estacion_6_L1.set_e_adelante(Estacion_7_L1)
    Estacion_6_L1.set_e_atras(Estacion_5_L1)

    Estacion_7_L1.set_e_adelante(Estacion_8_L1)
    Estacion_7_L1.set_e_atras(Estacion_6_L1)

    Estacion_8_L1.set_e_adelante(Estacion_9_L1)
    Estacion_8_L1.set_e_atras(Estacion_7_L1)

    Estacion_9_L1.set_e_adelante(Estacion_10_L1)
    Estacion_9_L1.set_e_atras(Estacion_8_L1)

    Estacion_10_L1.set_e_adelante(Estacion_11_L1)
    Estacion_10_L1.set_e_atras(Estacion_9_L1)

    Estacion_11_L1.set_e_adelante(Estacion_12_L1)
    Estacion_11_L1.set_e_atras(Estacion_10_L1)

    Estacion_12_L1.set_e_adelante(Estacion_13_L1)
    Estacion_12_L1.set_e_atras(Estacion_11_L1)

    Estacion_13_L1.set_e_adelante(Estacion_14_L1)
    Estacion_13_L1.set_e_atras(Estacion_12_L1)

    Estacion_14_L1.set_e_adelante(Estacion_15_L1)
    Estacion_14_L1.set_e_atras(Estacion_13_L1)

    Estacion_15_L1.set_e_adelante(Estacion_16_L1)
    Estacion_15_L1.set_e_atras(Estacion_14_L1)

    Estacion_16_L1.set_e_adelante(Estacion_17_L1)
    Estacion_16_L1.set_e_atras(Estacion_15_L1)

    Estacion_17_L1.set_e_adelante(Estacion_18_L1)
    Estacion_17_L1.set_e_atras(Estacion_16_L1)

    Estacion_18_L1.set_e_adelante(Estacion_19_L1)
    Estacion_18_L1.set_e_atras(Estacion_17_L1)

    Estacion_19_L1.set_e_adelante(Terminal_2)
    Estacion_19_L1.set_e_atras(Estacion_18_L1)

    Estacion_1_L2 = Estacion("JUAREZ")
    Estacion_2_L2 = Estacion("Plaza Universidad")
    Estacion_3_L2 = Estacion("San Juan de Dios")
    Estacion_4_L2 = Estacion("Belisario Dominguez")
    Estacion_5_L2 = Estacion("Oblatos")
    Estacion_6_L2 = Estacion("Cristobal de Oñate")
    Estacion_7_L2 = Estacion("San Andrés")
    Estacion_8_L2 = Estacion("San Jacinto")
    Estacion_9_L2 = Estacion("La Aurora")
    Estacion_10_L2 = Estacion("Tetlán")
    Terminal_3 = Terminal("T_L2_3",Estacion_1_L2)
    Terminal_4 = Terminal("T_L2_4",Estacion_10_L2)

    Estacion_1_L2.set_e_adelante(Estacion_2_L2)
    Estacion_1_L2.set_e_atras(Terminal_3)

    Estacion_2_L2.set_e_adelante(Estacion_3_L2)
    Estacion_2_L2.set_e_atras(Estacion_1_L2)

    Estacion_3_L2.set_e_adelante(Estacion_4_L2)
    Estacion_3_L2.set_e_atras(Estacion_2_L2)

    Estacion_4_L2.set_e_adelante(Estacion_5_L2)
    Estacion_4_L2.set_e_atras(Estacion_3_L2)

    Estacion_5_L2.set_e_adelante(Estacion_6_L2)
    Estacion_5_L2.set_e_atras(Estacion_4_L2)

    Estacion_6_L2.set_e_adelante(Estacion_7_L2)
    Estacion_6_L2.set_e_atras(Estacion_5_L2)

    Estacion_7_L2.set_e_adelante(Estacion_8_L2)
    Estacion_7_L2.set_e_atras(Estacion_6_L2)

    Estacion_8_L2.set_e_adelante(Estacion_9_L2)
    Estacion_8_L2.set_e_atras(Estacion_7_L2)

    Estacion_9_L2.set_e_adelante(Estacion_10_L2)
    Estacion_9_L2.set_e_atras(Estacion_8_L2)

    Estacion_10_L2.set_e_adelante(Terminal_4)
    Estacion_10_L2.set_e_atras(Estacion_9_L2)
    
    while(True):
        print("Menu de simulador de metro con de Guadalajara con Lineas 1 y 2\n")
        opcion = input("Ingrese una opcion:\n1.-Iniciar simulacion\n2.-Salir\n")
        if(opcion == "1"):
            linea_opcion = input("Ingresa la linea en la que deseas iniciar tu simulador: ")
            tren_ida = input("Cuantos trenes deseas de ida: ")
            tren_regreso = input("Cuantos trenes deseas de regreso: ")
            if(linea_opcion == "1"):
                if(tren_ida == "2"):
                    tren_2 = Trenes(2, 1, "Funcional", Estacion_1_L1).start()
                if(tren_ida == "2" or tren_ida == "1"):
                    tren_1 = Trenes(1, 1, "Funcional", Estacion_1_L1).start()
                else:
                    print("Valor fuera del rango o incorrecto")
                if(tren_regreso == "2"):
                    tren_4 = Trenes(4, 0, "Funcional", Estacion_19_L1).start()
                if(tren_regreso == "2" or tren_regreso == "1"):    
                    tren_3 = Trenes(3, 0, "Funcional", Estacion_19_L1).start()
                else:
                    print("Valor fuera del rango o incorrecto")
            elif(linea_opcion == "2"):
                if(tren_ida == "2"):
                    tren_6 = Trenes(6, 1, "Funcional", Estacion_1_L2).start()
                if(tren_ida == "2" or tren_ida == "1"):
                    tren_5 = Trenes(5, 1, "Funcional", Estacion_1_L2).start()
                else:
                    print("Valor fuera del rango o incorrecto")
                if(tren_regreso == "2"):    
                    tren_8 = Trenes(8, 0, "Funcional", Estacion_10_L2).start()
                if(tren_regreso == "2" or tren_regreso == "1"):    
                    tren_7 = Trenes(7, 0, "Funcional", Estacion_10_L2).start()
                else:
                    print("Valor fuera del rango o incorrecto")
            else:
                print("Valor fuera del rango o incorrecto")
        
        elif(opcion=="2"):
            break
        else:
            print("Dato fuera de rango vuelva a ingresar los datos")
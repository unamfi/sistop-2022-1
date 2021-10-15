"""
- Elevador de la facultad (Hilo)
- Cada persona que utiliza el elevador es otro hilo
- 5 pisos en el edificio
    - Un usuario puede llamar al elevador desde cualquiera de los 5 pisos
    - Un usuario puede querer ir a cualquiera de los pisos
- El elevador tiene capacidad = 5 pasajeros
- Los usuarios prefieren esperar dentro del elevador
    - Esto quiere decir qwue si va para arriba pero el usuario desea ir 
    abajo, subira aunque el elevador vaya para arriba
"""

import threading
import random 
import time


#CONSTANTES
USUARIOS = 10
PISO_INF = 1
PISO_SUP = 5

llamadas = []
# mutex para proteger la escritura y lectura de la lista llamadas
mut_llamadas = threading.Semaphore(1)

# semafora para indicar si alguien llamo al elevador
mueve_elevador = threading.Semaphore(0)


class Elevador(threading.Thread):
    
    __CAPACIDAD = 5

    def __init__(self, piso_inf, piso_sup):
        super().__init__(target=self.funcionamiento, args=[])
        self.piso = piso_inf
        self.__PISO_INF = piso_inf
        self.__PISO_SUP = piso_sup

        # lista que almacena a los usuarios que usan el elevador
        self.usuarios_usando_elevador = []
        
        # mutex para proteger la escritura  y lectura de la lista usuarios_usando_elevador
        self.mut_usuarios_elevador = threading.Semaphore(1)

    def funcionamiento(self) -> None:
        global mueve_elevador, llamadas, mut_llamadas

        direccion = None # determina si va hacia arriba o hacia abajo
        usuario_mas_antiguo = None

        while True:
            #print(len(self.usuarios_usando_elevador))

            # El elevador se duerme en lo que espera una llamada
            mueve_elevador.acquire()

            # Posteriormente se libera para mantener un balance
            # pues cuando un usuario baja del elevador se libera 
            # de la llamada inicial que hizo el usuario y en cada 
            # iteracion se estaria bloqueando continuamente, creando un desbalance
            mueve_elevador.release()
            
            print("Elevador en piso %d" % self.piso)

            index = 0

            self.mut_usuarios_elevador.acquire()

            # Comprueba si un usuario ha llegado a su destino
            for i in self.usuarios_usando_elevador:
                if i[1] == self.piso:
                    print("     U%s: Llegue a mi destino, adios" % i[2])
                    self.usuarios_usando_elevador.pop(index)
                    mueve_elevador.acquire()
                index += 1

            self.mut_usuarios_elevador.release()


            mut_llamadas.acquire()

            # Comprueba si algun usuario se quiere subir al elevador
            index = 0
            for i in llamadas:
                # Si el elevador llego a su capacidad de usuarios continua con su recorrido
                if len(self.usuarios_usando_elevador) == self.__CAPACIDAD:
                    print("     E: ya no se puede subir nadie mas, vamonos")
                    break
                elif self.piso == i[0]:
                    usuario_actual = llamadas.pop(index)
                    self.usuarios_usando_elevador.append(usuario_actual)
                    print("     U%s: Subiendo al elevador" % usuario_actual[2])
                index += 1
            
            mut_llamadas.release()

            # Determinamos la direccion hacia el elevador
            # direccion = -1, el elevador baja
            # direccion = 1, el elevadro sube
            if self.piso ==  self.__PISO_SUP:
                direccion = -1
            elif self.piso == self.__PISO_INF:
                direccion = 1

            # En el caso de estar en algun piso intermedio determina la direccion
            # dandole prioridad a la llamada mas antigua
            elif len(self.usuarios_usando_elevador) != 0:
                usuario_mas_antiguo = self.usuarios_usando_elevador[0]
                #print("             Usuario mas antiguo", usuario_mas_antiguo)
                if usuario_mas_antiguo[1] - usuario_mas_antiguo[0] < 0:
                    direccion = -1
                else:    
                    direccion = 1

            print("     E: Moviendome de piso")
            time.sleep(1)
            #print(              "Usuarios usando elevador: ", self.usuarios_usando_elevador)
            self.piso += direccion
            

class Usuario(threading.Thread):

    def __init__(self, id, num_piso):
        super().__init__(target=self.llamar_elevador, name=id)
        self.num_piso = num_piso

    # Determina el piso hacia donde va un Usuario aleatoriamente
    def hacia_que_piso(self) -> int:
        global PISO_SUP, PISO_INF

        # 1 = arriba, 0 = abajo
        if self.num_piso == PISO_INF:
            direccion = 1
            return random.randint(PISO_INF + 1, PISO_SUP)
        elif self.num_piso == PISO_SUP: 
            direccion = 0
            return random.randint(PISO_INF, PISO_SUP - 1)
        else:
            direccion = random.randint(0, 1)
            if direccion == 1:
                return random.randint(self.num_piso + 1, PISO_SUP)
            return random.randint(PISO_INF, self.num_piso - 1)
                
    def llamar_elevador(self) -> None:
        global mut_llamadas, llamadas, mueve_elevador

        #Bloqueamos llamadas para que ningun otro hilo escriba en el
        mut_llamadas.acquire()

        llamadas.append([self.num_piso, self.hacia_que_piso(), self.getName()])
        
        mut_llamadas.release()

        #Se hace una llamada al elevador
        mueve_elevador.release()

#Inicializa el hilo del elevador
Elevador(PISO_INF, PISO_SUP).start()

#Inicializa los hilos de los usuaros
for i in range(USUARIOS):
    time.sleep(random.random())
    Usuario(i + 1, random.randint(PISO_INF, PISO_SUP)).start()


#Prueba para probar que el elevador pasa a un estado de espera hasat que llegue un nuevo usuario
#time.sleep(40)
#Usuario(11, random.randint(PISO_INF, PISO_SUP)).start()
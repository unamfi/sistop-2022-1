# -*- coding: utf-8 -*-
from threading import Semaphore


#Señalizaciones para refrescar la pantalla
sigHilos = Semaphore(0)
sigInterfaz = Semaphore(0)

#Torniquete para el lanzamiento de proceso de cortesanos
pausa = Semaphore(0)

#Visualizacion del escenario
grafico = [""]*8
grafico[0] = "                      "
grafico[1] = "o=====================o"
grafico[2] = "|       |     |       "
grafico[3] = "|       |_____|      |"
grafico[4] = "|                    |"
grafico[5] = "|                    |"
grafico[6] = "o=  =================o"
grafico[7] = ""

# Problemas de Sincronización

Autores:
  - García Figueroa Munguía Alberto
  - García Gutiérrez Edgar Cristóbal
## Problema resuelto
Problema de Santa Claus
## Lenguaje y entorno que se empleó
En este ejercicio, usamos el lenguaje de programación (`Python`), y el entorno 
que usamos para desarrollar fue Visual Studio Code y la terminal.
Para ejecutar el programa, bastará con solo ir a la ruta de la [carpeta](./SantaProblem.py)
y posteriormente ejecutar el comando 
   $ python SantaProblem.py
## La estrategia de sincronización (mecanismo / patrón) que nos funcionó
Para resolver el ejercicio, los mecanismos que se usaron fueron los Semáforos y el mutex. Esto debido
a que la naturaleza del problema implicaba compartir recursos (en este caso contadores) para que
los hilos pudieran trabajar entre si sin afectar la ejecución del programa.
Los Semáforos nos ayudan a evitar la "colisión de los hilos" y el Mutex nos ayuda a administrar 
correctamente el uso de los recursos.
## ¿Implementamos algun refinamiento?
No, en este caso en nuestro desarrollo no vimos necesario implementar algun refinamiento
## Dudas acerca del desarrollo del problema.
Durante el desarrollo del programa, algunas de las dudas que nos surgieron fueron resueltas viendo la
documentación oficial de Python
Sin embargo, no pudimos implementar que el programa fuera finito, esto es, que nuestro programa
no termina su ejecución al menos que detengamos el proceso directamente con el sistema operativo.
Además, no pudimos enseñar correctamente algunos mensajes en la consola debido a que en ese mismo instante
de tiempo los hilos imprimían sus estados.
## Referencias.
  - Synchronization Primitives — Python 3.10.0 documentation. (2021). 
    Python Docs. https://docs.python.org/3/library/asyncio-sync.html
  - UNIVERSIDAD NACIONAL JORGE BASADRE GROHMANN FACULTAD DE INGENIERIA E.A.P. INGENIARIA EN INFORAMTICA Y SISTEMAS MONITORES: "PROBLEMA DE SANTA CLAUS 
   Recuperado 14 de octubre de 2021, de 
  https://docplayer.es/57576521-Universidad-nacional-jorge-basadre-grohmann-facultad-de-ingenieria-e-a-p-ingeniaria-en-inforamtica-y-sistemas-monitores-problema-de-santa-claus.html
# Tarea 3. Sistemas Operativos
- Manzanares Peña Jorge Luis
- Salazar Domínguez Jesús Eduardo


## Requisitos para la ejecución
El programa fue desarrollado en el lenguaje de programación Python en su versión 3.8. Para su ejecución, se deberá contar con esas especificaciones. Además, se necesita instalar la biblioteca *numpy*.

Una vez que se cumplió con estos requisitos, se podrá ejecutar el programa simplemente con el siguiente comando en la terminal:

	$python3 main.py

El programa permite al usuario elegir entre una ejecución por default (con los parámetros de los procesos idénticos a los vistos en el ejemplo de clase) o una ejecución con procesos aleatorios. Una vez que se selecciona una opción, el programa mostrará los resultados en la terminal, dividiéndolos según el algoritmo al que pertenezcan.


## Ejemplos de una ejecución exitosa

Ejecución de la opción default:

	¡Bienvenido!
	Selecciona una opción
	Ejecución con carga de procesos por defecto (1) o aleatoria (2) 1
	
	Los procesos son:
	ID:  A , Tiempo de llegada:  0 , Tiempo de ejecución:  3
	ID:  B , Tiempo de llegada:  1 , Tiempo de ejecución:  5
	ID:  C , Tiempo de llegada:  3 , Tiempo de ejecución:  2
	ID:  D , Tiempo de llegada:  9 , Tiempo de ejecución:  5
	ID:  E , Tiempo de llegada:  12 , Tiempo de ejecución:  5
	================================================================
	First Come First Serve (FCFS)
	T:  6.2
	E:  2.2
	P:  1.74
	Esquema de ejecución:
	AAABBBBBCCDDDDDEEEEE
	================================================================
	Round Robin (RR) con quantum = 1
	T:  7.6
	E:  3.6
	P:  1.98
	Esquema de ejecución:
	ABABCABCBDBDEDEDEDEE
	================================================================
	Round Robin (RR) con quantum = 4
	T:  7.2
	E:  3.2
	P:  1.88
	Esquema de ejecución:
	AAABBBBCCBDDDDEEEEDE
	================================================================
	Shortest Process Next (SPN)
	T:  5.6
	E:  1.6
	P:  1.32
	Esquema de ejecución:
	AAACCBBBBBDDDDDEEEEE

Ejecución de la opción aleatoria:

	¡Bienvenido!
	Selecciona una opción
	Ejecución con carga de procesos por defecto (1) o aleatoria (2) 2

	Los procesos son:
	ID:  B , Tiempo de llegada:  0 , Tiempo de ejecución:  3
	ID:  E , Tiempo de llegada:  1 , Tiempo de ejecución:  2
	ID:  C , Tiempo de llegada:  3 , Tiempo de ejecución:  8
	ID:  A , Tiempo de llegada:  6 , Tiempo de ejecución:  7
	ID:  D , Tiempo de llegada:  7 , Tiempo de ejecución:  9
	================================================================
	First Come First Serve (FCFS)
	T:  10.6
	E:  4.8
	P:  1.74
	Esquema de ejecución:
	BBBEECCCCCCCCAAAAAAADDDDDDDDD
	================================================================
	Round Robin (RR) con quantum = 1
	T:  14.6
	E:  8.8
	P:  2.31
	Esquema de ejecución:
	BEBECBCADCADCADCADCADCADCADDD
	================================================================
	Round Robin (RR) con quantum = 4
	T:  12.2
	E:  6.4
	P:  1.95
	Esquema de ejecución:
	BBBEECCCCAAAACCCCDDDDAAADDDDD
	================================================================
	Shortest Process Next (SPN)
	T:  10.6
	E:  4.8
	P:  1.74
	Esquema de ejecución:
	BBBEECCCCCCCCAAAAAAADDDDDDDDD
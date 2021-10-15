# Problema: El cruce del rio



#Autor

	- Moreno Peralta Angel Eduardo



# Lenguaje y entorno de desarrollo



Con tener python es suficiente para poder usar el archivo llamado Tarea2.py para esto hay que ingresar a la carpeta de MorenoEduardo y ejecutar:

	$python Tarea2.py



# Estrategia de Sincronización



Utilice para su desarrollo semáforos y mutex.



# Refinamientos



No llevé a cabo ningún refinamiento.



# Dudas



- A pesar de que el programa puede parar la impresión del movimiento de la balsa, el programa no sale del proceso, y no deja la terminal libre, así que es necesario cerrar la terminal para poder "ejecutar" nuestro programa. (Esto sucediendo en Windows)
- El programa se detiene con un control + c y se sale de su ejecución con el siguiente control + c, me imagino que pasa esto debido a que mato el proceso, pero no libero los hilos que uso durante la ejecución, tendría que ver en donde liberar los hilos sin que se rompa el programa antes. (Caso Linux)
- La ejecución en Linux y Windows en el caso de random es diferente, en Windows los valores varian mucho más que en Linux.

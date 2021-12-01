# Tarea 4. Sistemas Operativos
- Manzanares Peña Jorge Luis
- Salazar Domínguez Jesús Eduardo


## Requisitos para la ejecución
El programa fue desarrollado en el lenguaje de programación Python en su versión 3.8. También se utizó el módulo `re` para expresiones regulares.

```shell
	$ python3 interface.py
```

El programa inicia su ejecución mostrándole al usuario los posibles comandos que puede emplear. Si en aglún momento se ingresa una línea incorrecta o se comete otro tipo de error en la ejecución, entonces el programa imprimirá la naturaleza del mismo en la consola.

Cabe resaltar que los contenidos de nuestros archivos comienzan en la posición cero. Por ejemplo, si se tiene la siguiente cadena: `ABCDEFGHIJ`, entonces `A` está en la posición `0`, `B` está en la posición `1` y así sucesivamente hasta llegar a la letra `J`, que está en la posición `9`. Además, la longitud total de la cadena es  `10`.


## Ejemplos de una ejecución exitosa
```shell
    ---------------------------------BIENVENIDO--------------------------------------------

    Los posibles comandos a emplear son los siguientes:
    dir → Muestra el directorio
    open <arch> <modo> → Especifica que operaremos con el archivo de
    nombre "arch", empleando el modo especificado. Entrega un
    descriptor de archivo numérico
    close <descr> → Termina una sesión de trabajo con el archivo
    referido por el descriptor indicado. Después de un close,
    cualquier intento por usar ese archivo entregará error.
    read <descr> <longitud> → Lee la cantidad de bytes especificada
    write <descr> <longitud> <datos> → Escribe la cantidad de
    bytes especificada en el archivo "descr", guardando los datos indicados como parámetro
    seek <descr> <ubicación> → Salta a la ubicación del archivo especificada del
    archivo.
    quit → Detiene la ejecución de la simulación
    
    » dir
    arch1 [20 bytes]
    arch2 [15 bytes]
    arch3 [25 bytes]
    arch4 [10 bytes]
    » open arch1 R
    Archivo abierto (R) -> 1
    » read 1 20
    ABCDEFGHIJ0123456789
    » write 1 5 solar
    El archivo está en modo de escritura
    » close 1
    » open arch2 W
    Archivo abierto (W) -> 2
    » read 2 5
    El archivo está en modo de escritura
    » read
    El comando ingresado es inválido
    » write 7 saludos
    El comando ingresado es inválido
    » write 1 7 saludos
    El descriptor ya está cerrado
    » write 2 7 saludos
    » close 2
    » open arch2 A
    Archivo abierto (A) -> 3
    » read 3 10
    Intentaste acceder a una posición mayor al tamaño del archivo
    » read 3 7
    saludos
    » seek 3 5
    » write 3 4 1234
    » seek 3 0
    » read 3 11
    Intentaste acceder a una posición mayor al tamaño del archivo
    » read 3 7
    salud12
    » read 3 9
    salud1234
    » quit
```


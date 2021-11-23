# Implementando la semántica de archivos

	Tarea creada: 2021.11.23
	Entrega: 2021.11.30

Les presenté a la interfaz por medio de la cual utilizamos a los
archivos como una *emulación de unidad de cinta*: Los archivos se
presentan al programador de aplicaciones como si fueran un flujo de
caracteres que podemos ir _pasando_ por una cabeza de
lectura/escritura. A semejanza de la unidad de cinta, podemos pedirle
al sitema que adelante o retroceda a una posición específica
(`seek()`).

Los archivos, además, se estructuran en *directorios*. Un directorio
es una estructura de datos que permite tener acceso a varios archivos,
organizados _de alguna manera_ (que no hemos abordado aún) en un medio
de almacenamiento.

## ¿Y esta tarea?

Para esta tarea, les pido que –sin meternos en la complejidad de cómo
representar esto en un medio de almacenamiento persistente–
implementen un sistema interactivo con la interfaz lógica de
manipulación de un directorio y los archivos que éste
contiene.

Ojo: **No les estoy pidiendo que manejen archivos reales**. Manejen
alguna estructura que *no se grabe nunca* a almacenamiento
real. Pueden ser cadenas en la memoria.

Ejemplifico un poco lo que espero ver:

### 1. Listar el directorio, _abrir_ uno de los pseudoarchivos

Al entrar al programa, debe presentarnos un directorio con el cual
interactuar. Les pido que este directorio esté _pre-cargado_ con
algunos _pseudo-archivos_. Les pido que la interfaz explique
brevemente cómo utilizarse, algo por el estilo de:

    $ ./tarea4
	dir → Muestra el directorio
	open <arch> <modo> → Especifica que operaremos con el archivo de
	         nombre "arch", empleando el modo especificado. Entrega un
			 descriptor de archivo numérico.
	close <descr> → Termina una sesión de trabajo con el archivo
	         referido por el descriptor indicado. Después de un close,
			 cualquier intento por usar ese archivo entregará error.
    read <descr> <longitud> → Lee la cantidad de bytes especificada
	write <descr> <longitud> <datos» → Escribe la cantidad de
	         bytes especificada, guardando loss datos indicados
			 como parámetro.
	seek <descr> <ubicacion> → Salta a la ubuicación especificada del
	         archivo.
	quit → Detiene la ejecucin de la simulación
    ‣ dir
	arch1 [15441 bytes]    arch2 [200 bytes]      otro_mas [2048 bytes]

Los pseudo-archivos pueden abrirse en cuatro modos:

- `Lectura` (R): Permite recuperar información del archivo. El archivo
  _no puede ser modificado_.
- `Escritura` (W): descarta toda la información que contenga; abre el
  archivo para sólo escritura, y establece su tamaño a 0
- `Modificación` (A): Permite operaciones de lectura y escritura. Si se
  escribe más allá del fin de archivo, éste crecerá.

Puedo elegir alguno de estos archivos para trabajar, o crear uno
nuevo:

    ‣ open arch1 R
	Archivo abierto (R) → 1
	‣ open otro_mas A
	Archivo abierto (A) → 2
	‣ open arch2 W
	Archivo abierto (W) → 3

`open` me entrega un descriptor de archivo que utilizaré para
indicarle a todas las llamadas sucesivas a qué pseudoarchivo me estoy
refiriendo.

    ‣ read 1 60
	012345678901234567890123456789012345678901234567890123456789

Lee los siguientes 60 caracteres del descriptor solicitado

	‣ seek 1 1500

Salta a la ubicación especificada en el archivo en cuestión

	‣ write 1 5 Hola!
	Error: El archivo 'arch1' está abierto para lectura únicamente

¡Tengan cuidado de implementar verificaciones! El uso que damos a los
archivos debe ser congruente con el que especificamos.

	‣ seek 2 70
	‣ write 2 5 Hola!
	‣ seek 2 65
	‣ read 2 10
    VeamoHola!

Había algún texto en el archivo #2 a partir del caracter 65, pero los
caracters 70-75 fueron sobreescritos por «Hola!»

    ‣ close 3
	0
	‣ write 3 Acá seguimos
	Error: El identificador #3 ya está cerrado.


Ojo: Consideren que están simulando un dispositivo de acceso
secuencial, de longitud definida. Si su pseudoarchivo `4` es la cadena
`0123456789ABCDEF` y hacemos un `seek 4 5`, y damos `write 4 2 OK`, el
archivo resultante será `012OK56789ABCDEF`. La longitud de la cadena
debe coincidir con la declarada: `write 2 5 Saluditos` no debe
escribir nada, sino que regresar un error.

Espero que con esta interacción resulte suficiente para entender lo
que busco que hagan. Les repito, _no les estoy pidiendo_ que manipulen
archivos de verdad, sino que alguna estructura en la memoria (volátil)
del sistema.

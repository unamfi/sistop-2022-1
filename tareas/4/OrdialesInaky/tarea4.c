/*
  Elaborado por: Iñaky Ordiales Caballero
  

  IMPLEMENTANDO LA SEMÁNTICA DE ARCHIVOS

  Tarea 4 de la materia de sistemas operativos, Facultad de Ingeniería, UNAM.
  Instrucciones: Implementar un sistema interactivo con la interfaz lógica de
                 manipulación de un directorio y los archivos que éste contiene.

  Asignatura: "Sistemas Operativos".
  Grupo: 6
  Profesor: I. Gunnar Eyal Wolf Iszaevich
  Semestre: 2022-1


 */


// Bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Declaracion de estructuras

struct Archivo{
  int size;
  char* nombre;
  char* texto;
};

struct Directorio{
  char nombre[20];
  int archivos;
  struct Archivo** directorio;
};


// Declaración de funciones.
void rojo();
void verde();
void amarillo();
void azul();
void rosa();
void cyan();
void blanco();
void normal();
void comando();
void inicializarPseudoArchivos(char* nombre, char* contenido, struct Directorio* directorio);
void imprimirAyuda();
void imprimirDir(struct Directorio* directorio);
int estaAbierto(char* arch, struct Directorio* directorio);
int abiertoDescr(char* descr, struct Directorio* directorio);
void abrirArchivo(char* arch, char* modo, struct Directorio* directorio);
void cerrarArchivo(char* descr, struct Directorio* directorio);
void leerArchivo(char* descr, char* longitud, struct Directorio* directorio);
void escribirArchivo(char* descr, char* longitud, char* data, struct Directorio* directorio);
void posicionarArchivo(char* descr, char* ubicacion, struct Directorio* directorio);
void liberarMemoria(struct Directorio* directorio, char* buffer);


// Declaración de variables globales.
// Se tienen 6 archivos cada uno con:
// edo. abierto | descriptor | lugar directorio | modo | ubicacion
// La variable datos será el control del estado de los archivos.
// Tomará dinámicamente el espacio de un arreglo de 5 enteros por cada
// archivo del directorio. Es una matriz, pero se manejará como vector.
int* datos;


// A continuación se definen las funiones utilizadas:

// Colores de impresión.
void rojo(){
  printf("\033[0;31m");
}
void verde(){
  printf("\033[0;32m");
}
void amarillo(){
  printf("\033[0;33m");
}
void azul(){
  printf("\033[0;34m");
}
void rosa(){
  printf("\033[0;35m");
}
void cyan(){
  printf("\033[0;36m");
}
void blanco(){
  printf("\033[0;37m");
}
void normal(){
  printf("\033[0m");
}


// Mensaje de error por número de argumentos.
void comando(char* cadena){
  printf("\nDemasiados argumentos para el comando ");
  rosa();
  printf("%s ", cadena);
  normal();
  printf("...");
}


// Aquí se inicializan dinámicamente los pseudoarchivos de simulación.
// y se agregan a nuestra estructura directorio que los "contiene" (su dirección realemente).
void inicializarPseudoArchivos(char *nombre, char *contenido, struct Directorio* directorio){

  struct Archivo* arch;
  int tamNombre = strlen(nombre);
  int tamContenido = strlen(contenido);
  
  arch = malloc(sizeof(struct Archivo));
  arch->nombre = malloc(tamNombre*sizeof(char));
  strcpy(arch->nombre, nombre);
  arch->texto = malloc(tamContenido*sizeof(char));
  strcpy(arch->texto, contenido);
  arch->size = tamContenido;

  directorio->archivos++;
  int i = directorio->archivos-1;
  if(directorio->archivos == 1){
    directorio->directorio = malloc(sizeof(struct Archivo*));
    datos = malloc(directorio->archivos*5*sizeof(int));
    datos[i*5+0]=0;
    datos[i*5+1]=i+1;
    datos[i*5+2]=-1;
    datos[i*5+3]=0;
    datos[i*5+4]=0;
  }else{
    directorio->directorio = (struct Archivo**) realloc(directorio->directorio, (directorio->archivos)*sizeof(struct Archivo**));
    datos = realloc(datos, directorio->archivos*5*sizeof(int));
    datos[i*5+0]=0;
    datos[i*5+1]=i+1;
    datos[i*5+2]=-1;
    datos[i*5+3]=0;
    datos[i*5+4]=0;
  }
  directorio->directorio[(directorio->archivos)-1] = arch;
  
}


// Se imprimen las instrucciones del programa con formato especial y dedicado.
void imprimirAyuda(){

  blanco();
  printf("\n Terminal InOr, los comandos disponibles son:\n\n");
  rosa();
  printf("   ayuda");
  normal();
  printf("   :  muestra la información actual, es decir los comandos\n              básicos de la terminal.\n");
  rosa();
  printf("\n   salir");
  normal();
  printf("   :  libera memoria y cierra el programa, los cambios en\n              archivos se pierden.\n");
  rosa();
  printf("\n   dir");
  normal();
  printf("     :  muestra los archivos del directorio actual junto\n              con su tamaño.\n");
  rosa();
  printf("\n   open");
  cyan();
  printf("  <arch> <modo>");
  normal();
  printf(" :  Abre un archivo en el modo especificado.\n                          Es necesario abrir un archivo antes de \n                          poder trabajar con él. Le asigna y muestra\n                          un descriptor para el archivo.\n");
  blanco();
  printf("         [arch] ");
  normal();
  printf("- nombre del archivo.\n");
  blanco();
  printf("         [modo] ");
  normal();
  printf("- 'R' lectura, 'W' escritura, 'A' modificación.\n");
  rosa();
  printf("\n   close");
  cyan();
  printf(" <descr>");
  normal();
  printf(" :  Cierra un archivo con el cual se estaba trabajando.\n                    Una vez cerrado ya no se podrá leer, escribir o \n                    posicionar hasta que se vuelva a abrir y obtenga\n                    un nuevo descriptor.\n");
  blanco();
  printf("         [descr] ");
  normal();
  printf("- el descriptor del archivo abierto que se cerrará.\n");
  rosa();
  printf("\n   read");
  cyan();
  printf("  <descr> <longitud>");
  normal();
  printf(" :  lee la cantidad de bytes especificada\n                               del archivo al que hacer referencia el\n                               descriptor. El archivo necesita haber \n                               sido abierto en modo lectura.\n");
  blanco();
  printf("         [descr] ");
  normal();
  printf("- el descriptor del archivo abierto que se leerá.\n");
  blanco();
  printf("         [longitud] ");
  normal();
  printf("- la cantidad de bytes a leer a partir de la\n                          ubicación de lectura (inicio al abrirlo).\n");
  rosa();
  printf("\n   write");
  cyan();
  printf(" <descr> <longitud> <datos>");
  normal();
  printf(" :  Escribe una cantidad determinada de\n                   bits en el archivo al que hace referencia el descriptor.\n                   Dependiendo si fue abierto en modo escritura o en modo\n                   modificación, se borrará el contenido antiguo o sólo se\n                   le añadirá.\n");
  blanco();
  printf("         [descr] ");
  normal();
  printf("- el descriptor del archivo abierto donde se escribirá.\n");
  blanco();
  printf("         [longitud] ");
  normal();
  printf("- la cantidad de bytes que se escribirán a partir de\n                      la ubicación de escritura (modo 'A') o al inicio\n                      (modo 'W').\n");
  blanco();
  printf("         [datos] ");
  normal();
  printf("- la información a escribir, debe coincidir la longitud.\n");
  rosa();
  printf("\n   seek");
  cyan();
  printf("  <descr> <ubicacion>");
  normal();
  printf(" :  Despalza la ubicación de lectura o escritura de\n                                un archivo al que hace referencia el descriptor.\n");
  blanco();
  printf("         [descr] ");
  normal();
  printf("- el descriptor del archivo abierto donde se cambiará la\n                   ubicación.\n");
  blanco();
  printf("         [ubicacion] ");
  normal();
  printf(" - la posición en la que se establecerá la lectura o \n                        escritura. No puede exceder el tamaño del archivo.\n");
  azul();
  printf("\n   Ctrl+C");
  normal();
  printf("  :  aborta la ejecución de la terminal InOr (programa).\n");
  
}


// Se imprimen los archivos del directorio.
// Su nombre, tamaño y de estar abiertos, modo y descriptor.
void imprimirDir(struct Directorio* directorio){
  int i, j;
  int n = directorio->archivos;
  int suma=0;

  blanco();
  printf("\n  InOr/%s/", directorio->nombre);
  normal();
  for(i=0; i<n; i++){
    printf("\n\t- ");
    cyan();
    printf("%s\t ", directorio->directorio[i]->nombre);
    normal();
    printf("[");
    amarillo();
    printf("%d bytes",  directorio->directorio[i]->size);
    normal();
    printf("]");
    //printf(" %d %d %d %d %d", datos[i*5+0], datos[i*5+1], datos[i*5+2], datos[i*5+3], datos[i*5+4]);
    for(j=0; j<n; j++){
      if(datos[j*5+2]==i){
	if(datos[j*5+0]==1){
	  if(datos[j*5+3]==1){
	    printf(" 'R'  descr: %d", j+1);
	  }else if(datos[j*5+3]==2){
	    printf(" 'W'  descr: %d", j+1);
	  }else if(datos[j*5+3]==3){
	    printf(" 'A'  descr: %d", j+1);
	  }
	}
      }
    }
    suma+=directorio->directorio[i]->size;
  }
  blanco();
  printf("\n  Total: %d archivos,    %d [bytes]", n, suma);
  normal();
}

// Regresa la posicion del archivo en el directorio si no está abierto,
// -1 si ya está abierto, -2 si no existe.
int estaAbierto(char* arch, struct Directorio* directorio){

  int n = directorio->archivos;
  int i;
  int posDir=-1;

  for(i=0; i<n; i++){
    if(!strcmp(arch, directorio->directorio[i]->nombre)){
      posDir = i;
      i=n;
    }
  }

  if(posDir == -1){
    return -1000;
  }else{
    for(i=0; i<n; i++){
      if(datos[i*5+2]==posDir){
	return -(i+1);
      }
    }
    return posDir;
  }
  
}


// Averigua si para un descriptor dado, existe un archivo correspondiente.
// Regresa 0 si no existe, o el mismo descriptor si sí existe.
int abiertoDescr(char* descr, struct Directorio* directorio){
  int n = directorio->archivos;
  int i = atoi(descr);
  
  if(i<1 || i>n){
    printf("\nEl descriptor no es válido.");
    return 0;
  }else{
    if(datos[(i-1)*5+0]==0){
      printf("\nNo hay ningun archivo abierto con ese descriptor.");
      return 0;
    }else{
      return i;
    }
  }
  
}


// Se abre un archivo en la modalidad especificada y se le asigna un
// descriptor que se muestra en pantalla.
void abrirArchivo(char* arch, char* modo, struct Directorio* directorio){
  
  int i;
  int modoArch;

  int abierto = estaAbierto(arch, directorio);

  if(abierto==-1000){
    if(!strcmp(modo, "R") || !strcmp(modo, "r")){
      modoArch = 1;
    }else if(!strcmp(modo, "W") || !strcmp(modo, "w")){
      modoArch = 2;
    }else if(!strcmp(modo, "A") || !strcmp(modo, "a")){
      modoArch = 3;
    }else{
      printf("\nEl parámetro '%s' no es válido para abrir el archivo.", modo);
      return;
    }
    inicializarPseudoArchivos(arch, "", directorio);
    datos=realloc(datos, directorio->archivos*5*sizeof(int));
    for(i=0; i<directorio->archivos; i++){
      if(datos[i*5+0]==0){
	datos[i*5+0]=1;
	datos[i*5+2]=(directorio->archivos)-1;
	datos[i*5+3]=modoArch;
	datos[i*5+4]=0;
	printf("\nArchivo %s creado en modo '%s' con el descriptor %d", arch, modo, datos[i*5+1]);
	return;
      }
    }
  }else if(abierto < 0){
    printf("\nEl archivo ya está abierto con el descriptor: %d",-1* abierto);
    return;
  }else{
    if(!strcmp(modo, "R") || !strcmp(modo, "r")){
      modoArch = 1;
    }else if(!strcmp(modo, "W") || !strcmp(modo, "w")){
      modoArch = 2;
    }else if(!strcmp(modo, "A") || !strcmp(modo, "a")){
      modoArch = 3;
    }else{
      printf("\nEl parámetro '%s' no es válido para abrir el archivo.", modo);
      return;
    }
    for(i=0; i<directorio->archivos; i++){
      if(datos[i*5+0]==0){
	datos[i*5+0]=1;
	datos[i*5+2]=abierto;
	datos[i*5+3]=modoArch;
	datos[i*5+4]=0;
	printf("\nArchivo %s abierto en modo '%s' con el descriptor %d", arch, modo, datos[i*5+1]);
	return;
      }
    } 
  }
  
}


// Se cierra un archivo a partir del descriptor. Es decir, el descriptor
// deja de señalar al archivo y se desmarca el bit de ocupado para el descriptor.
void cerrarArchivo(char* descr, struct Directorio* directorio){

  int i = abiertoDescr(descr, directorio);
  if(i){
    printf("\nSe cerró el archivo %s con descriptor %d", directorio->directorio[datos[(i-1)*5+2]]->nombre, i);
    datos[(i-1)*5+0]=0;
    datos[(i-1)*5+2]=-1;
    datos[(i-1)*5+3]=0;
    datos[(i-1)*5+4]=0;
    return;
  }else{
    return;
  }
  
}


// Se lee un archivo abierto para lectura a partir del posicionamiento (seek) dado.
// No puede leer más del tamaño del archivo. 
void leerArchivo(char* descr, char* longitud, struct Directorio* directorio){

  int i = abiertoDescr(descr, directorio);
  int largo = atoi(longitud);
  int j;

  if(i){
    if( (largo < 1) || (largo+datos[(i-1)*5+4] > directorio->directorio[datos[(i-1)*5+2]]->size) ){
      printf("\nLa longitud no puede ser menor a 1 o mayor al tamaño del archivo.");
      return;
    }else{
      if(datos[(i-1)*5+3] == 1){
	printf("\n");
	for(j=datos[(i-1)*5+4]; j<(largo+datos[(i-1)*5+4]); j++){
	  printf("%c", directorio->directorio[datos[(i-1)*5+2]]->texto[j]);
	}
	return;
      }else{
	printf("\nEl archivo del descriptor no está en modo lectura 'R'.");
	return;
      }
    }
  }else{
    return;
  }
}


// En esta función se escribe en los archivos, según la modalidad en la que estén abiertos.
// Si están abiertos para escritura 'W' se borra el contenido antiguo y se escribe el nuevo.
// Si están abiertos para modificación 'A' se agrega al archivo según dónde esté el
// posicionamiento (seek). Además se checa que la longitud declarada sea igual a la de los
// datos que se quieren escribir, si no coincide no se escribe por seguridad.
void escribirArchivo(char* descr, char* longitud, char* data, struct Directorio* directorio){

  int i = abiertoDescr(descr, directorio);
  int largo = atoi(longitud);
  int tamContenido = strlen(data);
  int j;

  if(!i){
    printf("\nEl archivo del descriptor no está en modo escritura 'W' o modificación 'A'.");
    return;
  }else  if(largo!=tamContenido){
    printf("\n Declara: %d , lee: %d  s: %s", largo, tamContenido, data);
    printf("\nLos datos de entrada no tienen la longitud declarada, por seguridad no se escribirá.");
    return;
  }else{
    if(datos[(i-1)*5+3] == 2){ // 'W'
      free(directorio->directorio[datos[(i-1)*5+2]]->texto);
      directorio->directorio[datos[(i-1)*5+2]]->texto = malloc(tamContenido*sizeof(char));
      strcpy(directorio->directorio[datos[(i-1)*5+2]]->texto, data);
      directorio->directorio[datos[(i-1)*5+2]]->size = largo;
      printf("\nLos datos han sido sobre escritos para el archivo del descriptor %d.", i);
      return;
    }else if(datos[(i-1)*5+3] == 3){ // 'A'
      if( (datos[(i-1)*5+4]+largo) > directorio->directorio[datos[(i-1)*5+2]]->size ){
	directorio->directorio[datos[(i-1)*5+2]]->texto = realloc(directorio->directorio[datos[(i-1)*5+2]]->texto, (datos[(i-1)*5+4]+largo)*sizeof(char));
	directorio->directorio[datos[(i-1)*5+2]]->size = datos[(i-1)*5+4]+largo;
	for(j=datos[(i-1)*5+4]; j < datos[(i-1)*5+4]+largo; j++){
	  directorio->directorio[datos[(i-1)*5+2]]->texto[j] = data[j-datos[(i-1)*5+4]];
	}
	datos[(i-1)*5+4] +=largo;
	printf("\nLos datos han sido modificados para el archivo del descriptor %d.", i);
	return;
      }else{
	for(j=datos[(i-1)*5+4]; j < datos[(i-1)*5+4]+largo; j++){
	  directorio->directorio[datos[(i-1)*5+2]]->texto[j] = data[j-datos[(i-1)*5+4]];
	}
	printf("\nLos datos han sido modificados para el archivo del descriptor %d.", i);
	return;
      }
    }else{
      printf("\nEl archivo del descriptor no está en modo escritura 'W' o modificación 'A'.");
      return;
    }
  }  
}


// Esta función corresponde al seek y posiciona la lectura/escritura en una ubicación determinada.
void posicionarArchivo(char* descr, char* ubicacion, struct Directorio* directorio){
  int i = abiertoDescr(descr, directorio);
  int ubi = atoi(ubicacion);
  
  if(i){
    if( (ubi < 0) || (ubi > directorio->directorio[datos[(i-1)*5+2]]->size) ){
      printf("\nLa ubicación de posicionamiento no puede ser menor a 0 o mayor al tamaño del archivo.");
      return;
    }else{
      if(datos[(i-1)*5+3]==2){
	printf("\nEl archivo del descriptor está en modo 'W' por lo que la ubicación de escritura siempre es 0.");
	return;
      }else{
	datos[(i-1)*5+4]=ubi;
	printf("\nEl lector/escritor para el archivo del descriptor %d se posicióno en %d", i, ubi);
	return;
      }
    }
  }else{
    return;
  }
}


// Se libera la memoria dinámica solicitada durante la ejecución para los archivos, directorio y buffer.
void liberarMemoria(struct Directorio* directorio, char *buffer){

  int i;
  int n = directorio->archivos;
  struct Archivo* aux;

  free(datos);
  
  for(i=0; i<n; i++){
    aux = directorio->directorio[i];
    free(aux->nombre);
    free(aux->texto);
    free(aux);
  }
  free(directorio->directorio);
  free(buffer);
}


// En el main se establece el flujo general del programa. La mayor parte se encuentra dentro de
// un ciclo while que se rompe para acabar la ejecución cuando se recibe el comando salir.
int main(){

  int salir=0;
  int aux, contador;
  char *buffer;
  char *tokenAux;
  char *token[4];
  size_t bufsize = 256;
  struct Directorio directorio;
  
  // Apartamos el tamaño para la entrada
  buffer = malloc(bufsize*sizeof(char));

  
  // Inicialización directorio, psuedo-archivos y datos control.
  strcpy(directorio.nombre, "Tarea4");
  directorio.archivos = 0;
  
  inicializarPseudoArchivos("ProyectoFinal", "Este archivo contiene información del proyecto final", &directorio);
  inicializarPseudoArchivos("PoemaI", "Por qué razón o sinrazón llora la lluvia su alegría?    - Pablo Neruda", &directorio);
  inicializarPseudoArchivos("PoemaII","Por qué se suicidan las hojas cuando se sienten amarillas?    - Pablo Neruda", &directorio);
  inicializarPseudoArchivos("Clasificado", "Los rumores son ciertos, la tierra es plana .... CUIDADO con esta info", &directorio);
  inicializarPseudoArchivos("Passwords", "Gmail - CruzAzul9, Office - LaMaquinaCeleste, Banco - arribaCruzAzul", &directorio);
  inicializarPseudoArchivos("Matematicas", "2x2 = 2^2 = 2+2 = 3", &directorio);

  
  // Preparamos la consola
  system("clear");
  azul();
  printf("\n\n ~~~~~~~~~~~~~~~~~~~ Terminal InOR ~~~~~~~~~~~~~~~~~~~~\n\n");
  printf(" ** ingrese 'ayuda' para ver los comandos \n\n");
  normal();

  verde();
  printf("InOr  ~>> ");
  normal();
  printf("ayuda\n");
  imprimirAyuda();

  // Mientras el usuario no ingrese el comando salir, se queda en la consola.
  while(!salir){

    // Impresión de la señalización de la consola.
    verde();
    printf("\n\n\nInOr  ~>> ");
    normal();

    // Obtención de la línea ingresada
    getline(&buffer, &bufsize, stdin);
    aux = strlen(buffer);
    buffer[aux-1]='\0'; // cambio '\n' por '\0'.

    contador = 0;
    tokenAux=strtok(buffer, " ");

    // Se separa la entrada por sus espacios en tokens.
    while (tokenAux != NULL && contador<4){
      token[contador]=tokenAux;
      if(contador==2){
	tokenAux=strtok(NULL, "\n");
      }else{
	tokenAux=strtok(NULL, " ");
      }
      contador++;
    }

    // Lógica de operación de comandos.
    if (contador>0){
      if(!strcmp(token[0], "salir")){
	if(contador==1){
	  salir++;
	}else{
	  comando("salir");
	}
      }else if(!strcmp(token[0], "dir")){
	if(contador==1){
	  imprimirDir(&directorio);
	}else{
	  comando("dir");
	}
      }else if(!strcmp(token[0], "open")){
	if (contador!=3){
	  printf("\nNúmero incorrecto de argumentos para el comando:");
	  cyan();
	  printf(" open <arch> <modo>");
	}else{
	  abrirArchivo(token[1], token[2], &directorio);
	}
      }else if(!strcmp(token[0], "close")){
	if (contador!=2){
	  printf("\nNúmero incorrecto de argumentos para el comando:");
	  cyan();
	  printf(" close <descr>");
	}else{
	  cerrarArchivo(token[1], &directorio);
	}
      }else if(!strcmp(token[0], "read")){
	if (contador!=3){
	  printf("\nNúmero incorrecto de argumentos para el comando:");
	  cyan();
	  printf(" read <descr> <longitud>");
	}else{
	  leerArchivo(token[1], token[2], &directorio);
	}
      }else if(!strcmp(token[0], "write")){
	if (contador!=4){
	  printf("\nNúmero incorrecto de argumentos para el comando:");
	  cyan();
	  printf(" write <descr> <longitud> <datos>");
	}else{
	  escribirArchivo(token[1], token[2], token[3], &directorio);
	}
      }else if(!strcmp(token[0], "seek")){
	if (contador!=3){
	  printf("\nNúmero incorrecto de argumentos para el comando:");
	  cyan();
	  printf(" seek <descr> <ubicacion>");
	}else{
	  posicionarArchivo(token[1], token[2], &directorio);
	}
      }else if(!strcmp(token[0], "ayuda")){
	imprimirAyuda();
      }else{
	printf("\nNo se reconoce el comando: %s", token[0]);
	printf("\nLas opciones son: ");
	rosa();
	printf("salir");
	normal();
	printf(", ");
	rosa();
        printf("dir");
        normal();
        printf(", ");
	rosa();
        printf("open");
        normal();
        printf(", ");
	rosa();
        printf("close");
        normal();
        printf(", ");
	rosa();
        printf("read");
        normal();
        printf(", ");
	rosa();
        printf("write");
        normal();
        printf(", ");
	rosa();
        printf("seek");
        normal();
        printf(".");
      }
    }
    
  }

  // Se libera la memoria asignada dinámicamente.
  liberarMemoria(&directorio, buffer);
  
  printf("\n\n\n\n        . . .   ");
  printf("\033[0;35m");
  printf("C e r r a n d o   ");
  printf("\033[0m");
  printf(". . .\n\n\n\n\n");
  
  return 0;
}

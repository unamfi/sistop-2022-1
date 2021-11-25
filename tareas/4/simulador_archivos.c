#include <stdio.h> 
#include <stdlib.h>


typedef struct{
    char* nombre;
    char* apertura;
    char* datos; 
} Archivo;

#define TAM_STRING 1024
#define NOMBRE_ARCH "informacion_uso.txt"


int main() {

    printf("Simulador de sistema de archivos: \n\n");

    FILE* f = fopen(NOMBRE_ARCH, "r");

    if(!f) {
        printf("ERROR: no se ha encontrado el archivo '%s'", NOMBRE_ARCH);
        fclose(f);
        exit(1);
    }

    char texto[TAM_STRING];

    while(fgets(texto, TAM_STRING, f)) {
        puts(texto);
    }

    fclose(f);

    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// ESTRUCTURA PROCESO                                                           

struct Proceso{
  char nombre;
  int llegada;     // El tiempo en el que llega                                 
  int requerido;   // Su tiempo de ejecución necesario                          
  int inicio;      // Cuando llega a formarse                                   
  int final;       // Cuando termina ejecución                                  
  int tiempo;      // El tiempo que existió (final - llegada)                   
  int espera;      // El tiempo que esper sin ejecutarse (tiempo - requerido)   
  float por;       // Tiemo tardado entre tiempo requerido                      
};


// Funciones prototipos

void fifo(struct Proceso*, int num);
void roundRobin(struct Proceso*, int, int);
void shortNext(struct Proceso*, int, int);
void highNext(struct Proceso*, int);
void fb(struct Proceso*, int, int, int);
void selfRR(struct Proceso*, int, int, int);



// Algoritmos de administración de procesos                                     

void fifo(struct Proceso *lista, int num){

  int tiempo = 0;
  int requerido;
  int i=-1;
  int proceso=0;
  struct Proceso actual;
  int aux = 1;

  printf("FIFO:  ");

  while(aux){

    // Si no hay proceso                                                        
    if(!proceso && lista[i+1].llegada<=tiempo){
      i++;
      actual = lista[i];
      actual.inicio = tiempo;
      proceso = 1;
    }

    printf("%c", actual.nombre);

    tiempo++;

    // Si ya acabó                                                              
    if((tiempo-actual.inicio)==actual.requerido){
      proceso=0;
      actual.final = tiempo-1;
      actual.tiempo = actual.final - actual.llegada;
      actual.espera = actual.tiempo - actual.requerido;
      actual.por = (float)actual.tiempo/actual.requerido;

      if(i==num-1)
	aux=0;

    }
  }
  printf("\n");

}

void roundRobin(struct Proceso *lista, int num, int q){


}

void shortNext(struct Proceso *lista, int num, int q){


}

void highPNext(struct Proceso *lista, int num){


}

void fb(struct Proceso *lista, int num, int n, int q){


}

void selfRR(struct Proceso *lista, int num, int a, int b){


}



int main() {

  struct Proceso listaEjemplo[5];
  struct Proceso* lista1, lista2, lista3;

  listaEjemplo[0].nombre = 'A';
  listaEjemplo[0].llegada = 0;
  listaEjemplo[0].requerido = 3;
  listaEjemplo[1].nombre = 'B';
  listaEjemplo[1].llegada = 1;
  listaEjemplo[1].requerido = 5;
  listaEjemplo[2].nombre = 'C';
  listaEjemplo[2].llegada = 3;
  listaEjemplo[2].requerido = 2;
  listaEjemplo[3].nombre = 'D';
  listaEjemplo[3].llegada = 9;
  listaEjemplo[3].requerido = 5;
  listaEjemplo[4].nombre = 'E';
  listaEjemplo[4].llegada = 12;
  listaEjemplo[4].requerido = 5;

  int i;
  float promedio=0;
  for (i=0; i<5; i++){
    promedio+=listaEjemplo[i].requerido;
  }
  promedio /= i;

  fifo(listaEjemplo, 5);




  return 0;
}

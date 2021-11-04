#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// ESTRUCTURA PROCESO                                                           

struct Proceso{
  char nombre;
  int llegada;     // El tiempo en el que llega                                 
  int requerido;   // Su tiempo de ejecución necesario                          
  int inicio;      // Cuando llega a formarse                                   
  int termina;     // Cuando termina ejecución                                  
  int tiempo;      // El tiempo que existió (final - llegada)                   
  int espera;      // El tiempo que esper sin ejecutarse (tiempo - requerido)   
  float por;       // Tiemo tardado entre tiempo requerido                      
};


// Funciones prototipos

void fifo(struct Proceso*, int);
void roundRobin(struct Proceso*, int, int);
void shortNext(struct Proceso*, int, int);
void highNext(struct Proceso*, int);
void fb(struct Proceso*, int, int, int);
void selfRR(struct Proceso*, int, int, int);
void imprimirCarga(struct Proceso*, int);
void imprimirResultados(struct Proceso*, int);
void simulacion(struct Proceso*, int);


// Algoritmos de administración de procesos                                     

void fifo(struct Proceso *procesos, int num){

  struct Proceso *actual;
  int tiempo = 0;
  int i=-1;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;

  printf("\n\n\n FIFO:  ");

  while(!fin){

    // Si no hay proceso y quedan más se asigna uno nuevo
    if(!ocupado && procesos[i+1].llegada<=tiempo){
      i++;
      actual = &procesos[i];
      actual->inicio = tiempo;
      ocupado = 1;
    }

    // imprime nombre de trabajo
    printf("%c", actual->nombre);

    tiempo++;

    // Si ya acabó se calculan resultados individuales
    if((tiempo-actual->inicio)==actual->requerido){
      ocupado = 0;
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo/actual->requerido;
      // checa si es el último proceso
      if(i==num-1)
	fin=1;

    }
  }
  printf("\n");

}

void roundRobin(struct Proceso *procesos, int num, int q){

  struct Proceso *actual;
  int tiempo = 0;
  int i=-1;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;

  printf("\n\n\n FIFO:  ");

  while(!fin){

    // Si no hay proceso y quedan más se asigna uno nuevo
    if(!ocupado && procesos[i+1].llegada<=tiempo){
      i++;
      actual = &procesos[i];
      actual->inicio = tiempo;
      ocupado = 1;
    }

    // imprime nombre de trabajo
    printf("%c", actual->nombre);

    tiempo++;

    // Si ya acabó se calculan resultados individuales
    if((tiempo-actual->inicio)==actual->requerido){
      ocupado = 0;
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo/actual->requerido;
      // checa si es el último proceso
      if(i==num-1)
	fin=1;

    }
  }
  printf("\n");

}

void shortNext(struct Proceso *procesos, int num, int q){


}

void highPNext(struct Proceso *procesos, int num){


}

void fb(struct Proceso *procesos, int num, int n, int q){


}

void selfRR(struct Proceso *procesos, int num, int a, int b){


}


void imprimirCarga(struct Proceso *procesos, int num){

  float promedio = 0;
  
  printf(  "\n               Tiempo        Tiempo");
  printf(  "\n  PROCESO    de llegada    requerido (t)\n");
  printf(  " ______________________________________________\n");
  for(int i=0; i<num; i++){
    printf("     %c           %2d             %2d\n", procesos[i].nombre, procesos[i].llegada, procesos[i].requerido);
    promedio += procesos[i].requerido;
  }
  promedio = (float)promedio/num;
  printf(" ______________________________________________\n");
  printf(" PROMEDIO                       %2.2f\n", promedio);

  
}

void imprimirResultados(struct Proceso *procesos, int num){

  float promedioT = 0;
  float promedioE = 0;
  float promedioP = 0;

  printf(  "\n  PROCESO  INICIO   FIN      T      E      P\n");
  printf(  " ______________________________________________\n");
  for(int i=0; i<num; i++){
    printf("      %c       %2d     %2d     %2d     %2d    %2.2f\n", procesos[i].nombre, procesos[i].inicio, procesos[i].termina, procesos[i].tiempo, procesos[i].espera, procesos[i].por);
    promedioT+=procesos[i].tiempo;
    promedioE+=procesos[i].espera;
    promedioP+=procesos[i].por;
  }
  promedioT = (float)promedioT/num;
  promedioE = (float)promedioE/num;
  promedioP = (float)promedioP/num;
  printf(  " ______________________________________________\n");
  printf(  "  PROMEDIOS                %2.2f   %2.2f   %2.2f\n");
  
}


void simulacion(struct Proceso *procesos, int num){

  imprimirCarga(procesos, num);
  fifo(procesos, num);
  imprimirResultados(procesos, num);

}


int main() {

  struct Proceso ejemplo[5];
  struct Proceso* lista1, lista2, lista3;

  printf("\n\n ~ ~ ~ Bienvenido al simulador de algoritmos de planificacion. ~ ~ ~\n\n");
  printf(" Se presentan 4 simulaciones para los algoritmos, la vista en\n");
  printf(" clase y otras 3 aleatorias de 5, 10 y 15 procesos respectivamente.\n\n");
  
  ejemplo[0].nombre = 'A';
  ejemplo[0].llegada = 0;
  ejemplo[0].requerido = 3;
  ejemplo[1].nombre = 'B';
  ejemplo[1].llegada = 1;
  ejemplo[1].requerido = 5;
  ejemplo[2].nombre = 'C';
  ejemplo[2].llegada = 3;
  ejemplo[2].requerido = 2;
  ejemplo[3].nombre = 'D';
  ejemplo[3].llegada = 9;
  ejemplo[3].requerido = 5;
  ejemplo[4].nombre = 'E';
  ejemplo[4].llegada = 12;
  ejemplo[4].requerido = 5;

  printf("\n---------------------------------------------------------------------");
  printf("\n Tabla de procesos, caso 1:\n");
  simulacion(ejemplo, 5);


  printf("\n\n");
  
  return 0;
}

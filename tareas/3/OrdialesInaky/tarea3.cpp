/*     TAREA 3 de la asignatura de Sistemas Operativos

       " Algoritmos de administración de procesos "

       Elaborado por: Ordiales Caballero, Iñaky
       Noviembre del 2021.
       

       El código tiene todos los algoritmos y funcionan adecuadamente, pero en ocasiones
       marca un segmentation fault en el FB que no pude desbuguear, por lo que no 
       se ejecutara este algoritmo para evitar problemas. 
       Al ejecutar el código te muestra la información en tablas conforme se va simulando.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <cmath>

using namespace std;


// ESTRUCTURA PROCESO                                                           

struct Proceso{
  char nombre;
  int llegada;     // El tiempo en el que llega                                 
  int requerido;   // Su tiempo de ejecución necesario
  int ejecutado;   // Tiempo ejecutado
  int inicio;      // Cuando llega a formarse                                   
  int termina;     // Cuando termina ejecución                                  
  int tiempo;      // El tiempo que existió (final - llegada)                   
  int espera;      // El tiempo que esper sin ejecutarse (tiempo - requerido)   
  float por;       // Tiempo tardado entre tiempo requerido                      
};


// Estrctura para comparar ordenar por el proceso más corto

struct CompareShort{
  bool operator()(Proceso* const& p1, Proceso* const& p2){
    return ((p1->requerido) > (p2->requerido));
  }
};


// Funciones prototipos

void fifo(struct Proceso*, int);
void roundRobin(struct Proceso*, int, int);
void shortNext(struct Proceso*, int);
void fb(struct Proceso*, int, int, int);
void selfRR(struct Proceso*, int, int, int);
void imprimirCarga(struct Proceso*, int);
void imprimirResultados(struct Proceso*, int);
void simulacion(struct Proceso*, int);



// Algoritmos de administración de procesos                                     

// First in first out, la idea es tener una cola y se forman
// para ser procesados como van llegando, de inicio hasta
// que acaben.
void fifo(struct Proceso *procesos, int num){

  struct Proceso *actual=NULL;
  queue<struct Proceso*> cola;
  int tiempo = 0;
  int contadorLlegada = 0;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;

  printf("\n\n\n FIFO:  ");

  // Si llegó un proceso en el tiempo 0 -> se agrega a la fila.
  if(procesos[contadorLlegada].llegada == tiempo){
    procesos[contadorLlegada].ejecutado = 0;
    cola.push(&procesos[contadorLlegada]);
    contadorLlegada++;
  }
  
  while(!fin){
    
    // Si no hay proceso y quedan más se asigna uno nuevo
    if(!ocupado && cola.size()!=0){
      actual = cola.front();
      cola.pop();
      ocupado = 1;
      if(actual->ejecutado == 0){
	actual->inicio = tiempo;
      }
    }

    // imprime proceso en ejecucion
    if(ocupado){
      printf("%c", actual->nombre);
      actual->ejecutado++;
    }
    tiempo++;

    // Si ya llegó un proceso -> se agrega a la fila.
    if(contadorLlegada<num && procesos[contadorLlegada].llegada <= tiempo){
      procesos[contadorLlegada].ejecutado = 0;
      cola.push(&procesos[contadorLlegada]);
      contadorLlegada++;
    }
    
    // Si ya acabó se calculan resultados individuales
    if(actual!=NULL && actual->ejecutado == actual->requerido){
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo / actual->requerido;
      actual = NULL;
      ocupado = 0;
      
      // checa si es el último proceso
      if(contadorLlegada == num && cola.size()==0){
	fin=1;
      }
    }
    
  }
  
  printf("\n");

}


// La idea es que todos los procesos de la fila tienen un tiempo
// predeterminado de ejecución y después se tienen que volver a
// formar al final. Así hasta acabar.
void roundRobin(struct Proceso *procesos, int num, int q){

  struct Proceso *actual=NULL;
  queue<struct Proceso*> cola;
  int tiempo = 0;
  int contadorLlegada = 0;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;
  int contadorQ = 1;
  

  printf("\n\n\n RR con q=%d:  ", q);

  
  // Si llegó un proceso en el tiempo 0 -> se agrega a la fila.
  if(procesos[contadorLlegada].llegada == tiempo){
    procesos[contadorLlegada].ejecutado = 0;
    cola.push(&procesos[contadorLlegada]);
    contadorLlegada++;
  }
  
  while(!fin){

    // Si no hay proceso
    if(!ocupado && cola.size()!=0){
      actual = cola.front();
      cola.pop();
      ocupado = 1;
      if(actual->ejecutado == 0){
	actual->inicio = tiempo;
      }
    }

    // imprime nombre de trabajo
    if(ocupado){
      printf("%c", actual->nombre);
      actual->ejecutado++;
    }
    tiempo++;

    // Si ya llegó el proceso -> se agrega a la fila.
    if(contadorLlegada<num && procesos[contadorLlegada].llegada == tiempo){
      procesos[contadorLlegada].ejecutado = 0;
      cola.push(&procesos[contadorLlegada]);
      contadorLlegada++;
    }
    
    // Si ya acabó se calculan resultados individuales
    if(actual!=NULL && actual->ejecutado == actual->requerido){
      ocupado = 0;
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo/actual->requerido;
      actual=NULL;
      contadorQ=0;
      
      // checa si es llegaron todos y ya no hay en la cola
      if(contadorLlegada == num && cola.size()==0){
	fin=1;
      }
    }else if(contadorQ==q){ // si se le acabo el tiempo, se forma
      ocupado = 0;
      if(actual!=NULL){
	cola.push(actual);
      }
      contadorQ = 0;
    }
    
    contadorQ++;
  }
  
  printf("\n");

}


// Aquí se trata de que se ejecute el proceso más corto que esté formado
// en la fila. Una vez termine se vuelve a checar la fila por el proceso
// más corto. Para su implementación usé una priority queue que se acomoda
// de tiempo requerido menor a mayor. Y cada que llega un proceso éste
// se inserta según le corresponde en la fila.
void shortNext(struct Proceso *procesos, int num){

  struct Proceso *actual=NULL;
  priority_queue<Proceso*, vector<Proceso*>, CompareShort> cola;
  int tiempo = 0;
  int contadorLlegada = 0;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;

  printf("\n\n\n SPN:  ");

  // Si llegó un proceso en el tiempo 0 -> se agrega a la fila.
  if(procesos[contadorLlegada].llegada == tiempo){
    procesos[contadorLlegada].ejecutado = 0;
    cola.push(&procesos[contadorLlegada]);
    contadorLlegada++;
  }
  
  while(!fin){
    
    // Si no hay proceso y quedan más se asigna uno nuevo
    if(!ocupado && cola.size()!=0){
      actual = cola.top();
      cola.pop();
      ocupado = 1;
      if(actual->ejecutado == 0){
	actual->inicio = tiempo;
      }
    }

    // imprime nombre de trabajo
    if(ocupado){
      printf("%c", actual->nombre);
      actual->ejecutado++;
    }
    tiempo++;

    // Si ya llegó el proceso -> se agrega a la fila.
    if(contadorLlegada<num && procesos[contadorLlegada].llegada <= tiempo){
      procesos[contadorLlegada].ejecutado = 0;
      cola.push(&procesos[contadorLlegada]);
      contadorLlegada++;
    }
    
    // Si ya acabó se calculan resultados individuales
    if(actual!=NULL && actual->ejecutado == actual->requerido){
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo / actual->requerido;
      actual = NULL;
      ocupado = 0;
      
      // checa si es el último proceso
      if(contadorLlegada == num && cola.size()==0){
	fin=1;
      }
    }
    
  }
  
  printf("\n");
  
}


// La lógica de fb me parece que está bien onstruída y en ocasiones corre
// sin problemas, pero en otras marca un segmentation fault y aborta
// la ejecución. Traté de entender por qué pasaba esto, pero no pude.
// Su idea es que hay varias colas y después de determinados quantums
// de ejecución, un proceso es degradado a una cola de menor prioridad.
// Para esto utilize un arreglo de colas y un contador de quantums, si
// se le terminaban los quantums y le faltaba ejecución, se degradaba.
void fb(struct Proceso *procesos, int num, int n, int q){
  
  struct Proceso *actual=NULL;
  queue<struct Proceso*> colas[6];
  int tiempo = 0;
  int contadorLlegada = 0;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;
  int contadorQ = 1;
  int valorQ;
  int numCola = 0;

  if(q){
    printf("\n\n\n FB con n=%d y q=2^nQ:  ", n);
  }else{
    printf("\n\n\n FB con n=%d y q=1:  ", n);
  }
  
  // Si llegó un proceso en el tiempo 0 -> se agrega a la fila.
  if(procesos[contadorLlegada].llegada == tiempo){
    procesos[contadorLlegada].ejecutado = 0;
    colas[0].push(&procesos[contadorLlegada]);
    contadorLlegada++;
  }
  
  while(!fin){

    // Si no hay proceso se buscan en las colas
    if(!ocupado){
      for(int i=0; i<6; i++){
	if(colas[i].size()>0){
	  numCola=i;
	  i=6;
	}
      }
      actual = colas[numCola].front();
      colas[numCola].pop();
      ocupado = 1;
      if(q){
	valorQ = pow(2, numCola);
      }else{
	valorQ=1;
      }
      if(actual->ejecutado == 0){
	actual->inicio = tiempo;
      }
    }

    // imprime nombre de trabajo
    if(ocupado){
      printf("%c", actual->nombre);
      actual->ejecutado++;
    }
    tiempo++;

    // Si ya llegó el proceso -> se agrega a la fila.
    if(contadorLlegada<num && procesos[contadorLlegada].llegada == tiempo){
      procesos[contadorLlegada].ejecutado = 0;
      colas[0].push(&procesos[contadorLlegada]);
      contadorLlegada++;
    }
    
    // Si ya acabó se calculan resultados individuales
    if(actual!=NULL && actual->ejecutado == actual->requerido){
      ocupado = 0;
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo/actual->requerido;
      actual=NULL;
      contadorQ=0;
      
      // checa si es llegaron todos y ya no hay en la cola
      if(contadorLlegada == num){
	fin = 1;
	for(int i = 0; i<6; i++){
	  if(colas[i].size()>0){
	    fin = 0;
	  }
	}
      }
    }else if(contadorQ==valorQ){
      ocupado = 0;
      if(numCola<5){
	colas[numCola+1].push(actual);
      }else{
	colas[numCola].push(actual);
      }
      contadorQ = 0;
    }
    
    contadorQ++;
  }
  
  printf("\n");

}


// Selfish round robin trata de que se tienen dos colas, una de procesos
// nuevos y una de procesos "aceptados". Cada una tiene una proporción
// de crecimiento de su prioridad, entonces hasta que los nuevos no lleguen
// a la prioridad de los aceptados no podrán entrar a ejecución.
// Se favorece al que se está ejecutando para no perder el control hasta que
// un nuevo lo iguale o rebase en prioridad. Los aceptados no lo pueden
// quitar porque su prioridad crece al mismo ritmo.
// Para la implementación use colas con llaves de prioridad para el proceso.
void selfRR(struct Proceso *procesos, int num, int a, int b){

  struct Proceso *actual=NULL, *aux=NULL;
  queue<pair<int, struct Proceso*>> colaNuevos, colaAceptados;
  int tiempo = 0;
  int contadorLlegada = 0;
  // fin -> bandera se acabó carga
  int fin = 0;
  // ocupado -> procesador está libre
  int ocupado = 0;
  int contadorQ = 1;
  int q = 1;
  int prioridad=0;
  int auxPrioridad=0;
  int sNuevos;
  int sAceptados;
  int min=0;
  
  printf("\n\n\n SRR con q=1, a=%d y b=%d:  ", a, b);
  
  
  while(!fin){
    
    // Si ya llegó el proceso -> se agrega a la fila.
    if(contadorLlegada<num && procesos[contadorLlegada].llegada == tiempo){
      procesos[contadorLlegada].ejecutado = 0;
      if(colaAceptados.size() == 0){
	colaAceptados.push(make_pair(0, &procesos[contadorLlegada]));
      }else{
	colaNuevos.push(make_pair(0,&procesos[contadorLlegada]));
      }
      contadorLlegada++;
    }
    
    
    // Si no hay proceso
    if(!ocupado && colaAceptados.size()!=0){
      actual = colaAceptados.front().second;
      prioridad = colaAceptados.front().first;
      colaAceptados.pop();
      ocupado = 1;
      if(actual->ejecutado == 0){
	actual->inicio = tiempo;
      }
    }
    
    // imprime nombre de trabajo
    if(ocupado){
      printf("%c", actual->nombre);
      actual->ejecutado++;
      prioridad+=b;
    }
    tiempo++;


    // Aumenta prioridades y promueve procesos.
    sAceptados = colaAceptados.size();
    if(sAceptados == 0){
      if(actual!=NULL){
	min = prioridad;
      }else{
	min = 0;
      }
    }else{
      min = 100;
    }
    for(int i=0; i<sAceptados; i++){
      aux = colaAceptados.front().second;
      auxPrioridad = colaAceptados.front().first+b;
      if(auxPrioridad<min){
	min = auxPrioridad;
      }
      colaAceptados.pop();
      colaAceptados.push(make_pair(auxPrioridad, aux));
    }
    sNuevos = colaNuevos.size();
    for(int i=0; i<sNuevos; i++){
      aux = colaNuevos.front().second;
      auxPrioridad = colaNuevos.front().first+a;
      colaNuevos.pop();
      colaNuevos.push(make_pair(auxPrioridad, aux));
    }
    for(int i=0; i<sNuevos; i++){
      aux = colaNuevos.front().second;
      auxPrioridad = colaNuevos.front().first;
      colaNuevos.pop();
      if(auxPrioridad>=min){
	colaAceptados.push(make_pair(auxPrioridad, aux));
      }else{
	colaNuevos.push(make_pair(auxPrioridad, aux));
      }
    }

    // Si ya acabó se calculan resultados individuales
    if(actual!=NULL && actual->ejecutado == actual->requerido){
      ocupado = 0;
      actual->termina = tiempo;
      actual->tiempo = actual->termina - actual->llegada;
      actual->espera = actual->tiempo - actual->requerido;
      actual->por = (float)actual->tiempo/actual->requerido;
      actual=NULL;
      contadorQ=0;
      
      // checa si es llegaron todos y ya no hay en la cola
      if(contadorLlegada == num && colaAceptados.size()==0){
	fin=1;
      }
      
    }else if(contadorQ==q && ocupado){
      ocupado = 0;
      colaAceptados.push(make_pair(prioridad, actual));
      contadorQ = 0;
    }
    
    contadorQ++;
    
  }
  
  printf("\n");
  
}


// Se imprime en pantalla los datos iniciales de los procesos a simular
void imprimirCarga(struct Proceso *procesos, int num){

  float promedio = 0;
  int total;
  
  printf(  "\n               Tiempo        Tiempo");
  printf(  "\n  PROCESO    de llegada    requerido (t)\n");
  printf(  " ______________________________________________\n");
  for(int i=0; i<num; i++){
    printf("     %c           %2d             %2d\n", procesos[i].nombre, procesos[i].llegada, procesos[i].requerido);
    promedio += procesos[i].requerido;
  }
  total = promedio;
  promedio = (float)promedio/num;
  printf(" ______________________________________________\n");
  printf(" TOTAL                           %d\n", total);
  printf(" PROMEDIO                       %2.2f\n", promedio);
  printf(  "\n **************************************************\n");
  
}

// Se imprime en pantalla los resultados de los datos a simular.
void imprimirResultados(struct Proceso *procesos, int num, float *prome, int idxProme){

  float promedioT = 0;
  float promedioE = 0;
  float promedioP = 0;

  printf(  "\n  PROCESO    INICIO    FIN      T       E      P\n");
  printf(  " ___________________________________________________\n");
  for(int i=0; i<num; i++){
    printf("      %c       %3d     %3d     %3d     %3d    %2.2f\n", procesos[i].nombre, procesos[i].inicio, procesos[i].termina, procesos[i].tiempo, procesos[i].espera, procesos[i].por);
    promedioT+=procesos[i].tiempo;
    promedioE+=procesos[i].espera;
    promedioP+=procesos[i].por;
  }
  promedioT = (float)promedioT/num;
  promedioE = (float)promedioE/num;
  promedioP = (float)promedioP/num;
  prome[idxProme]=promedioT;
  prome[idxProme+1]=promedioE;
  prome[idxProme+2]=promedioP;
  printf(  " ___________________________________________________\n");
  printf(  "  PROMEDIOS                   %2.2f   %2.2f   %2.2f\n", promedioT, promedioE, promedioP);
  
}


// Se simulan los diferentes algoritmos con una carga específica.
// y se muestran resultados.
void simulacion(struct Proceso *procesos, int num){

  float prome[21];
  
  imprimirCarga(procesos, num);
  fifo(procesos, num);
  imprimirResultados(procesos, num, prome, 0);
  roundRobin(procesos, num, 1);
  imprimirResultados(procesos, num, prome, 3);
  roundRobin(procesos, num, 4);
  imprimirResultados(procesos, num, prome, 6);
  shortNext(procesos, num);
  imprimirResultados(procesos, num, prome, 9);
  //fb(procesos, num, 1, 0);
  //imprimirResultados(procesos, num, prome, 12);
  //fb(procesos, num, 1, 1);
  //imprimirResultados(procesos, num, prome, 15);
  selfRR(procesos, num, 2, 1);
  imprimirResultados(procesos, num, prome, 18);

  printf("\n\n\n\n COMPARATIVA DE ALGORITMOS.\n\n");
  printf(" FIFO:\t\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[0], prome[1], prome[2]);
  printf(" RR1 :\t\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[3], prome[4], prome[5]);
  printf(" RR4 :\t\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[6], prome[7], prome[8]);
  printf(" SPN :\t\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[9], prome[10], prome[11]);
  //printf(" FB1 :\t\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[12], prome[13], prome[14]);
  //printf(" FB2^n:\t\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[15], prome[16], prome[17]);
  printf(" SRR-21:\tT: %2.2f\tE: %2.2f\tP: %2.2f\n", prome[18], prome[19], prome[20]);
  
}


int main() {

  struct Proceso ejemplo[5];
  struct Proceso lista1[5], lista2[10], lista3[15];
  srand(time(NULL));
  int aux;

  printf("\n\n ~ ~ ~ Bienvenido al simulador de algoritmos de planificacion. ~ ~ ~\n\n");
  printf(" Se presentan 4 simulaciones para los algoritmos, la vista en\n");
  printf(" clase y otras 3 aleatorias de 5, 10 y 15 procesos respectivamente.\n\n");

  //Ejemplo en clase -- inicialización
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

  printf("\n\n\n-----------------------------------------------------------------------------");
  printf("\n Tabla de procesos, caso 1:\n");

  simulacion(ejemplo, 5);

  // Aleatorio de 5 procesos.
  printf("\n\n\n-----------------------------------------------------------------------------");
  printf("\n Tabla de procesos, caso 2:\n");
  aux = 0;
  for(int i=0; i<5; i++){
    lista1[i].nombre = (char)(65+i);
    if(i!=0){
      aux+=rand()%5;
      aux++;
    }
    lista1[i].llegada = aux;
    lista1[i].requerido = (rand()%12)+1;
  }

  simulacion(lista1, 5);


  // Aleatorio de 10 procesos.
  printf("\n\n\n-----------------------------------------------------------------------------");
  printf("\n Tabla de procesos, caso 3:\n");
  aux = 0;
  for(int i=0; i<10; i++){
    lista2[i].nombre = (char)(65+i);
    if(i!=0){
      aux+=rand()%5;
      aux++;
    }
    lista2[i].llegada = aux;
    lista2[i].requerido = (rand()%12)+1;
  }

  simulacion(lista2, 10);

  // Aleatorio de 15 procesos.
  printf("\n\n\n-----------------------------------------------------------------------------");
  printf("\n Tabla de procesos, caso 4:\n");
  aux = 0;
  for(int i=0; i<15; i++){
    lista3[i].nombre = (char)(65+i);
    if(i!=0){
      aux+=rand()%5;
      aux++;
    }
    lista3[i].llegada = aux;
    lista3[i].requerido = (rand()%12)+1;
  }

  simulacion(lista3, 15);


  printf("\n\n\n\n\n - - - - - - - - - - - - - -  FINAL SIMULACIÓN - - - - - - - - - - - - - \n\n\n\n");
  
  return 0;
}

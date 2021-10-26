#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>

int trabajar();

// Declaración semaforos (torniquetes y mutex) globales
sem_t mutex;
sem_t mutexElfoSanta;
sem_t mutexSanta;
sem_t torniqueteEntradaRenos;
sem_t torniqueteSalidaRenos;
sem_t mutexRenos;
sem_t multiplexElfos;

// Declaración e inicialización de de variables de condición
pthread_mutex_t mutexCVSanta = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cvSanta = PTHREAD_COND_INITIALIZER;

pthread_mutex_t mutexCVRenos = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cvRenos = PTHREAD_COND_INITIALIZER;

pthread_mutex_t mutexCVElfos = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cvElfos = PTHREAD_COND_INITIALIZER;

pthread_barrier_t barreraElfos;
pthread_barrier_t barreraRenos;

// Declaración variables globales
int numElfo=1;
int esperaElfo=0;
int elfos[3]={0,0,0};
int numReno=1;
int esperaReno=9;
int trabajoSanta=0;

// Hilo de Santa Claus
void* santa(void* args) {
	
	while(1) {
		
		while(!trabajoSanta){ // se duerme hasta que le avisen para checar condición
			pthread_cond_wait(&cvSanta, &mutexCVSanta);
		}
		sem_wait(&mutexElfoSanta); // toma Mutex para que Elfos no trabajen
		printf("\n\n° SANTA CLAUS HA DESPERTADO !!!");
		if(trabajoSanta==1){
			printf("\n__________________________________________________________________________");
			printf("\n° 'SANTA': Ayudando a mis queridos elfos con sus problemas ... \n");
			printf("      Santa ayudó a los elfos: '%d', '%d' y '%d'\n", elfos[0], elfos[1], elfos[2]);
			printf("__________________________________________________________________________-\n");
			trabajoSanta=0;
			pthread_cond_signal(&cvElfos); // Avisa a elfos que resolvió sus problemas
		} else if (trabajoSanta==2) {
			printf("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
			printf("\n° Es 24 de diciembre, todos duermen por la noche ...\n° Santa Claus tiene todos sus renos y vuela para entregar los regalos ...\n");
			printf("\n°°° FELIZ NAVIDAD °°°\n");
			printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n");
			trabajoSanta=0;
			pthread_cond_signal(&cvRenos); // Avisa a renos que pueden irse de vacaciones
		}
		sem_post(&mutexElfoSanta); // Libera mutex para dejar trabajar a elfos
    }
}

//Hilo de elfo ayudante de Santa
void* elfo(void* args) {
	sem_wait(&mutex);
	int num = numElfo; // darles un valor reconocible a los elfos mediante un torniquete
	numElfo++;
	sem_post(&mutex);
	
	while(1){
		
		if(trabajar()) { // Entran hilos con problemas
			
			sem_wait(&mutexElfoSanta); // Candado un hilo con problemas a la vez, protege a Santa y valores
			elfos[esperaElfo]=num;
			esperaElfo++;
			printf("\n El elfo %d tiene problemas, hay %d elfos con problemas.", num, esperaElfo);
			if(esperaElfo==3) {
				sem_wait(&mutexSanta); // Evita que los renos puedan llamar a Santa
				trabajoSanta=1;
				pthread_cond_signal(&cvSanta); // Despierta a Santa
				while(!trabajoSanta) {
					pthread_cond_wait(&cvElfos, &mutexCVElfos); // Espera señal terminal de Santa
				}
				sem_post(&mutexSanta); // Libera la llamada de Santa
				esperaElfo=0;
			}
			sem_post(&mutexElfoSanta); // libera candado cuando espera a llegar a 3, o Santa ya les ayudó
		}
		
		sleep(0.5); //descanso
	}
}

// Función de simulación de trabajo y problemas de los elfos.
int trabajar() {
	sleep(1);
	srand(time(NULL));
	if(rand()%2==1)
		return 1;
	return 0;
}

// Hilo de los renos
void* reno(void* args) {
	sem_wait(&mutex);
	int reno = numReno; // darles un valor reconocible a los renos mediante un torniquete
	numReno++;
	sem_post(&mutex);
	
	while(1) {
		
		sem_wait(&torniqueteSalidaRenos); // se abre o cierra el torniquete desde el hilo tiempo
		esperaReno--;
		printf(" *** Se va el reno %d\n", reno);
		if(!esperaReno){
			sem_post(&mutexRenos); // si es el último reno libera el candado para el hilo del tiempo
		}
		sem_post(&torniqueteSalidaRenos); // se libera torniquete
		
		pthread_barrier_wait(&barreraRenos); // Esperan a llegar los 9 renos para irse.
		if(reno==1)
			printf("* Todos los renos se han ido de vacaciones ...\n");
		
		
		sem_wait(&torniqueteEntradaRenos); // se abre o cierra el torniquete desde el hilo tiempo
		esperaReno++;
		printf(" -- Ya llegó el reno %d, hay %d renos en el polo norte!\n", reno, esperaReno);
		sem_post(&torniqueteEntradaRenos);
		
		pthread_barrier_wait(&barreraRenos); // esperan a llegar los 9 renos para avisarle a Santa
		
		if(reno==1){ // El reno 1 siempre es el que avisa y espera, los demás lo esperan en el torniquete cerrado.
			printf("\n- Ya están todos los renos listos en el trineo.\n");
			sem_wait(&mutexSanta);
			trabajoSanta=2;
			pthread_cond_signal(&cvSanta); // avisa a Santa
			while(!trabajoSanta) {
				pthread_cond_wait(&cvRenos, &mutexCVRenos); // espera a Santa
			}
			sem_post(&mutexSanta);
			sem_post(&mutexRenos);
		}
		
	}
	
}



int main() {
	
	//declaracion variables creación de hilos
	pthread_t pidSanta;
	pthread_t pidRenos[9];
	pthread_t *pidElfos;
	
	// declaración variables para crear e inicializar hilos
	int elfos;
	int i=0;
	int aux;
	int mes = -1;
	
	// inicialización de semaforos, barreras.
	sem_init(&mutex,0,1);
	sem_init(&mutexElfoSanta,0,1);
	sem_init(&mutexSanta, 0,1);
	sem_init(&torniqueteEntradaRenos, 0, 0);
	sem_init(&torniqueteSalidaRenos, 0, 0);
	sem_init(&mutexRenos, 0, 0);
	pthread_barrier_init(&barreraElfos, NULL, 3);
	pthread_barrier_init(&barreraRenos, NULL, 9);
	
	// Creación del hilo Santa Claus
	if(!pthread_create(&pidSanta,NULL,&santa,NULL)){
		printf("\n ~ Santa Claus ha llegado ...\n\n");
	}
	// Creación de los hilos de renos
	for(i=0; i<9; i++){
		if(!pthread_create(&pidRenos[i],NULL,&reno,NULL))
			printf(" Reno %d ha sido adoptado...\n", i+1);
	}
	// Pregunta y creación de los hilos de x número de elfos
	printf("\n Cuántos elfos desea que ayuden a Santa?: ");
	scanf("%d", &elfos);
	pidElfos=malloc(elfos*sizeof(pthread_t));
	aux=elfos;
	// --> Inicia creación bajo candado (torniquete cerrado) con los elfos, para que no se etorben hasta estar todos.
	sem_wait(&mutex);
	while(aux-- && !pthread_create(&pidElfos[elfos-aux-1],NULL,&elfo,NULL)){
	}
	if(aux)
		printf("\n ~ Todos los %d elfos han sido contratados...\n", elfos);
	
	printf("\n |*******************************************************|");	
	printf("\n |-----------------  EMPIEZA TRABAJO  -------------------|");
	printf("\n |*******************************************************|\n");
	
	// --> Se libera el torniquete para que todos los hilos puedan trabajar.
	sem_post(&mutex);
	
	// declaración de los meses, el hilo principal llevará el "paso" del tiempo.
	char *meses[12] = {"ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO",
						"AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"};
	
	// PASO DEL AÑO
	while(1) {
		mes++;
		mes%=12;
		sleep(1);
		printf("\n\n |.........................................  Mes: %s  ...................................|\n\n", meses[mes]);
		if(mes==0) { // Se van los renos de vacaciones, todos juntos. (ENERO)
			sem_post(&torniqueteSalidaRenos);
			sem_wait(&mutexRenos);
			sem_wait(&torniqueteSalidaRenos);
		} else if(mes==11) { // regresan los renos de vacaciones a diferentes tiempos. (DICIEMBRE)
			sem_post(&torniqueteEntradaRenos);
			sem_wait(&mutexRenos);
			sem_wait(&torniqueteEntradaRenos);
		}
    }
	
	return 0;
}

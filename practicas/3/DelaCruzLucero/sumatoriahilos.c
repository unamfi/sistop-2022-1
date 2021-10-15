#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
 
struct hilos_random_parms
{
    int randi;
    int index;
};
 
int aleatorios[5];
 
void* hilos_random(void* parameters)
{
    struct hilos_random_parms* p = (struct hilos_random_parms*)parameters;
    int cont = p->index;
    srand(time(NULL) + cont);
    aleatorios[cont] = (rand() % p->randi) + 1;
    printf("Número aleatorio: (%d) %d \n", cont, aleatorios[cont]);
    cont++;
    return NULL;
}
 
int main()
{
    pthread_t thread1_id;
    pthread_t thread2_id;
    pthread_t thread3_id;
    pthread_t thread4_id;
    pthread_t thread5_id;
 
    struct hilos_random_parms thread1_args[5];
    int i;
    for(i = 0; i < 5; i++) {
        thread1_args[i].randi = 10;
        thread1_args[i].index = i;
    }
 
 
    pthread_create(&thread1_id, NULL, &hilos_random, &thread1_args[0]);
    pthread_create(&thread2_id, NULL, &hilos_random, &thread1_args[1]);
    pthread_create(&thread3_id, NULL, &hilos_random, &thread1_args[2]);
    pthread_create(&thread4_id, NULL, &hilos_random, &thread1_args[3]);
    pthread_create(&thread5_id, NULL, &hilos_random, &thread1_args[4]);
 
    pthread_join(thread1_id, NULL);
    pthread_join(thread2_id, NULL);
    pthread_join(thread3_id, NULL);
    pthread_join(thread4_id, NULL);
    pthread_join(thread5_id, NULL);
 
    int total = 0;
    for (i = 0; i < 5; i++)
    {
        total += aleatorios[i];
    }
 
    printf("Suma de los números: %d \n", total);
 
    return 0;
}

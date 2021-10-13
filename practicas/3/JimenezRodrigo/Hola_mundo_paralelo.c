#include <stdio.h>
int main()
{
    int tid,nth,j,X;
    #pragma omp parallel num_threads(4)
    //#pragma omp parallel
    {
        int i;
        printf("Hola Mundo\n");
        tid=omp_get_thread_num();
        nth=omp_get_num_threads();
        X=omp_get_max_threads( );
        printf("DISPONIBLES: %d \n",X);
        for (i=0;i<10;i++)
        printf("Iteracion: %d desde el hilo %d de un total de %d\n",i,tid,nth);
    }
    printf("Adios \n");
    return 0;
}

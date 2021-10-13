//Ejercicio EDAII. Profesor Francisco Javier Rodriguez

/*Instrucción de compilación
    gcc -Wall -std=c99 hilos.c -fopenmp
*/

#include <stdio.h>

#include <stdlib.h>
// para system() y rand()

#include <time.h>
// para time()

#include <omp.h>

#define TAM 10

int main()
{
    int a[TAM];
    int b[TAM];
    srand( time( NULL ) );

    #pragma omp parallel num_threads( 4 )
    {
        //#pragma omp single
        {
            printf( "Thread %d\n", omp_get_thread_num() );

            for( size_t i = 0; i < TAM; ++i ){
                a[ i ] = rand() % 100;
                printf( "a[%d] = %d\n", i, a[i] );
            }
        } // --- Implicit barrier

        #pragma omp for
            for( size_t i = 0; i < TAM; ++i ){
                b[ i ] = a[ i ] * 2;
            } // --- Implicit barrier

       // #pragma omp single
        {
            for( size_t i = 0; i < TAM; ++i ){
            printf( "Thread(%d): b[%d] = %d\n", omp_get_thread_num(), i, b[i] );
            }
        } // --- Implicit barrier

    } // --- Implicit barrier
} 
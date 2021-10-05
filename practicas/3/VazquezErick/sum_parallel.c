//Ejercicio EDA 2 Prof. Francisco Rodriguez

#include <stdio.h>
#include <stdlib.h>
// para la función rand()
#include <time.h>
// para inicializar la semilla de aleatoriedad
#include <omp.h>
// para las funciones de biblioteca de OpenMP
// No vamos a usar esta función, pero está aquí para que se vea la
// diferencia con su contraparte paralela.

void sum_sec( int arr1[], int arr2[], int res[], int tam ) {

    for( int i = 0; i < tam; ++i ){
        res[ i ] = arr1[ i ] + arr2[ i ];
    }
}

void sum_par( int arr1[], int arr2[], int res[], int tam ) {

#pragma omp parallel for num_threads( 4 )

    for( int i = 0; i < tam; ++i ) {

        printf( "The thread %d is calculating res[ %d ]\n", omp_get_thread_num(), i );
        res[ i ] = arr1[ i ] + arr2[ i ];
    }
}

#define TAM 10

int main() {

    int a[ TAM ];
    int b[ TAM ];
    int c[ TAM ];
    srand( time( NULL ) );

    for( int i = 0; i < TAM; ++i ) {

        a[ i ] = rand() % 100;
        b[ i ] = rand() % 100;
    }

    sum_par( a, b, c, TAM );
    for( int i = 0; i < TAM; ++i ) {

        printf( "%2d) %d + %d = %d\n", i + 1, a[ i ], b[ i ], c[ i ] );
    }

}
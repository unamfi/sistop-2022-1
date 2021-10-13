#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<omp.h>

int n;
void buscaMaximo(int a[][n],int A[3]);
void llenarArreglo(int a[][n]);

int main(){
	int retorno;
	printf("Inserta la longitud del arreglo:"); //Introducir un valor procesable menor que 1000, para el caso de mi equipo :(
	scanf("%d",&n);
	int A[n][n];
	int B[3];

	llenarArreglo(A);
	buscaMaximo(A,B);

	printf("Maximo: %d\n",B[0]);
	printf("Renglon: %d\n",B[1]);
	printf("Columna: %d\n",B[2]);

	return 0;
}

void buscaMaximo(int a[][n],int A[3]){
	int max=0,i,j;
	#pragma omp parallel for private (j)//Permite que los for se dividan las operaciones de forma equivalente.
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(a[i][j]>max){
				#pragma omp critical //Implementacion del mutex, solo ejecuta un hilo a la vez
				{
					if(a[i][j]>max){
						max=a[i][j];
						A[0]=max;
						A[1]=i;
						A[2]=j;
					} 
				}
			}
		}
	}
}

void llenarArreglo(int a[][n]){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			a[i][j]=rand(); 
			printf("%d\t",a[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}
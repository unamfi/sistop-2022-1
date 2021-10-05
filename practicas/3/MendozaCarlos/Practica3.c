#include<stdio.h>
#include<omp.h>
int buscaMaximo(int *a, int n){ 
	int max,i;
	max=a[0]; 
	for(i=1;i<n;i++) {
	if(a[i]>max)
	max=a[i];
	}
return max;
}

int main(){
	int n,i;
	printf("Ingresa el numero de elementos del arreglo: ");
    scanf("%d",&n);
    int a[n]; 
    for(i=0; i<n; i++)
    {
        printf("Ingresa el elemento numero %d del arreglo: ", (i+1) );
        scanf("%d",&a[i]);
    }
    printf("El numero máximo es: %d",buscaMaximo(a,n));
}

#include <stdio.h>

struct Vehiculo{
    int ruedas;
    int precio;
    char color[15];
    char nombre[15];
};

void presentacion(struct Vehiculo v){

    printf("este vehiculo se llama %s \n tiene %i ruedas\n es de color %s\n cuesta $%i\n",v.nombre, &v.ruedas, v.color, &v.precio);
}

int main(){

    struct Vehiculo vehiculos[] = { {2,100, "verde", "moto"}, {4,100, "rojo", "auto"}, {6,1000, "negro", "camion"}};
    int count = 3;

    for (size_t i = 0; i < count; i++){
        presentacion(vehiculos[i]);
    }
    return 0;
}
/*
  Proyecto 1 para la materia de Sistemas Operativos, grupo 6.

  Desarrollado por IÑAKY ORDIALES CABALLERO

  Profesor: Gunnar Eyal Wolf Iszaevich
  Semestre: 2022-1
  Facultad de Ingeniería, UNAM.

  Instrucciones.
  Implementen un programa que simule un proceso de la vida real
  que presente características de concurrencia, necesariamente
  empleando hilos o procesos simultáneos. 
  Implementen una interfaz de ususario profesional, que demuestre
  cómo la sincronización puede ser bella y elegante.

*/

/*
         "Simulación de centro comercial en pandemia"

  Para este desarrollo se decicdió el simular la afluencia y 
  compras de un centro comercial durante esta época de pandemia. 
  El usuario indicará el semáforo que limita el cupo máximo de
  las instalaciones, el número de clientes que desean acceder al
  centro comercial y el tiempo en segundos que permanecerán 
  abiertas las instalaciones.


 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <ncurses.h>

// Declaración funciones prototipo


// Declaración semáforos (torniquetes y mutex) globales


// Declaración e inicialización de variables de condición


// Declaración variables globales


// Hilo cliente

// Hilo cajero

// Hilo seguridad





int main() {

  int capacidad;
  int semaforoPandemia;
  int clientes;
  int tiempo;
  
  printf(" Bienvenido al simulador de Centro Comercial SISTOP\n\n");
  printf("~Se simulará el flujo de un centro comercial durante la época de\n");
  printf(" pandemia. La plaza tendrá un cupo máximo delimitado por su capacidad\n");
  printf(" máxima y por el semáforo epidemiológico.\n\n");
  printf("~El centro comercial cuenta con 5 tiendas:\n");
  printf("\t- Una tienda departamental grande (10 cajeros)\n");
  printf("\t- Un supermercado grande (4 cajeros)\n");
  printf("\t- Una tienda de ropa mediana (2 cajeros)\n");
  printf("\t- Una tienda de tecnología chica (1 cajero)\n");
  printf("\t- Un kiosko para trámites del gobierno (1 ventanilla)\n\n");
  printf("~Los clientes podrán entrar tanto a la plaza como a las tiendas sólo si\n");
  printf(" van a realizar una compra y el cupo máximo no ha sido superado.\n\n");
  printf("*** A conitnuación se le solicitarán los valores para la simulación,\n");
  printf("    por favor ingréselos según se le solicitan.\n\n");
  printf(" ¿Cuál será la capacidad máxima del centro comercial?\n");
  printf(" (Tome en cuenta las siguientes capacidades para las tiendas:\n");
  printf("   - Departamental -> 40% de la capacidad de la plaza.\n");
  printf("   - Supermercado  -> 20% de la capacidad de la plaza.\n");
  printf("   - Ropa -> 10% de la capacidad de la plaza.\n");
  printf("   - Tecnología -> 5% de la capacidad de la plaza.\n");
  printf("   - Kiosko -> 5
  scanf("%d", &capacidad);
  printf(" 
  printf("Semáforo verde(80%), amarillo(60%), naranja(40%), rojo(%30%)\n");
  scanf("%d", &semaforoPandemia);
  printf("1 hora = 5 segundos de simulación\n");
  printf("Cuántas horas al día abrirá sus puertas?: ");
  scanf("%d", &tiempo);
  printf("Cuántas personas querrán entrar a la plaza durante el día?: ");
  scanf("%d", &clientes);

  
  

  return 0;
}

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
  
  /*

  // inititalizes the screen
  // sets up memory and clears the screen
  initscr();

  // prints a string(const char *) to a window
  //printw("Hello world!\n");

  int height=10;
  int width=20;
  int start_y=10;
  int start_x=10;

  WINDOW * win =newwin(height, width, start_y, start_x);
  refresh();
  box(win,0,0);
  mvwprintw(win,1,1,"this is my box");
  wrefresh(win);
  

  // refreshes the screen to match whats in memory
  //refresh();

  // whats for user input, returns int value of that key
  int c=getch();
  wprintw(win,"\n%d\n", c);

  getch();


  // deallocates memory and ends ncurses
  endwin();
  */

  return 0;
}

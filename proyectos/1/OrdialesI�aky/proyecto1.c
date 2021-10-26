/* Proyecto 1 de la materia de Sistemas Operativos */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <ncurses.h>

int main() {

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


  return 0;
}

#include <stdio.h>
int main() {
double x = 1.0;
int n = 0;
while (1.0 + (x * 0.5) > 1.0) {
++n; x *= 0.5;
}
printf("Epsilon de la maquina en forma binaria = 2^(-%d)\n", n);
printf("Epsilon de la maquina en forma decimal = %G\n", x);
return 0;
}

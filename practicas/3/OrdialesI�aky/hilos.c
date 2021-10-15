#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main() {

    FILE *fptr = NULL;

    pid_t pid;
    pid = fork();

    if(pid == -1) {
        printf("Fallo en fork del proceso\n");
        return -1;
    } else {
        if (pid > 0) {
            printf("Soy el padre: PID %d\n", getpid());
	    fptr = fopen("PID_padre.txt", "w");
	    if (fptr == NULL)  {
		printf("No se pudo crear el archivo del padre\n");
		return -1;
	    } else {
		fprintf(fptr, "Soy el padre de todos los hilos.\nMi PID es: %d\n", getpid());
		fclose(fptr);
	    }
        } else {
            printf("Soy el hijo: PID %d\n", getpid());
            fptr = fopen("PID_hijo.txt", "w");
	    if (fptr == NULL)  {
		printf("No se pudo crear el archivo del hijo\n");
		return -1;
	    } else {
		fprintf(fptr, "Soy el hijo del padre.\nMi PID es: %d\n", getpid());
		fclose(fptr);
	    }
	    pid=fork();

            if(pid == -1) {
	        printf("Fallo en fork del hijo\n");
		return -1;
	    } else {
		if(pid > 0) {
		    printf("Soy el hijo (padre del nieto): PID %d\n", getpid());
		} else {
		    printf("Soy el nieto: PID %d\n", getpid());
		    fptr = fopen("PID_nieto.txt", "w");
	    	    if (fptr == NULL)  {
			printf("No se pudo crear el archivo del nieto\n");
			return -1;
	            } else {
			fprintf(fptr, "Soy el nieto del padre.\nMi PID es: %d\n", getpid());
			fclose(fptr);
	    	    }
		    pid=fork();

		    if(pid == -1) {
			printf("Fallo en fork del nieto\n");
			return -1;
		    } else {
			if( pid > 0) {
			    printf("Soy el nieto (padre del bisnieto): PID %d\n", getpid());
			} else {
			    printf("Soy el bisnieto: PID %d\n", getpid());
			    fptr = fopen("PID_bisnieto.txt", "w");
	    	    	    if (fptr == NULL)  {
				printf("No se pudo crear el archivo del bisnieto\n");
				return -1;
	            	    } else {
				fprintf(fptr, "Soy el bisnieto del padre.\nMi PID es: %d\n", getpid());
				fclose(fptr);
	    	    	    }
			}
		    }
		}
	    }
        }
    }
}

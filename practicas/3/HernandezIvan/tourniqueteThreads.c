/*		
 *			National Autonomus of Mexico
 *				Faculty of Engineering
 *					Operating Systems
 *		Developers:
 *			Hernández Campuzano Iván
 *		Master:
 *			Gunnar Wolf
 *		Description: 
 *			Solution of the problem of tourniquets with dekker algorithm 
 *		Biografy:
 *			1. Wolf G., Ruiz E., Bergero F. & Meza E., 2015, 
 *			Fundamentos de  Sistemas Operativos, Primera Edición, México D.F. Univercidad Nacional Autónoma de México, Instituto de Invetigaciones Economics,Facultad de Ingneiería.
 *			2. https://www.um.es/earlyadopters/actividades/a3/PCD_Activity3_Session1.pdf
 *      */

#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
int count = 0;
int langOne, langTwo, whoIs;

void *tourniquetOne(void *arg){
	for(int i=0;i<20;i++){
		langOne = 1;
		whoIs = 2; // 2 -> tourniqueteTwo	
		if(langTwo && (whoIs==2)){
			usleep(1000000);
		}
        count++;
        printf("I'm touniquet one : %d\n",count);
        langOne = 0;
	}
}
void *tourniquetTwo(void *arg){
	for(int i=0;i<20;i++){
		langTwo = 1;
        whoIs = 1; // 1 -> tourniqueteOne
		if(langOne && (whoIs==1)){
			usleep(1000000);
		}
		count++;
		printf("I'm tourniquet two :%d\n",count);
		langTwo = 0;
	}
}
int main(int argc, char *argv[]){
	pthread_t process1;
	pthread_t process2;
	pthread_create(&process1, NULL, &tourniquetOne, NULL);
	pthread_create(&process2, NULL, &tourniquetTwo, NULL);
	pthread_join(process1,NULL);
	pthread_join(process2,NULL);
	return 0;
}	

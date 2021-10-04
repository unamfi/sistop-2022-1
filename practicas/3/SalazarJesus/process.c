#include <stdio.h>
int main () {
int pid;

printf ("I'm the original process with PID %d and PPID %d.\n", getpid(), getppid());
pid = fork (); /* Duplicate. Child and parent continue from here */

if (pid != 0) /* pid is non-zero, so I must be the parent */
{
printf ("I'm the parent process with PID %d and PPID %d.\n",
getpid (), getppid ());
printf ("My child's PID is %d\n", pid);
}

else /* pid is zero, so I must be the child */
{
printf ("I'm the child process with PID %d and PPID %d.\n",
getpid (), getppid ());
}

printf("PID %d terminates.\n",getpid ());/*Both procs execute this */
return 0;

}
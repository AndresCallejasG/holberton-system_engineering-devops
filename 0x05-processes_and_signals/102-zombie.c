#include <stdio.h>
#include <unistd.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - program that creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - not main
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

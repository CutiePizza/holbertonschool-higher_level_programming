#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

#include<pthread.h>

int a;


void *pair(void *arg)
{
	int i;

	for(i=0;i<a;i++)
		if(i%2==0)
		{
			printf("les nombres paires sont %d\n",i);
		}
}


void *impair(void *arg)
{
	int i;

	for(i=0;i<a;i++)
		if(i%2!=0)
		{
			printf("les nombres impaires sont %d\n",i);
		}
}


void main()
{
	printf("donnz un entier ");
	scanf("%d",&a);
	pthread_t  thread1, thread2;
	pthread_create(&thread1,NULL,pair,NULL);
	pthread_create(&thread2,NULL,impair,NULL);
	pthread_join(thread1,NULL);
	pthread_join(thread2,NULL);
}

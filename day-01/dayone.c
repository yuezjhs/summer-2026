#include <stdio.h>
int main()
{
	int a=42;
	int *p=&a;//&取地址符：获取a的内存地址
	printf("\na的值：%d\n",a); 
	printf("a的地址：%p\n",&a); 
	printf("\np的值：%p\n",p); 
	printf("*p的值：%d\n",*p); 
	printf("p自己的地址：%p\n",&p);
	return 0; 
 } 
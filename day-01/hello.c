#include <stdio.h>
int main(void)
{
    int a=42;
    printf("a的值：%d\n",a);
    printf("a的地址：%p\n",(void*)&a);
    return 0;
}
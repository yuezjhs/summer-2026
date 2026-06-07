#include <stdio.h>
int my_strlen(const char *str)//strlen函数实现
{
	const char *p=str;//指针指向数组的第一个元素
	while(*str!='\0')
	{
		str++;
	}
	return str-p;//计算字符数组的\0之前的个数
}
int main()
{
	char str[]="hello world";
	printf("字符的个数：%d",my_strlen(str));//输出并调用函数
	return 0;
}
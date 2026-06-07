#include<stdio.h>
int main()
{
	int arr[]={10,20,30,40,50};
	int len=sizeof(arr)/sizeof(arr[0]);//计算数组长度
	int sum=0;//定义累加器
	int *p=arr;//指针p指向数组arr的第一个值
	for(int i=0;i<len;i++)
	{
		sum+=*(p+i);
	}
	printf("数组总和：%d\n",sum);//输出总和


    //找出数组内的最大值
	int max=*arr;//默认第一个最大
	p=arr;//重新指向第一个元素
	while(p<arr+len)
	{
		if(*p>max)
		{
			max=*p;
		}
		p++;
	}
	printf("数组最大值：%d\n",max);
	return 0;
 } 
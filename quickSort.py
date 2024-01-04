#include<iostream>
using namespace std;
void swap(int *a,int *b)
{
int t=*a;
*a=*b;
*b=t;
}
void printArray(int array[],int size)
{
int i;
for(i=0;i<size;i++)
cout<<array[i]<<" ";
cout<<endl;
}
int partition(int array[],int low,int high)
{
int pivot=array[high];
int i=(low-1);
for(int j=low;j<high;j++)
{ 
if(array[j]<=pivot)
{
i++;
swap(&array[i],&array[j]);
}
}
swap(&array[i+1],&array[high]);
return(i+1);
}
void quicksort(int array[],int low,int high)
{
if(low<high)
{
int pi=partition(array,low,high);
quicksort(array,low,pi-1);
quicksort(array,pi+1,high);
}
}
int main()
{
int data[]={2,5,3,7,1,9};
int n=sizeof(data)/sizeof(data[0]);
cout<<"Unsorted Array:\n";
printArray(data,n);
quicksort(data,0,n-1);
cout<<("Sorted array in ascending order:\n");
printArray(data,n);
}

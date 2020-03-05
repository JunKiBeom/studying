#include <stdio.h>

int seq_search(int array[], int search_num, int n) // O(n)
/* n개의 원소를 가진 배열에서 search_num 순서대로 찾아서 있으면 그의 지수를 반환, 없으면 -1 */
{
    int i;
    array[n]=search_num;
    for(i=0;array[i]!=search_num;i++);
    return ((i<n)?i:-1);
}

int binary_search(int array[], int search_num, int left, int right) // O(n log n)
/* 배열에서 search_num이 있는가를 탐색, 있으면 그 위치와 index반환, 없으면 -1 */
{
    int middle;
    while (left<=right)
    {
        middle = (left+right)/2;
        if (array[middle]<search_num)
            left=middle+1;
        else if (array[middle]>search_num)
            right=middle-1;
        else
            return middle;
    }
    return -1;
}

void bubble_sort(int array[], int n) // O(n^2)
/* 버블 정렬을 이용하여 배열을 오름차순 정렬 */
{
    int i, j, tmp;
    for (i=0;i<n-1;i++)
        for (j=0;j<n-1;j++)
        {
            if(array[j]>array[j+1])
            {
                tmp=array[j];
                array[j]=array[j+1];
                array[j+1]=tmp;
            }
        }
}
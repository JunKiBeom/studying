#include <stdio.h>
int card_convr (unsigned x, int n, char d[])
{
    char dchar[]="0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ";
    int digits=0;
    if (x==0)
        d[digits++]=dchar[0];
    else
        while (x)
        {
            d[digits++]=dchar[x%n];
            x/=n;
        }
    return digits;
}
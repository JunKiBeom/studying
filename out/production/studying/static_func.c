#include <stdio.h>
short test_static_cnt()
{
    static short cnt=0;  // 이전값 지속적으로 유지
    cnt++;
    return cnt;
}

short test_cnt()
{
    short cnt=0; // 함수 재실행 마다 리셋
    cnt++;
    return cnt;
}

int main()
{
    int i=0;
    while (i<30)
    {
        printf("cnt = %d\n",test_cnt());
        printf("static cnt = %d\n",test_static_cnt());
        i++;
    }
    
}
/* 정수를 2진수 ~ 36진수로 기수 변환 */
#include <stdio.h>
/* unsigned int의 가장 큰 숫자는 4,294,967,295 2진수 변환시 11111111111111111111111111111111 최대 32자리 전역 변수 선언으로 접근 용이 */
char result[32]={0};
/* 정수 값 x를 n진수로 변환하여 배열 d에 아랫자리부터 저장 */
int card_convr (unsigned x, int n)
{
    char dchar[] = "0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ";
    int digits = 0;    // 변환 후 자릿수
    if (x == 0)    // 0이면
        result[digits++] = dchar[0];    // 변환 후에도 0
    else
        while (x)
        {
            result[digits++] = dchar[x%n];    // n으로 나눈 나머지를 저장
            x/=n;
        }
    return digits;
}

/* 실행 예시 */
int main()
{
    unsigned int num;
    int n;
    scanf("%d %d",&num,&n);    // 숫자를 입력받고 변환 할 진수 입력
    card_convr(num,n);
    printf("Convert %d to (%d) : ",num,n);
    for (int i=31;i>0;i--)
        printf("%c",result[i]);
    printf("\n");
}
#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp = NULL;
    char fname[256] = {0};
    char buff[256] = {0};
    char word[256] = {0};
    int line = 0;
    int fcnt = 0;

    printf("파일 이름을 입력하세요 : ");
    scanf("%s", fname);

    printf("탐색할 단어를 입력하세요 : ");
    scanf("%s", word);

    printf("\n");

    if ((fp = fopen(fname,"r"))==NULL)
        fprintf(stderr, "파일 %s를 열 수 없습니다.\n", fname);

    while (fgets(buff,256,fp))
    {
        line++;
        if (strstr(buff,word))
        {
            printf("라인 %d : 단어 %s가 발견되었습니다.\n", line, word);
            fcnt++;
        }
    }
    if (fcnt==0)
        printf("발견된 단어가 없습니다.\n");

    fclose(fp);
}
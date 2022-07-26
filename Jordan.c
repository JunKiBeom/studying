#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>
#pragma warning (disable:4996)

void Jordan();

int main()	// 10*10
{
	srand((unsigned int)time(NULL));
	Jordan(10);
	//Jordan(4);
}

void Jordan(int a) {
	int s = 0;								// 입력값 판별용
	int random1, random2 = 0;				// 랜덤번호 출력
	int all = a*10;							// 경품의 수
	int** arr = malloc(sizeof(int *) * a);	// 10*10 창고
	for (int i = 0; i < a; i++) {
		arr[i] = malloc(sizeof(int) * 10);
	}

	// 보드 세팅
	int tmp = 1;
	for (int i = 0; i < a; i++)
		for (int j = 0; j < 10; j++)
			arr[i][j] = tmp++;

	while (1) {
		printf("★★★★★★★★★ 조던링 뽑기 ★★★★★★★★★\n\n");
		printf("랜덤으로 뽑을 갯수 입력\n0 입력시 종료\n입력 : ");
		scanf("%d", &s);


		if (s < 0 || s > all) {	// 범위 초과시 재입력
			printf("\n숫자를 다시 넣어주세요\n");
			system("pause");
		}

		else if (s == 0) {	// 0 입력시 종료
			printf("\n★이벤트 종료!★\n");
			system("pause");
			break;

		}

		else {	// 랜덤 뽑기!
			int cnt = 0;
			printf("\n행운 번호 : ");

			for (int i = 0; (cnt < s) && all != 0; i++) {
				random1 = rand() % a;
				random2 = rand() % 10;

				if (arr[random1][random2] != 0) {	// 중복 확인
					arr[random1][random2] = 0;
					printf("%d ", random1 * 10 + random2 + 1);
					cnt++; all--;
				}
			}

			// 보드 출력
			printf("\n\n");
			for (int i = 0; i < a; i++) {
				for (int j = 0; j < 10; j++) {
					printf("%3d ", arr[i][j]);
				}
				printf("\n");
			}
			if (all == 0) {
				printf("\n★이벤트 종료!★\n");
				system("pause");
				break;
			}
			system("pause");
		}
		system("cls");
	}
}